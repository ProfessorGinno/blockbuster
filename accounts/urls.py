from django.urls import path
from .views import UserSignUp, UserLogin, UserDelete, UserLogout, user_update, profile, sign_up_success


urlpatterns = [
    path('signup/', UserSignUp.as_view(), name='signup'),
    path('sign-up-success/', sign_up_success, name='signup_success'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('profile/delete/<int:pk>', UserDelete.as_view(), name="delete_profile"),
    path('profile/update/', user_update, name="update_profile"),
    path('profile/', profile, name="profile"),
]
