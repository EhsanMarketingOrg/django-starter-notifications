from django.shortcuts import render
from notifications.signals import notify
from django.contrib.auth import get_user_model

import datetime

User = get_user_model()

def inbox(request):
    user = User.objects.all()[0]
    notify.send(user, recipient=user, verb='you reached level 10')
    context = {
        'time': datetime.datetime.now()
    }
    return render(request, 'our_notifications/inbox.html', context)
