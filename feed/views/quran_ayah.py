from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from feed.models import QuranAyahOfDay
from feed.serializers import QuranAyahOfDaySerializer


@api_view(['GET', 'POST'])
def quran_ayah_list(request):
    if request.method == 'GET':
        snippets = QuranAyahOfDay.objects.all()
        serializer = QuranAyahOfDaySerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuranAyahOfDaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def quran_ayah_item(request, pk):
    try:
        snippet = QuranAyahOfDay.objects.get(pk=pk)
    except QuranAyahOfDay.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuranAyahOfDaySerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuranAyahOfDaySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
