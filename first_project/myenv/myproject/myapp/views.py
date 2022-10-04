from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import random
from django.core.mail import send_mail
# Create your views here.
"""
insert data in database
var=Modelname.objects.create(fildname=pythonvar,fildname=pythonvar....)
-------------------------------
retrive data from database----it will return object 

var=modelname.objects.get(fildname=value)

2nd method we can retrive data using of filter()---it will return queryset()

data=modelname.objects.filter(fieldname=value)
"""

def signup(request):
    if request.POST:
        firstname=request.POST['firstname']
        pemail=request.POST['email']
        contact=request.POST['contact'] 
        role=request.POST['role']

        print("firstname",firstname)
        print("--> submit button clicked")

        l1=["aw33","dfreger4","dfe4454","thyt66","hyjyu6","thrt3","fdgrt53","fhyju6"]
        password=random.choice(l1)+firstname[:3]+pemail[3:6]


        uid= User.objects.create(email = pemail,password = password,role=role)
        if uid:
            send_mail("Confirmation Mail","Your Password is"+str(password),"pritiantala209@gmail.com",[pemail])
            if uid.role=="Shokeeper":
                sid= Shopkeeper.objects.create(user_id = uid,firstname = firstname,contact_number=contact)
                smsg="Successfully register"
                context={
                    "smsg": smsg
                }
                
                return render(request,"myapp/register.html",context)
            elif uid.role=="Customer":
                cid=Customer.objects.create(customer_id=uid,firstname=firstname,contact_number=contact)
                smsg="Successfully register"
                context={
                    "smsg": smsg
                }
                
                return render(request,"myapp/register.html",context)
        else:
            emsg="Something Went Wrong"
            context={
                "emsg": emsg
            }
            
            return render(request,"myapp/register.html",context)

    else:
        print("--> page just refresh")
        return render(request,"myapp/register.html")

def login(request):
    if request.POST:
        email=request.POST['email']
        password=request.POST['password']

        uid=User.objects.get(email=email)
        if uid.password==password:
            print("valid user")
            if uid.role=="Shopkeeper":
                sid=Shopkeeper.objects.get(user_id=uid)
                print("usename",sid.firstname)
                if uid.is_verify:
                    print("-----INDEX SHOPKEEPER")
                    context={
                        'uid': uid,
                        'sid': sid,
                    }
                    request.session['email']=email
                    return render(request,"myapp/s_index.html",context)
                else:
                    context={
                        'email':email,
                    }

                    return render(request,"myapp/change_password.html",context)
            elif uid.role=="Customer":
                
                cid=Customer.objects.get(customer_id=uid)
                print("username=",cid.firstname)
                if uid.is_verify:
                    print("--------INDEX CUSTOMER")
                    context={
                        'uid':uid,
                        'cid':cid,
                    }
                    request.session['email']=email
                    all_products=Products.objects.all()
                    offers=Offers.objects.all()
                    context={
                        'uid':uid,
                        'cid':cid,
                        'offers':offers,
                        'all_products':all_products,
                    }
                    return redirect('c_home')
                else:
                    context={
                        'email':email,
                    }
                    return render(request,"myapp/change_password.html",context)
        else:
            return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")

def change_password(request):
    if request.POST:
        email=request.POST['email']
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        retypepassword=request.POST['confirmpassword']
        
        uid=User.objects.get(email=email)
        if uid.password==oldpassword and newpassword==retypepassword:
            uid.password=newpassword
            uid.is_verify=True
            uid.save()  #update query
            
            context={
                'smsg':"successfully password updated !!"
            }
            return render(request,"myapp/login.html",context)
        else:
            context={
                'emsg':"invalid password !!"
            }
            return render(request,"myapp/login.html",context)

    else:
        return render(request,"myapp/change_password.html")
        
def home(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=='Shopkeeper':
            sid=Shopkeeper.objects.get(user_id=uid)
            context={
                        'uid': uid,
                        'sid': sid,
                    }
            return render(request,"myapp/s_index.html",context)
        elif uid.role=="Customer":
            cid=Customer.objects.get(customer_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request,"customerApp/c_index.html",context)   
    else:
        return render(request,"myapp/login.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
        return redirect('login')
    else:
        return redirect('login')

def add_products(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Shopkeeper":
            sid=Shopkeeper.objects.get(user_id=uid)
            if request.POST:
                spid=RAMSpecification.objects.get(ram_size=request.POST['spec_value'])
                pid=Products.objects.create(user_id=uid,shopkeeper_id=sid,product_name=request.POST['product_name'],product_price=request.POST['product_price'],product_description=request.POST['product_description'],s_id=spid,qty=request.POST['qty'],)
                if "pic" in request.FILES:
                    pid.pic=request.FILES['pic']
                    pid.save()
                context={
                    'uid':uid,
                    'sid':sid,
                }
                return render(request,"myapp/add-products.html",context)
            else:
                spec =RAMSpecification.objects.all()
                context={
                    'uid':uid,
                    'sid':sid,
                    'spec':spec,
                }
                return render(request,"myapp/add-products.html",context)
        else:
            return redirect('login')


def my_products(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        sid=Shopkeeper.objects.get(user_id=uid)
        all_products=Products.objects.filter(shopkeeper_id=sid)
        context={
            'uid':uid,
            'sid':sid,
            'all_products':all_products
        }

        return render(request,"myapp/my_products.html",context)

def view_customer(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        sid=Shopkeeper.objects.get(user_id=uid)
        all_customer=ProceedProduct.objects.filter(Shopkeeper_id=sid)
        context={
            'uid':uid,
            'sid':sid,
            'all_customer':all_customer,
        }

        return render(request,"myapp/customer.html",context)