from django.urls import path
from webapp.views.views import PhotoListView, PhotoCreateView, PhotoDeleteView, PhotoDetailView, PhotoUpdateView
from webapp.views.album_views import AlbumCreateView, AlbumDeleteView, AlbumDetailView, AlbumUpdateView

app_name = 'webapp'

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),
    path('photos/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('photos/create/', PhotoCreateView.as_view(), name='photo_create'),
    path('photos/<int:pk>/edit/', PhotoUpdateView.as_view(), name='photo_edit'),
    path('photos/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),

    path('albums/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
    path('albums/create/', AlbumCreateView.as_view(), name='album_create'),
    path('albums/<int:pk>/edit/', AlbumUpdateView.as_view(), name='album_edit'),
    path('albums/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
]
