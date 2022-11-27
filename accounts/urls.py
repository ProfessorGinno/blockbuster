from django.urls import path
from django.contrib import admin
from .views import UserSignUp, UserLogin, UserLogout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', UserSignUp.as_view(), name='signup'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
]
