from django.shortcuts import render, redirect
from userauth.forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def RegisterView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password1"])
            new_user.save()

            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            messages.success(request, f"Hey, {username}, your account was created successfully!")

            user = authenticate(request, username=username, password=raw_password)

            if user is not None:
                login(request, user)
                return redirect("core:index")
            else:
                messages.error(request, "Something went wrong. We couldn't log you in. Try logging in manually.")
                return redirect("core:index")  # Or wherever your login page is

    elif request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect("core:index")

    else:
        form = UserRegistrationForm()

    context = {"signup": form}
    return render(request, 'auth/register.html', context)



