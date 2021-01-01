from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Hiretuber
import re

# Create your views here.



def hiretuber(request):

    email_regex = "[\w\.-]+@[\w\.-]+\.\w{2,4}"

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email= request.POST['email']
        tubers_id = request.POST['tubers_id']
        tubers_name = request.POST['tubers_name']
        user_id = request.POST['user_id']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        message = request.POST['message']

        if (re.search(email_regex, email)):
            hiretuber = Hiretuber(first_name=first_name, last_name=last_name, email=email, tubers_id=tubers_id, tubers_name=tubers_name, user_id=user_id, city=city, state=state, phone=phone, message=message)
            hiretuber.save()
            messages.success(request, 'thanks for contacting us')
            return redirect('youtubers')


        else:
            messages.warning(request, 'please enter a valid email id')


