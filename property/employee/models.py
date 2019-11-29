from django.db import models
class EmployeeDetails(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_mail = models.EmailField()
    emp_location = models.CharField(max_length=100)
    emp_doj = models.CharField(max_length=100)
    emp_role = models.CharField(max_length=100)
    emp_qualificatiov = models.CharField(max_length=100)
    emp_remarks = models.CharField(max_length=100)
