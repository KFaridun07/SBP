from django.db import models

# Create your models here.
from django.db import models
from accounts.models import CustomUser

class Courses(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)



class Modules(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE,related_name='modules')


class Task(models.Model):
    title = models.CharField(max_length=50)
    context = models.TextField()
    module = models.ForeignKey(Modules, on_delete=models.CASCADE,related_name="modules")


class TestCases(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE,related_name="taskcases")
    input = models.CharField(max_length=50)
    output = models.CharField(max_length=50)


class Subissions(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    code = models.TextField()
    status = models.CharField(max_length=50,default="pending")
    created_at = models.DateField( auto_now_add=True)
