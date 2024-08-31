from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from webapp.models import Photo, Album


class PhotoListView(ListView):
    model = Photo
    template_name = 'photos/photo_list.html'
    context_object_name = 'photos'
    paginate_by = 10

    def get_queryset(self):
        return Photo.objects.filter(is_public=True).order_by('-created_at')


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photos/photo_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = self.object
        context['has_access_token'] = bool(photo.access_token)
        return context

    @login_required
    def post(self, request, *args, **kwargs):
        photo = self.get_object()
        if request.user == photo.author and not photo.access_token:
            photo.generate_access_token()
            return redirect('webapp:photo_detail', pk=photo.pk)
        return super().post(request, *args, **kwargs)

class PhotoDetailByTokenView(DetailView):
    model = Photo
    template_name = 'photos/photo_detail.html'

    def get_object(self, queryset=None):
        token = self.kwargs.get('token')
        photo = get_object_or_404(Photo, access_token=token)
        if not photo.is_public and self.request.user != photo.author:
            raise Http404("Фото не доступно")
        return photo


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['image', 'caption', 'album', 'is_public']
    template_name = 'photos/photo_create.html'
    success_url = reverse_lazy('webapp:photo_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.filter(author=self.request.user)
        return context

class PhotoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    fields = ['image', 'caption', 'album', 'is_public']
    template_name = 'photos/photo_edit.html'
    success_url = reverse_lazy('webapp:photo_list')

    def test_func(self):
        photo = self.get_object()
        user = self.request.user
        return user.is_staff or user == photo.author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        return context


class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    template_name = 'photos/photo_delete.html'
    success_url = reverse_lazy('webapp:photo_list')

    def test_func(self):
        photo = self.get_object()
        return self.request.user == photo.author

