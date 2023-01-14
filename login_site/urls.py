from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

#This App handles 4 URL's : for login, for signup, for logout, for password change

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('signup/',views.sign_up_view,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('change_password/',views.change_password_view,name="change_password"),
    re_path(r'^otpverify/(?P<username>[\w.@+-]+)/$',views.otp_verify,name='otp_verify'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('password_reset/', views.password_reset_request, name="password_reset")
]