from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import MyUserCreationForm
from accounts.models import Profile
from webapp.models import Photo, Album

User = get_user_model()


class RegistrationView(CreateView):
    form_class = MyUserCreationForm
    template_name = "registration.html"
    model = User

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:photo_list')
        return next_url


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "profile.html"
    context_object_name = "user_obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        public_albums = Album.objects.filter(author=user, is_public=True)
        public_photos = Photo.objects.filter(author=user, album__isnull=True, is_public=True)
        context['public_albums'] = public_albums
        context['public_photos'] = public_photos
        if self.request.user == user:
            private_albums = Album.objects.filter(author=user, is_public=False)
            private_photos = Photo.objects.filter(author=user, album__isnull=True, is_public=False)
            context['private_albums'] = private_albums
            context['private_photos'] = private_photos
            favorite_photos = Photo.objects.filter(favorited_by=user, is_public=True)
            favorite_albums = Album.objects.filter(favorited_by=user, is_public=True)
            context['favorite_photos'] = favorite_photos
            context['favorite_albums'] = favorite_albums
            context['show_favorites_link'] = True

        return context

