from django.shortcuts import render
from .models import UserMessage


def getform(request):
    message = None
    all_messages = UserMessage.objects.all()
    if all_messages:
        message = all_messages[0]

    # if request.method == 'POST':
    #     name = request.POST.get('name', '')
    #     email = request.POST.get('email', '')
    #     address = request.POST.get('address', '')
    #     message = request.POST.get('message', '')
    #
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.email = email
    #     user_message.address = address
    #     user_message.message = message
    #     user_message.save()
    return render(request, 'message_form.html',{'message': message})


def get_message(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        message = request.POST.get('message', '')

        user_message = UserMessage()
        user_message.name = name
        user_message.email = email
        user_message.address = address
        user_message.message = message
        user_message.save()
    return render(request, 'message_form.html')