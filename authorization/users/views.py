from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Category
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet): # весь функционал DRF ,добавление,удаление,изменение,чтение
    # queryset = User.objects.all()   если есть метод get_queryset, queryset не нужен. В urls.py добавим basename='user'
    serializer_class = UserSerializer

    def get_queryset(self): # возвращает список определенных данных
        pk = self.kwargs.get("pk")
        if not pk:
            return User.objects.all()[:3]
        return User.objects.filter(pk=pk)

    @action(methods=['get'], detail=True) #декоратор для определения новых маршрутов (пример: определение списка катерории)
    def category(self, request,pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats':cats.name})

# class UserAPIList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class UserAPIUpdate(generics.UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserApiView(APIView):
#     def get(self,request):
#         w = User.objects.all()
#         return Response({'posts':UserSerializer(w,many=True).data})
#
#     def post(self,request):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self,request,*args,**kwargs):
#         pk = kwargs.get("pk",None)
#         if not pk:
#             return Response ({"error": "Method PUT not allowed"})
#
#         try:
#             instance = User.objects.get(pk=pk)
#         except:
#             return Response ({"error": "Method PUT not allowed"})
#
#         serializer = UserSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post":serializer.data})
#
#     def delete(self,request,*args,**kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
# # код удаления таблицы с переданным pk
#
#         return Response({"post": "delete post" + str(pk)})


# class UserApiView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer