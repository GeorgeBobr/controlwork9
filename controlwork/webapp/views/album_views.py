from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from webapp.models import Album

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album/album_detail.html'

class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['title', 'description', 'is_public']
    template_name = 'album/album_create.html'
    success_url = reverse_lazy('webapp:photo_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AlbumUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Album
    fields = ['title', 'description', 'is_public']
    template_name = 'album/album_update.html'

    def test_func(self):
        album = self.get_object()
        return self.request.user == album.author

    def get_success_url(self):
        return reverse_lazy('webapp:album_detail', kwargs={'pk': self.object.pk})
class AlbumDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Album
    template_name = 'album/album_delete.html'

    def test_func(self):
        album = self.get_object()
        return self.request.user == album.author

    def get_success_url(self):
        user = self.request.user
        return reverse_lazy('accounts:profile', kwargs={'pk': user.pk})
