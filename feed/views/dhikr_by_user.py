from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from feed.models import DhikrByUser
from feed.serializers import DhikrByUserSerializer


@api_view(['GET', 'POST'])
def dhikr_by_user_list(request):
    if request.method == 'GET':
        snippets = DhikrByUser.objects.all()
        serializer = DhikrByUserSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DhikrByUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def dhikr_by_user_item(request, pk):
    try:
        snippet = DhikrByUser.objects.get(pk=pk)
    except DhikrByUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DhikrByUserSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DhikrByUserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # elif request.method == 'POST':
    #     data = request.data
    #
    #     if data['action'] == 'get_like':
    #         snippet.