from django.db import models


# Create your models here.
class Grow_From(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    employee_name = models.CharField(max_length=255, blank=True, null=True)
    employee_id = models.CharField(max_length=25, blank=True, null=True)
    employee_email = models.CharField(max_length=25, blank=True, null=True)
    shift = models.CharField(max_length=255, blank=True, null=True)
    division = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    line = models.CharField(max_length=25, blank=True, null=True)
    station = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    current_description = models.CharField(max_length=500, blank=True, null=True)
    idea_description = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
