from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import DesignForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.views import View
from django.contrib.auth.hashers import make_password
from .models import *
# from django.htpp import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
##########################
from Card_App.models import Design
from math import ceil
import json

def person(request):
    print(request)
    if request.method == 'POST':
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        mob = request.POST.get('mob', '')
        password = request.POST.get('password', '')
        c_password = request.POST.get('c_password', '')
        person = Person(firstname=firstname, lastname=lastname, email=email, mob=mob,
                        password=password, c_password=c_password)
        person.save()
        return redirect('/log')
    else:
        return render(request, 'Card_App/signup.html')


def log(request):
    return render(request, 'Card_App/login.html')


def sign(request):
    if request.method == 'POST':
        if Person.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            person = Person.objects.get(email=request.POST['email'], password=request.POST['password'])
            person.save()
            return render(request, 'Card_App/signup.html', {'person': person})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'Card_App/login.html', context)


#############################################################################################


#def index(request):
 #   return render(request, 'Card_App/index.html', {'title': 'index'})


########### register here #####################################

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('Card_App/Email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('loginn')
    else:
        form = UserRegisterForm()
    return render(request, 'Card_App/register.html', {'form': form, 'title': 'reqister here'})


################ login forms###################################################

def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            context = login(request, user)
            context.save()
            messages.success(request, f' wecome {username} !!')
            return redirect('/index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    context = AuthenticationForm()
    return render(request, 'Card_App/index.html', {'context': context, 'title': 'log in'})


########################################################

def design(request):
    return render(request, "Card_App/template_designs.html")


def edit(request):
    return render(request, "Card_App/edit_profile.html")


def index(request):
    products = Design.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    return render(request, 'Card_App/index.html', params)


def mngcard(request):
    return render(request, "Card_App/managecard.html")


def new(request):
    products = Design.objects.all()
    print(products)
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    return render(request, 'Card_App/designView.html', params)


def selectedimg(request):
        if request.method == "POST":
            form = DesignForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/slected')
                except:
                    pass
        else:
            form = DesignForm()
        return render(request, 'Card_App/managcard.html', {'form': form})

##################################################################payment



