from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

from .serializers import ItemSerializer
from core.models import Item


class ItemView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class ItemCreateView(generics.CreateAPIView):
#     serializer_class = ItemSerializer
#     queryset = Item.objects.all()


class ItemListCreateView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


# class TestView(APIView):

#     permission_classes = (IsAuthenticated, )

#     def get(self, request, *args, **kwargs):
#         qs = Item.objects.all()
#         serializer = ItemSerializer(qs, many=True)

#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = ItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# def test_view(request):
#     data = {
#         'name': 'john',
#         'age': 23
#     }

#     return JsonResponse(data)
