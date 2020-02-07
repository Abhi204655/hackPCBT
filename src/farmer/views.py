from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LandForm
from .models import Land

from django.conf import settings


User = settings.AUTH_USER_MODEL

# Create your views here.
def home(request):
    return render(request,'farmer/home.html')


def land(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        width = request.POST.get('width')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        land = Land(length=length,width=width,owner=request.user,address=address,city=city,state=state)
        land.save()
        return redirect('/')
    else:
        return render(request,'farmer/land.html')

def profile(request):
    return render(request,'farmer/profile.html')