from django.shortcuts import render , redirect, get_object_or_404 , get_list_or_404

#Import models
from .models import Account , Enterprise


# Create your views here.

def viewPosition(request):
    asociados = Account.objects.all()
    context ={
        'asociados':asociados
    }
    return render(request, 'home.html' , context)

def enterprise(request):
    info_enterprise = Enterprise.objects.all()
    print(info_enterprise)
    context = {
        'info_enterprise':info_enterprise
    }
    return render (request,'accounts/enterprise.html', context)

def staff(request):
    return render(request,'accounts/staff.html')