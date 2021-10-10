from django.core.mail import send_mail
from django.http import HttpResponse

def emailfunc(request):
    send_mail(
        'タイトル',
        '本文',
        'daigorou4be@gmail.com',
        ['abe.daigoro.sb@tut.jp'],
        fail_silently=False
    )
    return HttpResponse('')