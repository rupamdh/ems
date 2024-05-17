from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from core.utils import *
from .models import *
from .forms import *
from .decorators import is_group
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


#Employee
@login_required
@is_group('HR')
def employees(request):
    employees = Employee.objects.all().exclude(is_superuser=True).order_by('first_name')

    data = {
        'employees' : employees
    }
    return render(request, 'account/employees.html', data)

@login_required
@is_group('HR')
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')
    else:
        form = EmployeeForm()
    data = {
        'form': form
    }
    return render(request, 'account/employee-add.html', data)

@login_required
@is_group('HR')
def edit_employee(request, id):
    instance = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeEditForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('employees')
        else:
            print('Not Valid')
    else:
        form = EmployeeEditForm(instance=instance)

    data = {
        'employee' : instance,
        'form' : form
    }
    return render(request, 'account/employee-edit.html', data)

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



