from django.db import models
from django.forms import ValidationError

class Workers(models.Model):
    EMPLOYEE_ID = models.IntegerField(primary_key=True)
    IMAGE = models.ImageField(upload_to='media/', null=True, blank=True)
    FIRST_NAME = models.CharField(max_length=50)
    LAST_NAME = models.CharField(max_length=50)
    EMAIL = models.EmailField(max_length=254)
    PHONE_NUMBER = models.CharField(max_length=20)
    HIRE_DATE = models.DateField()
    JOB_ID = models.CharField(max_length=10)
    SALARY = models.DecimalField(max_digits=8, decimal_places=2)
    COMMISSION_PCT = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=True)
    DEPARTMENT_ID = models.IntegerField()
    MANAGER = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='employees')

    def clean(self):
        # Ensure that the manager_id is not the same as the employee_id
        if self.MANAGER == self.EMPLOYEE_ID:
            raise ValidationError('A worker cannot be their own manager')
    
    def __str__(self) -> str:
        return self.FIRST_NAME


class Job(models.Model):
    title = models.CharField(max_length=100)
    workers = models.ManyToManyField(Workers, related_name='jobs')

    def __str__(self):
        return self.title


class Paradigm(models.Model):
    name = models.CharField(max_length=100)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='paradigms')

    def __str__(self):
        return self.name

