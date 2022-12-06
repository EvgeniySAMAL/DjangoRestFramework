import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import User

# class UserModel:
#     def __init__(self,title,content):
#         self.title = title
#         self.content = content

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ("title","content","cat")
        # если нужно вернуть все поля
        fields = "__all__"

# def encode():
#     model = UserModel('Даша', 'Content: Даша')
#     model_sr = UserSerializer(model)
#     print(model_sr.data, type(model_sr.data))
#     json = JSONRenderer ().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Daria","content":"Content:Daria"}')
#     data = JSONParser().parse(stream)
#     serializer = UserSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)