from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.views.generic.list import ListView
from django.views.generic import DeleteView, CreateView

from .forms import UserEditForm
from . models import UserProfile


class UserSignUp(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('signup_success')
    template_name = 'accounts/signup.html'


class UserLogin(LoginView):
    template_name = 'accounts/user_login.html'
    next_page = reverse_lazy('movie_index')


class UserLogout(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/user_logout.html'


@login_required
def user_update(request):

    user = request.user
    user_profile, _ = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form_update = UserEditForm(request.POST, request.FILES)

        if form_update.is_valid():
            data = form_update.cleaned_data
            user.first_name = data.get("first_name")
            user.last_name = data.get("last_name")
            user.email = data.get("email")
            user_profile.phone = data.get("phone")
            user_profile.address = data.get("address")
            user_profile.country = data.get("country")
            user_profile.state = data.get("state")
            user_profile.city = data.get("city")
            user_profile.image = data.get("image")

            user_profile.save()
            user.save()
            return redirect("update_profile")
        else:
            return render(request, 'accounts/edit_user.html', {'form_update': form_update})
    form_update = UserEditForm(
        initial={
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.userprofile.phone,
            "address": user.userprofile.address,
            "country": user.userprofile.country,
            "state": user.userprofile.state,
            "city": user.userprofile.city,
            "image": user.userprofile.image
        }
    )
    return render(request, 'accounts/edit_user.html', {'form_update': form_update})


def sign_up_success(request):
    return render(request, template_name="accounts/sign_up_success.html")
