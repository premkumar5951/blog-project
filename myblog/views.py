from django.shortcuts import render
from django.http import HttpResponse
from .models import blogpost
# Create your views here.
def blogHome(request):
   blog=blogpost.objects.all()

   return render(request,'blog/blogHome.html',{'blog':blog})

def blogPost(request,slug):
      blogp=blogpost.objects.filter(sno=slug[-1:])
      return render(request,'blog/blogPost.html',{"blogp":blogp[0]})


