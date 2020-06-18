from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "index.html")

def test(request):
    return HttpResponse("test")

def process(request):
    print("Form submitted and processed")
    return redirect('/')
