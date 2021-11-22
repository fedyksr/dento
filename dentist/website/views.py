from django.shortcuts import render
from django.core.mail import send_mail

def index (request):
    return render(request, 'index.html',{})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #send_mail
        send_mail(
            message_name , #subject
            message , #message
            message_email, #from email
            ['fedyksr@gmail.com'] , #To email
        )
        
        return render(request, 'contact.html',{'message_name':message_name})
    else:
        return render(request, 'contact.html',{})

def about (request):
    return render(request, 'about.html',{})

def pricing (request):
    return render(request, 'pricing.html',{})

def service (request):
    return render(request, 'service.html',{})

def appointment (request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_scheldule = request.POST['your-scheldule']
        your_time = request.POST['your-time']
        your_message = request.POST['your-message']
        #send_mail
        appointment = "Name : "+your_name+" phone: "+your_phone+" Email: "+your_email+"\n Address: "+your_address+"\n Schedule: "+your_scheldule+" Day: "+your_time+"\n Message: "+your_message
        send_mail(
            'Appointment Request' , #subject
            appointment , #message
            your_email, #from email
            ['fedyksr@gmail.com'] , #To email
        )
        
        
        return render(request, 'appointment.html',{
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_scheldule': your_scheldule,
            'your_time': your_time,
            'your_message': your_message
        })
    else:
        return render(request, 'index.html',{})

