import csv, io
from django.shortcuts import render
from django.contrib import messages

from student.models import Student
from trainer.models import Trainer
from .models import *

from RewardSystem.settings import EMAIL_HOST_USER
from django.core import mail
from django.core.mail import send_mail


def profile_upload(request):
    # declaring template
    template = "admin_dash.html"
    student_data = Student.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be username,email',
        'profiles': student_data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    student_data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(student_data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Student.objects.update_or_create(
        username=column[0],
        email=column[1],
    )

    # send the email to the recipent
    users=Student.objects.all()
    
    for user in users:
        user.role=User.STUDENT
        user.save()

        password = User.objects.make_random_password(length=10, 
                        allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')  
        
        user.password=password
        user.save()
        # user.set_password(password)
        # user.save(update_fields=['password'])
        emails=user.email
        # password=user.password

        subject = "Welcome To The AkiraChix Rewarding System"
        message = "Hi Welcome to Akirachix Choin.\nYour username is {} and password is {} \nVisit this link to Log In : https://choin.herokuapp.com/".format(emails,password)
        recipient=emails
        send_mail(subject, message,EMAIL_HOST_USER,[recipient])

    context = {}
    return render(request, template, context)

def trainer_profile_upload(request):
    # declaring template
    template = "trainer.html"
    trainer_data = Trainer.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be username,email',
        'profiles': trainer_data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    trainer_data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(trainer_data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Trainer.objects.update_or_create(
        username=column[0],
        email=column[1],
    )

    # send the email to the recipent
    users=Trainer.objects.all()
    
    for user in users:
        user.role=User.TRAINER
        user.save()
        
        password = User.objects.make_random_password(length=10, 
                        allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')  
        user.password=password
        user.save()
        # user.set_password(password)
        # user.save(update_fields=['password'])
        emails=user.email
        subject = "Welcome To The AkiraChix Rewarding System"
        message = "Hi Welcome to Akirachix Choin.\nYour username is {} and password is {}. Your role is {} \nVisit this link to Log In : https://choin.herokuapp.com/".format(emails,password,user.role)
        recipient=emails
        send_mail(subject, message,EMAIL_HOST_USER,[recipient])

    context = {}
    return render(request, template, context)


def reward(request):
    return render(request,'reward.html')

def reward_confirm(request):
    metrics = Metrics.objects.all()
    return render(request,'reward_confirm.html',{'metrics':metrics})