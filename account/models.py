from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import EmployeeManager
# Create your models here.

class Designation(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Employee(AbstractUser):
    STATUS_CHOICES = ( 
        ("WK", "Working"),
        ("AV", "Available"),
        ("BK", "Booked"),
        ("AS", "Assist"), 
        ("AB", "Absent"),
    ) 

    username = None
    groups = models.ManyToManyField('auth.Group', related_name='employee_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='employee_user_permissions', blank=True)
    email = models.EmailField(unique=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name='employee_designation', null=True, blank=True)
    phone = models.CharField(max_length=10, unique=True)
    emg_phone = models.CharField(max_length=10, null=True, blank=True, verbose_name='Emergency Phone Number')
    address = models.CharField(max_length=300, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    adhar = models.CharField(max_length=12, null=True, blank=True, verbose_name='Adhar Number')
    epf = models.CharField(max_length=12, null=True, blank=True, verbose_name='EPF UAN Number')
    esic = models.CharField(max_length=10, null=True, blank=True, verbose_name='ESIC ID')
    image = models.ImageField(upload_to='user/', default='')

    wrk_status = models.CharField(max_length=2, verbose_name='Working Status', choices=STATUS_CHOICES, default='WK')
    assigned_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', limit_choices_to={'groups__name': 'Manager'})
    booked_by = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='employee_booked_by', limit_choices_to={'groups__name': 'Manager'})


    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = [] 

    objects = EmployeeManager()

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if it's a new user
            self.set_password(self.password)
            self.email = self.email.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.designation}"
    
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"