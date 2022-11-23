from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect(profile)
    else:
        return render(request, "index.html")

@login_required
def profile(request):
    content = {
        "profiles" : request.user.profiles.all()
    }
    return render(request, "account/profile.html", content)

@login_required
def browse(request):
    return render(request, "browse.html")