from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'index.html')


def loginUser(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        #checking user credentials 

        user = authenticate(username=username, password=password)

        if user is not None:
            #A backend authenticated the credentials
            login(request, user)
     
            return redirect('/') 

        else:
            # No backend authenticated the credentials

            return render(request, 'login.html')


    return render(request, 'login.html')

def signupHandle(request):
    if request.method =="POST":
        # Get the parameters
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['cnf-password']

        # check for erroneous parameters
        if len(username) > 10:
            messages.error(request, "username must be under 10 characters.")
            return redirect('/')

        # Checking username fulfills the criteria
        if not username.isalnum():
            messages.error(request, "username should only contain letters and nubmers ")
            return redirect('/')
        
        # password should match
        if pass1 != pass2:
            messages.error(request, "passwords do not match!")
            return redirect('/')



        # Create the user.
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()

        messages.success(request, "Your Socol account has been created!")
        return redirect('/')


    # else:
    #     return HttpResponse('404 - Not found')


    return render(request, 'signup.html')


def logoutUser(request):
    logout(request)

    return redirect("/login")


