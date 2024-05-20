from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from datetime import datetime
from django.contrib import messages
from .forms import *

# Create your views here.
def leaves(request):
    holidays = Holiday.objects.filter(start_date__year=datetime.now().year)
    leave_requests = Leave.objects.filter(employee__assigned_to=request.user, start_date__gt=datetime.today())
    leaves = Leave.objects.filter(employee=request.user)

    data = {
        'holidays' : holidays,
        'leave_requests' : leave_requests,
        'leaves' : leaves
    }
    return render(request, 'hr/leaves.html', data)

def apply_leave(request):
    if request.method == 'POST':
        form = LeaveApplyForm(request.POST)
        if form.is_valid():
           print('Valid')
        else:
           print('Not valid')
    else:
        form = LeaveApplyForm()
    
    data = {
        'form' : form
    }
    return render(request, 'hr/apply-leave.html', data)

def approve_leave_manager(request):
    id = request.POST.get('id')
    leave = Leave.objects.get(id=id)
    if leave.manager_status == False:
        leave.manager_status = True
        leave.save()
        return JsonResponse({'success': True, 'type': True})
    else:
        leave.manager_status = False
        leave.save()
        return JsonResponse({'success': True, 'type': False})


def delete_leave(request):
    id = request.POST.get('id')
    leave = Leave.objects.get(id=id)
    leave.delete()
    return redirect('leaves')