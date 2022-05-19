from django.shortcuts import render, redirect
import string
from app1.models import Contacts

PC = set(string.punctuation)


# Create your views here.
def index(request):
    return render(request, 'app1/index.html')


def meth(request):
    return render(request, 'app1/methadology.html')


def contact(request):
    if request.method == "GET":
        contact = Contacts.objects.all()
        return render(request, 'app1/contact.html')

    elif request.method == "POST":
        f_name = request.POST["c_fname"]
        l_name = request.POST["c_lname"]
        email = request.POST["c_email"]
        subject = request.POST["c_subject"]
        message = request.POST["c_message"]

        Contacts.objects.create(
            fast_name=f_name,
            last_name=l_name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect('/')


def about(request):
    return render(request, 'app1/about.html')


def form(request):
    if request.method == "GET":
        return render(request, 'app1/regstrationForm.html')
    if request.method == "POST":
        password = request.POST['pass']
        if len(password) <= 8:
            context = {
                "message": 'Please Input at least 8 character'
            }
            return render(request, 'app1/rufdata.html', context)
        elif password == password.lower():
            context = {
                "message": 'You Need to input one lowercase letter'
            }
            return render(request, 'app1/rufdata.html', context)
        elif password == password.upper():
            context = {
                "message": 'You Need to input one upper case letter'
            }
            return render(request, 'app1/rufdata.html', context)
        elif password[0].isnumeric():
            context = {
                "message": 'You can not input number at first'
            }
            return render(request, 'app1/rufdata.html', context)
        elif not any(_ in PC for _ in password):

            context = {
                "message": 'You have to input a special character'
            }
            return render(request, 'app1/rufdata.html', context)
        else:
            context = {
                "message": 'Done',
                "password": password
            }
            return render(request, 'app1/rufdata.html', context)
