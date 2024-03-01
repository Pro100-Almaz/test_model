from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from feed.models import YoutubeVideo
from feed.serializers import YouTubeVideoSerializer


@api_view(['GET', 'POST'])
def youtube_video_list(request):
    if request.method == 'GET':
        snippets = YoutubeVideo.objects.all()
        serializer = YouTubeVideoSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = YouTubeVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def youtube_video_item(request, pk):
    try:
        snippet = YoutubeVideo.objects.get(pk=pk)
    except YoutubeVideo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = YouTubeVideoSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = YouTubeVideoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)