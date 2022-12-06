from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class UserApiView(APIView):
    def get(self,request):
        w = User.objects.all()
        return Response({'posts':UserSerializer(w,many=True).data})

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self,request,*args,**kwargs):
        pk = kwargs.get("pk",None)
        if not pk:
            return Response ({"error": "Method PUT not allowed"})

        try:
            instance = User.objects.get(pk=pk)
        except:
            return Response ({"error": "Method PUT not allowed"})

        serializer = UserSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post":serializer.data})

    def delete(self,request,*args,**kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

# код удаления таблицы с переданным pk

        return Response({"post": "delete post" + str(pk)})


# class UserApiView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer