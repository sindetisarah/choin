import csv, io
from django.shortcuts import render
from django.contrib import messages
from .models import *

from RewardSystem.settings import EMAIL_HOST_USER
from django.core import mail
from django.core.mail import send_mail

# Create your views here.


#send mails




# one parameter named request
def profile_upload(request):
    # declaring template
    template = "admin_dash.html"
    data = User.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be username,email',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = User.objects.update_or_create(
        username=column[0],
        email=column[1],
    )

    # send the email to the recipent
    users=User.objects.all()
    
    for user in users:
        
        password = User.objects.make_random_password(length=10, 
                        allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')        
        user.set_password(password)
        user.save(update_fields=['password'])
        emails=user.email
        # password=user.password

        subject = "Welcome To The AKiraChix Rewarding System"
        message = "Hi Welcome to akirachix Choin. Your password is {}".format(password)
        recipient=emails
        send_mail(subject, message,EMAIL_HOST_USER,[recipient])

    context = {}

    
    

  
    

    return render(request, template, context)