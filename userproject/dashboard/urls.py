from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from dashboard import views as dash_views


urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dash_view,name='dashboard'),

    path('change-password/', views.change_password, name='change_password'),

    path('displayprofile/',views.profile_view,name='displayprofile'),
    path('editprofile/<int:user_id>/',views.profile_edit,name='editprofile'),
    

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),


    ]
