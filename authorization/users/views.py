from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from .models import Person, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import PersonSerializer

# class PersonViewSet(viewsets.ModelViewSet): # весь функционал DRF ,добавление,удаление,изменение,чтение
#     # queryset = Person.objects.all()   если есть метод get_queryset, queryset не нужен. В urls.py добавим basename='person'
#     serializer_class = PersonSerializer
#
#     def get_queryset(self): # возвращает список определенных данных
#         pk = self.kwargs.get("pk")
#         if not pk:
#             return Person.objects.all()[:3]
#         return Person.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=True) #декоратор для определения новых маршрутов (пример: определение списка катерории)
#     def category(self, request,pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats':cats.name})

class PersonAPIListPagination(PageNumberPagination): #  для отдельных API запросов настройка cвоих параметров пагинации
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000

class PersonAPIList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,) #ограничение доступа лицам
    pagination_class = PersonAPIListPagination #(код пишется когда есть пагинация)подключение этого класса к классу пагинации

class PersonAPIUpdate(generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticated,) #функционал изменения записи, доступен только автору(IsOwnerOrReadOnly)
                                            #содержимое записи, доступен только авторизованным пользователям(IsAuthenticated)
   # authentication_classes = (TokenAuthentication,) #предоставляет доступ только по токенам


class PersonAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAdminOrReadOnly,) # функционал удаления, доступен только администратору

# class PersonAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# class PersonApiView(APIView):
#     def get(self,request):
#         w = Person.objects.all()
#         return Response({'posts':PersonSerializer(w,many=True).data})
#
#     def post(self,request):
#         serializer = PersonSerializer(data=request.data)
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
#             instance = Person.objects.get(pk=pk)
#         except:
#             return Response ({"error": "Method PUT not allowed"})
#
#         serializer = PersonSerializer(data=request.data, instance=instance)
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


# class PersonApiView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = PersonSerializer