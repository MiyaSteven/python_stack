from django.shortcuts import render, redirect
from .models import Dojo, Ninjas

def index(request):
    context = {
        'all_dojos' : Dojo.objects.all(),
        'all_ninjas' : Ninjas.objects.all()
    }
    return render(request, 'index.html', context)

def process_dojo(request):
    Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state']
    )
    return redirect('/')

def process_ninja(request):
    this_dojo = Dojo.objects.get(id=request.POST['dojo'])
    Ninjas.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo=this_dojo
    )
    return redirect('/')

def delete_dojo(request, dojoId):
    void_dojo = Dojo.objects.get(id = dojoId)
    void_dojo.delete()
    return redirect('/')
