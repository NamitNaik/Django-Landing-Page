from django.shortcuts import render
from .models import UserInfo
from .forms import UserInfoForm
from django.http import HttpResponse
# Create your views here.

def index(request):
    form = UserInfoForm()

    if request.method == 'POST':
        form = UserInfoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return thanku(request)

    return render(request,'basic_app/index.html',{'form':form})

def thanku(request):
    return render(request, 'basic_app/thanku.html',{'thanku':thanku})

def about(request):
    return render(request,'basic_app/about.html',{})
