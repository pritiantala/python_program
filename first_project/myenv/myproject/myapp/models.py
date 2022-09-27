import email
from itertools import product
from tkinter import CASCADE
from turtle import title
from venv import create
from django.db import models

# Create your models here.
gender_choice=[
    ('Male','Male'),
    ('Female','Female'),
]
class User(models.Model):
    email=models.EmailField(unique=True,max_length=30)
    password=models.CharField(max_length=30)
    role=models.CharField(max_length=30)
    is_verify=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

class Shopkeeper(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30,blank=True,null=True)
    shop_name=models.CharField(max_length=30)
    contact_number=models.CharField(max_length=30)
    address=models.TextField(max_length=200,blank=True,null=True)

class Customer(models.Model):
    customer_id=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30,blank=True,null=True)
    contact_number=models.CharField(max_length=30)
    gender=models.CharField(max_length=30,choices=gender_choice)
    dob=models.DateField(auto_now_add=False,blank=True,null=True)
    address=models.TextField(max_length=200)

class RAMSpecification(models.Model):
    ram_size=models.CharField(max_length=30)

class Products(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    shopkeeper_id=models.ForeignKey(Shopkeeper,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=30)
    product_description=models.TextField(max_length=250)
    product_price=models.CharField(max_length=30)
    qty=models.CharField(max_length=30)
    s_id=models.ForeignKey(RAMSpecification,on_delete=models.CASCADE,null=True)
    pic=models.FileField(upload_to='media/images/',default='media/product_default.png')

class Offers(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Shopkeeper_id=models.ForeignKey(Shopkeeper,on_delete=models.CASCADE)
    pic=models.FileField(upload_to='media/images/',default='media/product_default.png')
    title=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.title

class MyCart(models.Model):
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    Shopkeeper_id=models.ForeignKey(Shopkeeper,on_delete=models.CASCADE)
    my_qty=models.CharField(max_length=30)
    total_price=models.CharField(max_length=30)
    status=models.CharField(max_length=80,default="PENDING")
    order_accept_status=models.CharField(max_length=80,default="PENDING")
    order_placed_status=models.CharField(max_length=80,default="PENDING")
    created_at=models.DateTimeField(auto_now_add=True)
    address=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.customer_id.firstname+ "-"+ self.product_id.product_name
