from django.shortcuts import render
from .models import User, details
import random


def home(request):  # redirects to main page
    request.session['usr'] = ''
    return render(request, 'index.html')


def gallery(request):  # redirects to gallery
    return render(request, 'gallery.html', {'usr': request.session['usr']})


def about(request):  # redirects to about
    return render(request, 'about.html', {'usr': request.session['usr']})


def login(request):  # redirects to login
    if request.method == 'POST':
        username = request.POST['username']  # retrieve's data from the form
        pwd = request.POST['pwd']
        if User.objects.filter(username=username).exists():
            a = User.objects.get(username=username)  # if username is present checks if password is same
            if pwd == a.password:
                request.session['usr'] = username  # creates session storage with key as 'usr' and username as its value
                return render(request, 'index.html',
                              {'msg': username + 'login successful', 'usr': request.session['usr']})
            else:  # if password is wrong
                return render(request, 'log.html', {'pwd_err': 'Wrong Password!'})
        else:  # if username is not found
            return render(request, 'log.html', {'usr_err': 'Username not found!'})
    else:
        return render(request, 'log.html')


def signin(request):
    if request.method == 'POST':
        name = request.POST['name']  # retrieve's data from the form
        username = request.POST['username']
        email = request.POST['your_email']
        pwd = request.POST['password']
        cnfrm = request.POST['confirm']
        if User.objects.filter(username=username).exists():  # if username is taken
            return render(request, 'signin.html', {'usr_err': 'Username already exists!!', 'name': name})
        elif User.objects.filter(email=email).exists():  # if email is already found
            return render(request, 'signin.html',
                          {'email_err': 'Email id already exits!!!', 'username': username, 'name': name})
        elif pwd != cnfrm:  # if password and confirm password doesn't match
            return render(request, 'signin.html',
                          {'pwd_err': 'passwords doesnt match', 'username': username, 'email': email, 'name': name})
        else:  # if every thing is correct
            User.objects.create(name=name, username=username, email=email,
                                password=pwd)  # creates a record in model user
            return render(request, 'log.html', {'username': username, 'msg': 'Registered successfully'})
    else:
        return render(request, 'signin.html')


def sat_det(request):
    return render(request, 'sputnik.html')


def detail(request):
    i = request.POST['search']  # collects name from the search
    try:
        a = details.objects.get(Name=i)  # retrieves data from the database with matching name
    except details.DoesNotExist:
        return render(request, 'details.html',
                      {'a': '', 'usr': request.session['usr']})  # send empty object if not found
    return render(request, 'details.html', {'a': a, 'usr': request.session['usr']})  # send satellites record


def link(request, name):
    a = details.objects.get(Name=name)
    return render(request, 'details.html', {'a': a, 'i': name, 'usr': request.session['usr']})


def category(request, i):  # gets orbit type form category dropdown
    a = [details.objects.filter(orbit_type=i)]  # filters records with same orbit type
    name = {}
    first = []
    for x in a:  # x contains all the records of that particular orbit type
        for y in x:  # iterates through x and y contains details of particular satellite
            if y.Name[0] not in first:  # selects one satellite starting from each alphabet
                name[y.Name] = y.comments
                first.append(y.Name[0])

    new_name = {}

    if len(name.keys()) > 10:  # if name has more than ten objects selects 10 random object and stores in new_name
        for x in random.sample(name.keys(), 10):
            new_name[x] = name[x]
    else:
        new_name = name

    return render(request, 'category.html', {'value': new_name, 'i': i, 'usr': request.session['usr']})


def manage(request):  # gets 20 random records and displays on category.html
    a = [details.objects.all()]
    name = {}  # same as category function but gets all records
    first = []
    for x in a:
        for y in x:
            if y.Name[0] not in first:
                name[y.Name] = y.comments
                first.append(y.Name[0])

    new_name = {}
    for x in random.sample(name.keys(), 20):
        new_name[x] = name[x]

    return render(request, 'category.html', {'value': new_name, 'usr': request.session['usr']})


def logout(request):
    request.session['usr'] = ''  # sets session storage to empty
    return render(request, 'index.html')
