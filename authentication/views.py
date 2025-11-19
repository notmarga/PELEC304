# from django.shortcuts import render, redirect
# from .forms import RegisterForm, LoginForm
# from .models import UserAccount

# def register_view(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = RegisterForm()

#     return render(request, "authentication/register.html", {"form": form})


# def login_view(request):
#     msg = ""
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']

#             try:
#                 user = UserAccount.objects.get(email=email, password=password)
#                 request.session['user_id'] = user.id  # simple session login
#                 return redirect('home')
#             except UserAccount.DoesNotExist:
#                 msg = "Invalid email or password."
#     else:
#         form = LoginForm()

#     return render(request, "authentication/login.html", {"form": form, "msg": msg})


# def home_view(request):
#     return render(request, "authentication/home.html")


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm

# * Register View
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form. save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login_user')
        else:

            messages.error(request, 'Please correct the errors below. ')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})




def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
            else:

                messages.error(request, "Invalid username or password. ")

        else:
            messages.error(request, 'Invalid input. ')

    else:

        form = AuthenticationForm()
    return render(request, 'accounts/login.html ', {'form': form})



def logout_user(request):
    logout (request)
    messages.info(request, 'You have been logged out. ')
    return redirect('login_user')

# * Dummy Dashboard
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
