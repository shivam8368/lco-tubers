from django.shortcuts import redirect, render
from .models import Contact
from django.contrib import messages

# Create your views here.


def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        company = request.POST['company']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, phone=phone, company=company, subject=subject, message=message)
        contact.save()
        messages.success(request, 'Thanks For Contacting Us')
        return redirect('home')

    return render(request, 'webpages/contact.html')
