from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UserForm
from myapp.models import User
import random


def get_dynamic_content():
    
    random_quote = random.choice([
        "Believe you can and you're halfway there.",
        "The only way to do great work is to love what you do.",
        "It always seems impossible until it's done.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Don't watch the clock; do what it does. Keep going."
    ])
    
    return {
        
        "random_quote": random_quote,
    }

def index(request):
    dynamic_content=get_dynamic_content()
    return render(request, 'index.html',dynamic_content)
    
def form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user=User(name=form.cleaned_data['name'],email=form.cleaned_data['email'])
            user.save()
            return redirect('success')
    else:
        form = UserForm()
    return render(request, 'form.html', {'form': form})

def success(request):
    users=User.objects.all()
    return render(request, 'success.html',{'users':users})





