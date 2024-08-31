from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from webapp.models import Photo, Album


@login_required
@api_view(['POST'])
def add_to_favorites(request, entity_type, entity_id):
    user = request.user
    try:
        if entity_type == 'photo':
            entity = Photo.objects.get(id=entity_id)
        elif entity_type == 'album':
            entity = Album.objects.get(id=entity_id)
        else:
            return Response({'error': 'Invalid entity type'}, status=status.HTTP_400_BAD_REQUEST)

        if user in entity.favorited_by.all():
            return Response({'error': 'Already in favorites'}, status=status.HTTP_400_BAD_REQUEST)

        entity.favorited_by.add(user)
        return Response({'message': 'Added to favorites'}, status=status.HTTP_200_OK)

    except (Photo.DoesNotExist, Album.DoesNotExist):
        return Response({'error': 'Entity not found'}, status=status.HTTP_404_NOT_FOUND)


@login_required
@api_view(['POST'])
def remove_from_favorites(request, entity_type, entity_id):
    user = request.user
    try:
        if entity_type == 'photo':
            entity = Photo.objects.get(id=entity_id)
        elif entity_type == 'album':
            entity = Album.objects.get(id=entity_id)
        else:
            return Response({'error': 'Invalid entity type'}, status=status.HTTP_400_BAD_REQUEST)

        if user not in entity.favorited_by.all():
            return Response({'error': 'Not in favorites'}, status=status.HTTP_400_BAD_REQUEST)

        entity.favorited_by.remove(user)
        return Response({'message': 'Removed from favorites'}, status=status.HTTP_200_OK)

    except (Photo.DoesNotExist, Album.DoesNotExist):
        return Response({'error': 'Entity not found'}, status=status.HTTP_404_NOT_FOUND)
