from django.urls import path
from .views import UserSignUp, UserLogin, UserLogout, ProfileUpdate, sign_up_success


urlpatterns = [
    path('signup/', UserSignUp.as_view(), name='signup'),
    path('sign-up-success/', sign_up_success, name='signup_success'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('user-profile/<int:pk>', ProfileUpdate.as_view(), name="profile-update"),
]