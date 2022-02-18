from django.shortcuts import render
from .models import pastes,PasteTextAccess
import secrets
import string
import datetime
import requests
import json
# Create your views here.

def home(request):
    if request.method=='GET':
        print(type(request.get_host()))
        paste=pastes.objects.all()
        return render(request,'app/home.html',{'paste':paste})
    elif request.method=='POST':
        if 'submit' in request.POST:
            res = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(6))
            pastes.objects.create(unique_link=res,snippet=request.POST['snippet'], encrypted = False)
            paste=pastes.objects.all()
            return render(request,'app/home.html',{'res': 'Your URL is:'+ request.get_host() + '/' + res, 'paste':paste})

def display_snippet(request,res):
    if request.method=='GET':
        url = 'https://api.bigdatacloud.net/data/client-ip/'
        r = requests.get(url)
        r = r.json()
        print('@@@@@@', r)
        paste = pastes.objects.get(unique_link = res)
        pasteAccess = PasteTextAccess(ip_address = r['ipString'], user_text = paste)
        pasteAccess.save()
        ip_list = PasteTextAccess.objects.filter(user_text = paste)
        return render(request, 'app/display_snippet.html', {"ip_list": ip_list, "paste": paste})
   
def delete(request,id):
    if request.method=='POST':
        paste=pastes.objects.get(id=id)
        paste.delete()
        paste=pastes.objects.all()
        return render(request,'app/home.html',{'paste':paste})

        
def renew(request,id):
    if request.method=='POST':
        paste=pastes.objects.get(id=id)
        paste.creation_date = datetime.datetime.now()
        paste.save()
        paste=pastes.objects.all()
        return render(request,'app/home.html',{'paste':paste})