from django.shortcuts import render, redirect

def index(request):
    print(request.session.keys())
    context={'key':42}
    return render(request, "index.html", context)

def process(request):
    print(request.session)
    print(request.session.keys())
    print("Form submitted and processed")
    if "name_in_form" in request.session:
        print("I has a name yey", request.session["name_from_form"])
        request.session["name_from_form"] = request.POST["name"]
        print("didn't haz name not yey, negayay!")
        request.session['favorite_flavor'] = request.POST["favorite_ice_cream"]
    return redirect("/checkout")

def checkout(request, name, location):
    print(request.session.keys())
    context = {
        "name" : request.session["name_from_form"],
    }
    return render(request, 'checkout.html', context)