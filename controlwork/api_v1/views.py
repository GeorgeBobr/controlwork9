from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from webapp.models import Photo, Album

@login_required
@api_view(['POST'])
def add_to_favorites(request, entity_type, entity_id):
    user = request.user
    if entity_type == 'photo':
        entity = Photo.objects.get(id=entity_id)
        if user in entity.favorited_by.all():
            return Response({'error': 'Already in favorites'}, status=status.HTTP_400_BAD_REQUEST)
        entity.favorited_by.add(user)
    elif entity_type == 'album':
        entity = Album.objects.get(id=entity_id)
        if user in entity.favorited_by.all():
            return Response({'error': 'Already in favorites'}, status=status.HTTP_400_BAD_REQUEST)
        entity.favorited_by.add(user)
    else:
        return Response({'error': 'Invalid entity type'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)

@login_required
@api_view(['POST'])
def remove_from_favorites(request, entity_type, entity_id):
    user = request.user
    if entity_type == 'photo':
        entity = Photo.objects.get(id=entity_id)
        if user not in entity.favorited_by.all():
            return Response({'error': 'Not in favorites'}, status=status.HTTP_400_BAD_REQUEST)
        entity.favorited_by.remove(user)
    elif entity_type == 'album':
        entity = Album.objects.get(id=entity_id)
        if user not in entity.favorited_by.all():
            return Response({'error': 'Not in favorites'}, status=status.HTTP_400_BAD_REQUEST)
        entity.favorited_by.remove(user)
    else:
        return Response({'error': 'Invalid entity type'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)
