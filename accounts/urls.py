from django.urls import path
from .views import UserSignUp, UserLogin, UserLogout, user_update, sign_up_success


urlpatterns = [
    path('signup/', UserSignUp.as_view(), name='signup'),
    path('sign-up-success/', sign_up_success, name='signup_success'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('profile/update/', user_update, name="update_profile"),
]
