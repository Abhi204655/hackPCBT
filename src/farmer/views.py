from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LandForm
from .models import Land

from django.conf import settings


User = settings.AUTH_USER_MODEL

# Create your views here.
def home(request):
    return render(request,'farmer/home.html')


def landRegister(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        width = request.POST.get('width')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        img = request.POST.get('img')
        land = Land(length=length,width=width,owner=request.user,address=address,city=city,state=state,image=img)
        land.save()
        print("file saved succesfully")
        return redirect('/')
    else:
        return render(request,'farmer/landRegister.html')

def profile(request):
    lands = Land.objects.filter(owner__username=request.user.username).all()
    context = {
        'lands':lands
    }
    return render(request,'farmer/profile.html',context)

def search(request):
    query = request.GET['query']
    lands = Land.objects.filter(city__icontains=query)
    params = {'lands': lands}
    return render(request, 'farmer/search.html', params)


def land(request):
    lands = Land.objects.all()
    context = {
        'lands':lands
    }
    return render(request,"farmer/lands.html",context)