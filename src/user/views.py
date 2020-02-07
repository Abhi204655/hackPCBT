from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations: you've successfully created account.")
            return redirect('/')
        else:
            messages.warning(request,'Please fill the form correctly!')
            return redirect('register')
    else:
        form = UserCreationForm()
        context = {'form':form}
        return render(request,'user/register.html',context)
