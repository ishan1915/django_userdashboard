from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
 
from .models import UserDetail
from .forms import SignUpForm,UserDetailForm
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from .forms import SignUpForm, LoginForm, ChangePasswordForm
from .models import CustomUser
from .tokens import account_activation_token

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')  # Redirect to dashboard page page after login
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keeps the user logged in after password change
            return redirect('dashboard')  # Redirect to dashboard after success
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'change_password.html', {'form': form})



@login_required
def dash_view(request):
    user=request.user
    try:
        user_detail = UserDetail.objects.get(user=user)
    except UserDetail.DoesNotExist:
        user_detail = None

 
    return render(request, 'dashboard.html', {'user_detail': user_detail, 'username': user.username})

@login_required
def profile_view(request):
    try:
        user_detail = UserDetail.objects.get(user=request.user)
    except UserDetail.DoesNotExist:
        user_detail = None

 
    return render(request, 'displayprofile.html', {'user_detail': user_detail})

  

def profile_edit(request,user_id):
    try:
        user_detail = UserDetail.objects.get(id=user_id,user=request.user)
    except UserDetail.DoesNotExist:
        user_detail = UserDetail(user=request.user)
    
    if request.method == 'POST':
        form = UserDetailForm(request.POST, request.FILES ,instance=user_detail)
        if form.is_valid():
            form.save()
            return redirect('displayprofile')  # Redirect to profile view after editing
    else:
        form = UserDetailForm(instance=user_detail)
    
    return render(request, 'editprofile.html', {'form': form})

def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = CustomUser.objects.filter(email=email).first()
            if user:
                token = account_activation_token.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_url = f"http://127.0.0.1:8000/password-reset-confirm/{uid}/{token}/"
                
                send_mail(
                    "Reset Your Password",
                    f"Click the link to reset your password: {reset_url}",
                    "your-email@example.com",
                    [email],
                    fail_silently=False,
                )
            return redirect('login')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})