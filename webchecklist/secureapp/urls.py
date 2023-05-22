
from django.urls import path

from . import views


# Password management

from django.contrib.auth import views as auth_views



urlpatterns = [

    path('', views.home, name=''),

    path('register', views.register, name='register'),

    path('dashboard', views.dashboard, name='dashboard'),

    path('user-logout', views.user_logout, name='user-logout'),

    path('account-locked', views.account_locked, name='account-locked'),


    # Password management urls/views


    # 1 - Submit our email form 

    path('reset_password', auth_views.PasswordResetView.as_view(template_name='password-reset/password-reset.html'), name='reset_password'),


    # 2 - A success message stating that an email was sent to reset our password 

    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='password-reset/password-reset-sent.html'), name='password_reset_done'),


    # 3 - Send a link to our email... so that we can reset our password

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password-reset/password-reset-form.html'), name='password_reset_confirm'),


    # 4 - Show a success message stating that our password was changed 

    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password-reset/password-reset-complete.html'), name='password_reset_complete'),


]









