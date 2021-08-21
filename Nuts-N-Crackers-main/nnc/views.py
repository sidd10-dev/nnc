from django.shortcuts import get_object_or_404, render, redirect
from django.template.defaultfilters import register
from django.views.generic import TemplateView
from django.utils import timezone
from .models import *
from accounts.models import customer


def home(request):
    context = {}

    context['categories'] = Category.objects.all

    return render(request,'home.html',context)

def productpage(request,slug):
    context = {}

    category = get_object_or_404(Category,slug = slug)
    cp = CategoryProduct.objects.filter(category = category)

    context['products'] = cp
    context['categories'] = Category.objects.all()

    return render(request, 'Products.html', context)

def allproductpage(request):
    context = {}

    context['categories'] = Category.objects.all()

    context['products'] = CategoryProduct.objects.all()


    return render(request,'allproducts.html',context)

def cart(request):
    context = {}

    user = request.user
    order = Order.objects.filter(user = user,complete = False)
    if order.exists():

        order = order[0]
        orderproduct = OrderProduct.objects.filter(order = order)
        total = 0

        for op in orderproduct:
            amount = op.calcprice()
            total = total + amount

        order.total = total
        order.save()

        context['total'] = total
        context['orderproduct'] = orderproduct
        context["count"] = OrderProduct.objects.filter(order = order).count()

    else:
        context["count"] = 0

    return render(request,'Cart.html',context)

def checkout(request):

    order = Order.objects.get(user = request.user,complete = False)
    order.number_of_items = OrderProduct.objects.filter(order = order).count()
    order.date_ordered = timezone.now()
    order.complete = True
    order.save()

    return render(request,'Recieved.html',{})

def orders(request):

    context = {}
    user = request.user

    order_list = Order.objects.filter(user = user,complete = True)
    context['orders'] = order_list

    return render(request,'previous.html',context)

def order_detail(request,pk):

    context = {}
    order = Order.objects.get(pk=pk)

    context['order'] = order

    orderproducts = OrderProduct.objects.filter(order = order)

    context['orderproducts'] = orderproducts
    
    return render(request, 'cartitemreview.html',context)

def delivery_page(request):

    context = {}
    order = Order.objects.filter(delivered = False)

    context['orders'] = order

    return render(request,'Deliveries.html',context)

def delivery_detail(request,pk):

    context = {}
    order = get_object_or_404(Order,pk=pk)
    orderproducts = OrderProduct.objects.filter(order = order)

    context['order'] = order
    context['orderproducts'] = orderproducts

    return render(request,'Deliveryitem.html', context)


# FUNCTIONALITIES
def addtocart(request,pk):

    product = get_object_or_404(CategoryProduct,pk=pk)
    order_list = Order.objects.filter(user = request.user, complete = False)
    
    if order_list.exists():
        order = order_list[0]
        orderproduct = OrderProduct.objects.filter(product = product, order = order)

        if orderproduct.exists():
            orderproduct = OrderProduct.objects.get(order = order,product = product)
            orderproduct.quantity = orderproduct.quantity + int(request.POST["quantity"])
            orderproduct.save()
            return redirect('nnc:product',slug = product.category.slug)
        
        else:
            orderproduct = OrderProduct.objects.create(order = order, product = product)
            orderproduct.quantity = request.POST["quantity"]
            orderproduct.save()
            return redirect('nnc:product',slug = product.category.slug)

    else:
        cust = customer.objects.get(user = request.user)
        order = Order.objects.create(user = request.user, customer = cust)
        orderproduct = OrderProduct.objects.create(order = order,product = product,quantity = request.POST["quantity"])
        return redirect('nnc:product',slug = product.category.slug)

def addtocartt(request,pk,quantity):

    product = get_object_or_404(CategoryProduct,pk=pk)
    order_list = Order.objects.filter(user = request.user, complete = False)
    
    if order_list.exists():
        order = order_list[0]
        orderproduct = OrderProduct.objects.filter(product = product, order = order)

        if orderproduct.exists():
            orderproduct = OrderProduct.objects.get(order = order,product = product)
            orderproduct.quantity = orderproduct.quantity + int(quantity)
            orderproduct.save()
            return redirect('nnc:product',slug = product.category.slug)
        
        else:
            orderproduct = OrderProduct.objects.create(order = order, product = product)
            orderproduct.quantity = quantity
            orderproduct.save()
            return redirect('nnc:product',slug = product.category.slug)

    else:
        cust = customer.objects.get(user = request.user)
        order = Order.objects.create(user = request.user, customer = cust)
        orderproduct = OrderProduct.objects.create(order = order,product = product,quantity = quantity)
        return redirect('nnc:cart')

def increaseqty(request,pk):

    orderproduct = get_object_or_404(OrderProduct,pk=pk)
    orderproduct.quantity += 1
    orderproduct.save()

    return redirect('nnc:cart')

def decreaseqty(request,pk):

    orderproduct = get_object_or_404(OrderProduct,pk=pk)
    if orderproduct.quantity == 1:
        return redirect('nnc:remove',pk=pk)
    else:
        orderproduct.quantity -= 1
        orderproduct.save()

    return redirect('nnc:cart')

def remove(request,pk):

    orderproduct = get_object_or_404(OrderProduct,pk=pk)
    orderproduct.delete()

    return redirect('nnc:cart')

def set_delivered(request,pk):

    order = get_object_or_404(Order,pk=pk)
    order.delivered = True
    order.save()
    
    return redirect('nnc:delivery')




        





