from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView as AuthLogoutView
from .forms import SignupForm

login = LoginView.as_view(template_name='accounts/login_form.html')

def logout(request):
    auth_logout(request)
    messages.success(request, "로그아웃되었습니다.")
    next_url = request.GET.get('next', '/')
    return redirect(next_url)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)    # 회원가입 후 자동 로그인
            messages.success(request, '회원가입 환영합니다.')
            # signed_user.send_welcome_email()
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })