from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Categorgy,Product

# Create your views here.



def index(request):
    return render( request,'index.html')
@login_required(login_url='log')


def productview(request):
    dict_prod={
        'product':Product.objects.filter(status=0)
    }
    
    return render(request,'productview.html',dict_prod)


# def productin(request,slug):
#      if(Categorgy.objects.filter(slug=slug,status=0)): 
#            products=Product.objects.filter(slug=slug)
#            categorgy_name=Categorgy.objects.fliter(slug=slug).frist()
#            context={'categorgy':categorgy}
#            return render(request,"productview.htnl",context)
 
#      else:
      
        #   return redirect('home')



def productin(request, slug=None):
    if slug:
        try:
            product = Product.objects.get(slug=slug)
            context = {'product': product}
            return render(request, "productview.html", context)
        except Product.DoesNotExist:
            # Handle the case where the product with the given slug doesn't exist
            return HttpResponse("Product not found", status=404)
    else:
        # Handle the case where slug is missing or not provided
        return HttpResponse("Slug parameter is missing or incorrect", status=400)


def payment(request):
     dict_pay={
         'pay':Product.objects.all()
     }
     return render( request,'payment.html',dict_pay)


              

def log(request):
    if request.method=="POST":
      username=request.POST['username']
      password=request.POST['password']
      user=auth.authenticate(username=username ,password=password)
      if user is not None:
            auth.login(request,user)
            return redirect('/')
      else:
            messages.info(request,"invaild login")
            return redirect("log")
    return render( request,'log.html')



def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"username already exists")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email taken")
            return redirect('register')
        else:   
         user=User.objects.create_user(username=username,email=email,password=password)
         user.save();
         return redirect('/')
    
    else:
     return render( request,'register.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')

def contact(request):
     return render( request,'contact.html')


def blog(request):
     return render( request,'blog_list.html')



   



   



# def productview(request,cate_slug,prod_slug):
#     if(Categorgy.objects.filter(slug=cate_slug,status=0)):
#         if(Product.objects.filter(slug=prod_slug,status=0)):
#             prod=Product.objects.filter(slug=prod_slug,status=0)
    
#         else:
#             messages.error(request,"no such product found ")
#             return redirect('collection')
    
# #     else:
#          messages.error(request,"no such category found ")
#          return redirect('collection')
#     return render(request,"productview.html",{"prod":prod})



