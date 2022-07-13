from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name  
class Dept(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Status(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Status_Staff(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Grade_Staff(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Grade_Student(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Category_Student(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    
    
    
      
class Book (models.Model):
    

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    photo_book = models.ImageField(upload_to='photo',null=True, blank=True)
    photo_author = models.ImageField(upload_to='photo',null=True, blank=True)  
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    stat = models.ForeignKey(Status, on_delete=models.PROTECT, null=True, blank=True)
    depart = models.ForeignKey(Dept, on_delete=models.PROTECT, null=True, blank=True)
    modarg = models.CharField(max_length=250,default='Place')
    thidate = models.DateTimeField (default=datetime.now)
    action = models.BooleanField(default=True)
    created_by = models.ForeignKey(User,related_name='book', on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField (auto_now_add=True,null=True, blank=True)
    def __str__(self):
        return self.author   
    
class Staff (models.Model):
    nat_id = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    photo_staff = models.ImageField(upload_to='photo',null=True, blank=True)
    email = models.CharField(max_length=250)
    status_staff = models.ForeignKey(Status_Staff, on_delete=models.PROTECT, null=True, blank=True)
    grade_staff = models.ForeignKey(Grade_Staff, on_delete=models.PROTECT, null=True, blank=True)
    depart = models.ForeignKey(Dept, on_delete=models.PROTECT, null=True, blank=True)
    date_of_hiring = models.DateTimeField (default=datetime.now)
    numb_of_research = models.CharField(max_length=250)
    action = models.BooleanField(default=True)
    created_by = models.ForeignKey(User,related_name='staff', on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField (auto_now_add=True,null=True, blank=True)
    def __str__(self):
        return self.name   
    
class Student (models.Model):
    nat_id = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    photo_student = models.ImageField(upload_to='photo',null=True, blank=True)
    email = models.CharField(max_length=250)
    category_student = models.ForeignKey(Category_Student, on_delete=models.PROTECT, null=True, blank=True)
    grade_student = models.ForeignKey(Grade_Student, on_delete=models.PROTECT, null=True, blank=True)
    date_of_hiring = models.DateTimeField (default=datetime.now)
    action = models.BooleanField(default=True)
    created_by = models.ForeignKey(User,related_name='student', on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField (auto_now_add=True,null=True, blank=True)
    def __str__(self):
        return self.name  