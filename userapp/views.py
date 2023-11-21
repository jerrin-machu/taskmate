#from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import CustomRegisterForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def register(request):
    
    if request.method == 'POST':
        register = CustomRegisterForm(request.POST)
        if register.is_valid():
            register.save()
            messages.success(request,"Account created successfully!")
            print("I am here only")
            return redirect('register')
        
        
    else:
        register = CustomRegisterForm()
    return render(request,'register.html',{'register_form':register})
    
    
