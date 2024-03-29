from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from feed.models import InspiringPicture
from feed.serializers import InspiringPictureSerializer

@api_view(['GET', 'POST'])
def inspiring_picture_list(request):
    if request.method == 'GET':
        snippets = InspiringPicture.objects.all()
        serializer = InspiringPictureSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InspiringPictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def inspiring_picture_item(request, pk):
    try:
        snippet = InspiringPicture.objects.get(pk=pk)
    except InspiringPicture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InspiringPictureSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InspiringPictureSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)