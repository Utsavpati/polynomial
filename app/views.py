from django.shortcuts import render
from .models import pastes
import secrets
import string
import datetime
# Create your views here.

def home(request):
    if request.method=='GET':
        print(type(request.get_host()))
        return render(request,'app/home.html')
    elif request.method=='POST':
        res = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(6))
        pastes.objects.create(unique_link=res,snippet=request.POST['snippet'])
        return render(request,'app/home.html',{'res': 'Your URL is:'+ request.get_host() + '/' + res})

def display_snippet(request,res):
    if request.method=='GET':
        if datetime.datetime.now(datetime.timezone.utc) - pastes.objects.get(unique_link=res).creation_date > datetime.timedelta(1):
                pastes.objects.get(unique_link=res).delete()
                return render(request,'app/display_snippet.html',{'show': 'Link Expired or the page is not availble'})
        else:
            res=pastes.objects.get(unique_link=res)
            show=res.snippet
            return render(request,'app/display_snippet.html',{'show':show})

