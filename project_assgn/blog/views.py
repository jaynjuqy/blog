from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms, models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.urls import reverse

# Create your views here.
def register(request):
    if request.method=='POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/')
    else:
        form = forms.UserRegistrationForm()
    return render(request, 'register.html', {'reg_form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('myfeed')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def feed_view(request):
    posts = models.Post.objects.select_related('author').all().order_by('-pub_date')
    template = loader.get_template("feed.html")
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context,request))

def post_form(request):
    if request.method == "POST":
        form = forms.Posts(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save() 
            return redirect('myfeed')
    else:
        form = forms.Posts()
    template = loader.get_template("postform.html")
    return HttpResponse(template.render({'form':form}, request))

def post_details_veiw(request,id):
    post = models.Post.objects.get(id=id)
    comments = models.Comment.objects.select_related('author').filter(post=id)
    context = {
        'post' : post,
        'comments': comments,
    }
    template = loader.get_template("postdetails.html")
    return HttpResponse(template.render(context, request))

def comment_form(request, id):
    post = models.Post.objects.get(id=id)
    if request.method == "POST":
        form = forms.Comments(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('myfeed')
    else:
        form = forms.Comments()
    template = loader.get_template("comment.html")
    return HttpResponse(template.render({'form':form, 'post':post}, request))