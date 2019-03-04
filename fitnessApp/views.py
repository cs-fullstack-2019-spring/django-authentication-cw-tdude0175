from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import FoodFitnessForm , FoodFitnessModel
# Create your views here.

# runs the basic index page for view
def index(request):
    return render(request,'fitnessApp/index.html')

# gathers the form information to be filled out
def newUser(request):
    form = FoodFitnessForm()

    context = \
        {
            'form': form
        }
    return render(request,'fitnessApp/newUser.html',context)

# saves the info then renders the index page for use
def saveNewUser(request):
    form = FoodFitnessForm(request.POST)

    User.objects.create_user(request.POST['username'],'','')
    form.save()

    return render(request,'fitnessApp/index.html')
