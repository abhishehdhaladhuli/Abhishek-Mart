from django.urls import path
from . import views  # Import views from the same app
from .forms import Login
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('', views.handle_request, name='home'),                  # e.g. /api/
    path('contact/', views.contact, name='contact'),    
    path('signup/',views.signup,name='signup'),
    path('login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=Login),name='login')
    
]
