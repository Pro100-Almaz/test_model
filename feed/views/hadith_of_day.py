from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from feed.models import HadithOfDay
from feed.serializers import HadithOfDaySerializer


@api_view(['GET', 'POST'])
def hadith_of_day_list(request):
    if request.method == 'GET':
        snippets = HadithOfDay.objects.all()
        serializer = HadithOfDaySerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HadithOfDaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def hadith_of_day_item(request, pk):
    try:
        snippet = HadithOfDay.objects.get(pk=pk)
    except HadithOfDay.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HadithOfDaySerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HadithOfDaySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)