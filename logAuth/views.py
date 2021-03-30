from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth import logout
from django.contrib.auth.models import User, auth   # for check user



# Create your views here.
def index(request):

    return render(request,'index.html')


def register(request):
    template_name = 'signIn.html'

    if request.method == 'POST':
        
        # Get form value
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if password match
        if password == password2:
            # Check UserName
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken..!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used..!')
                    return redirect('register')
                else:
                    # looks good ......
                    user = User.objects.create_user(username=username, password=password,
                        email=email,first_name=first_name, last_name=last_name)
                    
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now logged in')
                    return redirect('login')
        else:
            # error message
            messages.error(request, 'password do not match..!')
            return redirect('register')

    else:
        return render(request, template_name )






def login(request):
    template_name = 'signIn.html'

    if request.method == 'POST':
        # login User
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, ' Invalid credentials')
            return redirect('login')

    else:
        return render(request, template_name )







def logout(request):
    auth.logout(request)   
    return redirect('index')

