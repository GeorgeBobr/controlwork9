from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from webapp.models import Album

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album/album_detail.html'


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['image', 'caption', 'album', 'is_public']
    template_name = 'album/album_create.html'
    success_url = reverse_lazy('album_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AlbumUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Album
    fields = ['image', 'caption', 'album', 'is_public']
    template_name = 'album/album_update.html'
    success_url = reverse_lazy('album_list')

    def test_func(self):
        album = self.get_object()
        return self.request.user == album.author


class AlbumDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Album
    template_name = 'album/album_delete.html'
    success_url = reverse_lazy('album_list')

    def test_func(self):
        album = self.get_object()
        return self.request.user == album.author
