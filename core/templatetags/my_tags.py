from django import template
from account.models import Employee
from hr.models import *
from datetime import datetime

register = template.Library()

@register.filter(name='fullname')
def full_name(id):
    employee = Employee.objects.get(id=id)
    return f"{employee.first_name} {employee.last_name}"

@register.filter(name='avatar')
def avatar(id):
    employee = Employee.objects.get(id=id)
    return f"/uploads/{employee.image}"
    

@register.filter(name='workstatus')
def working_status(value):
    if value == 'WK':
        return f'<span class="badge text-primary-100 bg-primary-10">Working</span>'
    elif value == 'AV':
        return f'<span class="badge text-success-100 bg-success-10">Available</span>'
    elif value == 'BK':
        return f'<span class="badge text-warning-100 bg-warning-10">Booked</span>'
    elif value == 'AS':
        return f'<span class="badge text-info-100 bg-info-10">In Assist</span>'
    elif value == 'AB':
        return f'<span class="badge text-danger-100 bg-danger-10">Absent</span>'
    

@register.filter(name='has_group')
def has_group(user, group):
    return user.groups.filter(name=group).exists()

@register.filter(name='holiday_duration')
def holiday_duration(id):
    holiday = Holiday.objects.get(id=id)
    day1 = datetime(holiday.start_date.year, holiday.start_date.month, holiday.start_date.day)
    day2 = datetime(holiday.end_date.year, holiday.end_date.month, holiday.end_date.day)
    return (day2-day1).days if (day2-day1).days > 0 else 1