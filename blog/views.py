from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .models import post
from .forms import PostForm

# Create your views here.
def home(request):
    
    return render(request,'blog/home.html')
def about(request):
    return render(request,'blog/about.html')  
def contact(request):
    return render(request,'blog/contact.html')    
def user_signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            messages.success(request,"you have successfully register !!!!")
            form.save()
        
    else:
        form=SignupForm()
    return render(request,'blog/signup.html',{'form':form}) 
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"successfully login!!")
                    request.session['name']=uname
                    return HttpResponseRedirect('/dashboard/')
                    form=LoginForm()
        else:            
            form=LoginForm()
        return render(request,'blog/login.html',{'form':form}) 
    else:
        return HttpResponseRedirect('/dashboard/')       

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')  
def dashboard(request):
    if request.user.is_authenticated:
        posts=post.objects.all()
        
        return render(request,'blog/dashboard.html',{'post':posts})
    else:
        return HttpResponseRedirect('/login/')
         
def user_post(request):
    posts=post.objects.all()
    return render(request,'blog/post.html',{'post':posts})
def addpost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=PostForm(request.POST)
            if form.is_valid():
                utitle=form.cleaned_data['title']
                udesc=form.cleaned_data['desc']
                pst=post(title=utitle,desc=udesc)
                messages.success(request,'post added successfully !')
                pst.save()
                form=PostForm()
        else:
            form=PostForm()
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return  HttpResponseRedirect('/login/')    

def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request,'update successfully !')
                return HttpResponseRedirect('/dashboard/')
        else:
            pi=post.objects.get(pk=id) 
            form=PostForm(instance=pi)       
        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return  HttpResponseRedirect('/login/')    

def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=post.objects.get(pk=id)
            pi.delete()
            messages.success(request,'delete successfully !!')
            return HttpResponseRedirect('/dashboard/')
        
    else:
        return  HttpResponseRedirect('/login/')    