from django.db import models
from account.models import Employee
from datetime import datetime
# Create your models here.

class Holiday(models.Model):
    start_date = models.DateTimeField(unique=True)
    end_date = models.DateTimeField()
    title = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.start_date} - {self.end_date} - {self.title}'

    
class Leave(models.Model):
    LEAVE_CHOICES = ( 
        ("1", "Full Day"),
        ("2", "First Half"),
        ("3", "Second Half"),
        ("4", "Fullday with Second Half of Start Date"),
        ("5", "Fullday with First Half of End Date"),
    )
    type = models.CharField(max_length=1, choices=LEAVE_CHOICES)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    applied_date = models.DateField(default=datetime.now())
    reasone = models.CharField(max_length=500)
    manager_status = models.BooleanField(default=False)
    hr_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.employee} - {self.start_date}'

    class Meta:
        unique_together = ['start_date', 'employee']