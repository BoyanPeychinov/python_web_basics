from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, FormView

from petstagram.accounts.forms import LoginForm, RegisterForm, ProfileForm
from petstagram.accounts.models import Profile
from petstagram.pets.models import Pet


class LoginUserView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm
    success_url = reverse_lazy('index')


# def login_user(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('index')
#     else:
#         form = LoginForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'accounts/login.html', context)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

# def register_user(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('index')
#     else:
#         form = RegisterForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'accounts/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


class ProfileDetailsView(LoginRequiredMixin, FormView):
    template_name = 'accounts/user_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile details')
    object = None

    def get(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=request.user.id)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=request.user.id)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object.profile_image = form.cleaned_data['profile_image']
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pets'] = Pet.objects.filter(user_id=self.request.user.id)
        context['profile'] = self.object

        return context


# @login_required
# def profile_details(request):
#     profile = Profile.objects.get(pk=request.user.id)
#     if request.method == 'POST':
#         form = ProfileForm(
#             request.POST,
#             request.FILES,
#             instance=profile,
#         )
#         if form.is_valid():
#             form.save()
#             return redirect('profile details')
#     else:
#         form = ProfileForm(instance=profile)
#
#     user_pets = Pet.objects.filter(user_id=request.user.id)
#
#     context = {
#         'form': form,
#         'pets': user_pets,
#         'profile': profile,
#     }
#
#     return render(request, 'accounts/user_profile.html', context)
