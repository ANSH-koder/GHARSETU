
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.decorators import login_required


# USER REGISTRATION
def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')

        # Check whether passwords match
        if password != confirm_password:
            return render(request, 'accounts/register.html', {
                'error': 'Passwords do not match.'
            })

        # Check whether username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {
                'error': 'Username already exists.'
            })

        # Check whether email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'accounts/register.html', {
                'error': 'Email already registered.'
            })

        # Validate account type
        if role not in User.Role.values:
            return render(request, 'accounts/register.html', {
                'error': 'Invalid account type.'
            })

        # Create user
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role
        )

        return render(request, 'accounts/register.html', {
            'success': 'Your GHARSETU account has been created!'
        })

    return render(request, 'accounts/register.html')



# USER LOGIN
def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verify user credentials
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            # Create login session
            login(request, user)

            return redirect('dashboard')

        else:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid username or password.'
            })

    return render(request, 'accounts/login.html')


# USER LOGOUT
def user_logout(request):

    logout(request)

    return redirect('login')
    # USER DASHBOARD
@login_required
def dashboard(request):

    return render(request, 'accounts/dashboard.html')