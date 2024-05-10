from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from core.utils import *
from .models import *
from django.db.models import Q

# Authentication
def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')


    return render(request, 'account/login.html')
@login_required
def logout_url(request):
    logout(request)
    return redirect('login')



# Dashboard Functions
@login_required
def dashboard(request):
    teams = Employee.objects.filter(assigned_to=request.user).exclude(groups__name='Manager') if has_group(request.user, 'Manager') else Employee.objects.filter(assigned_to=request.user.assigned_to).exclude(groups__name='Manager')
    frees = Employee.objects.filter(wrk_status='AV').exclude(assigned_to=request.user)
    books =  Employee.objects.filter(booked_by=request.user).exclude(assigned_to=request.user)
    managers = Employee.objects.filter(groups__name='Manager').exclude(id=request.user.id)


    data = {
        'teams' : teams,
        'frees' : frees,
        'books' : books,
        'managers' : managers,
        'total_team_member' : teams.count()
    }
    return render(request, 'account/dashboard.html', data)

@login_required
def book(request, id):
    employee = Employee.objects.get(id=id)
    if employee.assigned_to == request.user:
        employee.wrk_status = 'WK'
        employee.booked_by = None
        employee.save()
    else:
        employee.wrk_status = 'BK'
        employee.booked_by = request.user
        employee.save()
    return redirect('dashboard')

@login_required
def free(request, id):
    employee = Employee.objects.get(id=id)
    if employee.wrk_status == 'AS':
        employee.wrk_status = 'WK'
        employee.booked_by = None
        employee.save()
    else:
        employee.wrk_status = 'AV'
        employee.booked_by = None
        employee.save()
    return redirect('dashboard')

@login_required
def assist(request, id):
    if request.method == 'POST':
        employee = Employee.objects.get(id=id)
        employee.wrk_status = 'AS'
        employee.booked_by = Employee.objects.get(id=request.POST['inassist'])
        employee.save()

    return redirect('dashboard')

@login_required
def employees(request):
    employees = Employee.objects.all().exclude(is_superuser=True).order_by('first_name')

    data = {
        'employees' : employees
    }
    return render(request, 'account/employees.html', data)

