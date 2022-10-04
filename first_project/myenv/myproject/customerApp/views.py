import imp
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from myapp.models import *
# Create your views here.
def c_home(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Customer":
            cid=Customer.objects.get(customer_id=uid)
            all_products=Products.objects.all()
            offers=Offers.objects.all()
            context={
                'uid':uid,
                'cid':cid,
                'all_products':all_products,
                'offers':offers,
            }
            return  render(request,"customerApp/c_index.html ",context)
    else:
        all_products=Products.objects.all()
        offers=Offers.objects.all()
        context={
            'all_products':all_products,
            'offers':offers,
        }
        return  render(request,"customerApp/c_index.html ",context)

def my_cart(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Customer":
            cid=Customer.objects.get(customer_id=uid)
            all_products=Products.objects.all()
            offers=Offers.objects.all()
            myall_product=MyCart.objects.filter(customer_id=cid,status="PENDING")
            total_price=0

            for i in myall_product:
                print("-------->",i.total_price)
                total_price += int(i.total_price)
            
            context={
                'uid':uid,
                'cid':cid,
                'all_products':all_products,
                'offers':offers,
                'myall_product':myall_product,
                'total_price':total_price,
            }
            return  render(request,"customerApp/shopping-cart.html ",context)

def selected_product(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Customer":
            cid=Customer.objects.get(customer_id=uid) #customer id
            all_products=Products.objects.all()
            offers=Offers.objects.all()

            pid=Products.objects.get(id=pk) #product id
            sid=Shopkeeper.objects.get(id=pid.shopkeeper_id.id) #shopkeeper id
            my_qty=1
            total_price=pid.product_price

            mycart=MyCart.objects.create(customer_id=cid,product_id=pid,Shopkeeper_id=sid,my_qty=my_qty,total_price=total_price,)
            myall_product=MyCart.objects.filter(customer_id=cid,status="PENDING")
            context={
                'uid':uid,
                'cid':cid,
                'all_products':all_products,
                'offers':offers,
                'myall_product':myall_product,
            }
            return  redirect('my-cart')


def delete_product(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Customer":
            cid=Customer.objects.get(customer_id=uid) #customer id
            all_products=Products.objects.all()
            offers=Offers.objects.all()
            print("----> pk = ",pk)
            pid=MyCart.objects.get(id=pk)
            print("---> all products from table ",pid)
            pid.delete()  # delete query - it will remove product from the table 
            return  redirect('my-cart')

def plus_product(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Customer":
            cid=Customer.objects.get(customer_id=uid) #customer id
            print("------>inside the python product changes",request.POST['id'])
            mid= MyCart.objects.get(id=request.POST['id'])
            print("--->product name:",mid.product_id.product_name)
            print("--->product qty=",mid.my_qty)
            product_price=mid.product_id.product_price
            real_price=product_price.replace(",","")
            print("----->product price for 1:",mid.product_id.product_price)
            print("---> real price:",real_price)

            new_qty= int(mid.my_qty) + 1
            new_price=new_qty * int(real_price)

            mid.my_qty = new_qty
            mid.total_price = new_price
            mid.save()
            myall_product=MyCart.objects.filter(customer_id=cid,status="PENDING")
            total_price=0

            for i in myall_product:
                total_price += int(i.total_price)
            
            print("------>myall product",myall_product)
            print("---->total price=",total_price)
            context={
                'qty':new_qty,
                'price':new_price,
                'total_price':total_price,
            }
            return JsonResponse({'context':context})

def minus_product(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Customer":
            cid=Customer.objects.get(customer_id=uid) #customer id
            print("------>inside the python product changes",request.POST['id'])
            mid= MyCart.objects.get(id=request.POST['id'])
            print("--->product name:",mid.product_id.product_name)
            print("--->product qty=",mid.my_qty)
            product_price=mid.product_id.product_price
            real_price=product_price.replace(",","")
            print("----->product price for 1:",mid.product_id.product_price)
            print("---> real price:",real_price)

            if int(mid.my_qty)==1:
                print("------------qty 1-----------")
                myall_product=MyCart.objects.filter(customer_id=cid,status="PENDING")
                total_price=0

                for i in myall_product:
                    total_price = int(i.total_price)
                context={
                    'qty':int(mid.my_qty),
                    'price':int(mid.total_price),
                }
                return JsonResponse({'context':context})
            else:
                new_qty= int(mid.my_qty) - 1
                new_price=new_qty * int(real_price)

                mid.my_qty = new_qty
                mid.total_price = new_price
                mid.save()
                myall_product=MyCart.objects.filter(customer_id=cid,status="PENDING")
                total_price=0

                for i in myall_product:
                    total_price += int(i.total_price)
                print("------>myall product",myall_product)
                print("---->total price=",total_price)
                context={
                    'qty':new_qty,
                    'price':new_price,
                    'total_price':total_price,
                }
                return JsonResponse({'context':context})

def coupon(request):
    coupon=request.POST['coupon']
    total_price=request.POST['total_price']
    discount =2999
    net_price= int(total_price)-discount
    print("--->coupon code:",request.POST['coupon'])

    context={
        'discount':discount,
        'net_price':net_price,
        'total_price':total_price,
    }
    return JsonResponse({'context':context})

def proceed_checkout(request):
     if "email" in request.session:
        print("------>proceed to checkout",request.POST['total_price_field'])
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Customer":
            cid=Customer.objects.get(customer_id=uid)
            all_products=Products.objects.all()
            offers=Offers.objects.all()
            myall_product=MyCart.objects.filter(customer_id=cid,status="PENDING")
            total_price=0

            for i in myall_product:
                print("----->product name:",i.product_id.product_name)
                total_price += int(i.total_price)
                proceed_checkout_id=ProceedProduct.objects.create(customer_id=i.customer_id,product_id=i.product_id,Shopkeeper_id=i.Shopkeeper_id,my_qty=i.my_qty,total_price=i.total_price,order_net_amount=total_price)
                
            context={
                'uid':uid,
                'cid':cid,
                'all_products':all_products,
                'offers':offers,
                'myall_product':myall_product,
                'total_price':total_price,
            }

            for i in myall_product:
                myall_product=MyCart.objects.filter(customer_id=cid,status="PENDING")
                myall_product.delete()

          
            return  render(request,"customerApp/c_index.html ",context)
