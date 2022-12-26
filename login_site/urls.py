from django.urls import path
from . import views

#This App handles 4 URL's : for login, for signup, for logout, for password change

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('signup/',views.sign_up_view,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('change_password/',views.change_password_view,name="change_password"),
]