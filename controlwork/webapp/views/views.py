from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from webapp.models import Photo

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


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['image', 'caption', 'album', 'is_public']
    template_name = 'photos/photo_create.html'
    success_url = reverse_lazy('webapp:photo_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PhotoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    fields = ['image', 'caption', 'album', 'is_public']
    template_name = 'photos/photo_edit.html'
    success_url = reverse_lazy('webapp:photo_list')

    def test_func(self):
        photo = self.get_object()
        return self.request.user == photo.author


class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    template_name = 'photos/photo_delete.html'
    success_url = reverse_lazy('webapp:photo_list')

    def test_func(self):
        photo = self.get_object()
        return self.request.user == photo.author