from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from. models import Contact
from django.contrib import messages
from myblog.models import blogpost
from django.contrib.auth.models import User
from .forms import formuser
import json
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout





# Create your views here.
def home(request):
     blog=blogpost.objects.all()
     length=len(blog)
     print(blog)
     return render(request,'home/home.html',{'blog':blog,"bloghome":blog[length-1]})
@login_required(login_url="/login/")
def about(request):
    return render(request,'home/about.html')

def contacts(request):
    if (request.method=="POST"):
        name=request.POST["name"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        textbox=request.POST["textbox"]
        
        if(len(name)>3 and len(phone)>5 and len(email)>5 and len(textbox)>10):
            contacts=Contact(name=name,phone=phone,email=email,textbox=textbox)
            contacts.save()
            messages.success(request,"The form has been submitted successfully!")
        else:
            messages.error(request,"Please fill up the form correctly!")

    return render(request,'home/contact.html')

def search(request):
    query=request.GET['search']

    if(len(query)>100):
        allsearch=blogpost.objects.none()
    else:
        allsearchtitle=blogpost.objects.filter(title__icontains=query)
        allsearchcontent=blogpost.objects.filter(content__icontains=query)
        allsearchauthor=blogpost.objects.filter(author__icontains=query)
        allsearch=allsearchtitle.union(allsearchcontent,allsearchauthor)
    if allsearch.count() == 0 or query=="":
        messages.warning(request,"No search result found.Please refine your query.")
    return render(request,'home/search.html',{"allsearch":allsearch,'query':query})


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.is_ajax() :
        data=json.load(request)
        value=data['post-data']
        str1=""
        if(len(value)>=5):
            str1='true'
        
        mydata={
            'mydata':str1
        }
        print(mydata)
        return JsonResponse(mydata)
    if request.method=="POST":
        print("ji")
        fm=formuser(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"You have been successfully registered. Please Login.")
            return render(request,"home/signup.html",{'form':fm}) 
    else:
        fm=formuser()

    return render(request,"home/signup.html",{'form':fm})


def loginform(request):
  if request.user.is_authenticated:
        return redirect('/')
  if request.method=="POST":
      forml=AuthenticationForm(request=request ,data=request.POST)
      if forml.is_valid():
         username=forml.cleaned_data['username']
         password=forml.cleaned_data['password']
         user=authenticate(username=username , password=password)
         if user is not None:
            login(request,user)
            messages.success(request,"You have been logged In. Keep Exploring!")
            return redirect("/")
  else:
      forml=AuthenticationForm()
    
  return render(request,"home/login.html",{'forml':forml})

@login_required(login_url="/login/")
def logmeout(request):
    logout(request)
    return redirect('/login/')

           