from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login

def home_page(request):
	context={
	"title" :"Home Page"
	}
	if request.user.is_authenticated():
		context['premium']='Yeaaaaaaaa'
	return render(request,"home_page.html",context)

def about_page(request):
	context={
	"title" :"about Page"
	}
	return render(request,"home_page.html",context)

def contact_page(request):
	contact_form= ContactForm(request.POST or None)
	context={
	"title" :"contact Page",
	"form" : contact_form
	}
	print(request.POST)
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	# if request.method== "POST":
	# 	print('Inside contact Page')
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('content'))
	return render(request,"home_page.html",context)

def login_page(request):
	login_class=LoginForm(request.POST or None)
	context = {
		"title": "contact Page",
		"form": login_class
	}
	print(request.user.is_authenticated)
	if login_class.is_valid():
		print(login_class.cleaned_data)

		username=login_class.cleaned_data.get("username")
		password = login_class.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)

		if user is not None:
			#print(request.user.is_authenticated)
			print(user)
			login(request, user)
			# Redirect to a success page.
			#context["form"]=login_class
			return redirect('/')
		else:
			# Return an 'invalid login' error message.
		     print("Error")
	return render(request,"auth/login.html",context)

def register_page(request):
	register_class = RegisterForm(request.POST or None)
	context={
		"form":register_class
	}
	if register_class.is_valid():
		print(register_class.cleaned_data)
	return render(request,"auth/register.html",context)
