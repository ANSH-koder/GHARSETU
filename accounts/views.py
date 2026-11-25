
from django.shortcuts import render
from .models import User


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
