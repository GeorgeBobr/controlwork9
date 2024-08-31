from django.urls import path
from api_v1.views import add_to_favorites, remove_from_favorites

urlpatterns = [
    path('favorites/add/<str:entity_type>/<int:entity_id>/', add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<str:entity_type>/<int:entity_id>/', remove_from_favorites, name='remove_from_favorites'),
]