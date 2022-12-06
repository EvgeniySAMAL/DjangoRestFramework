import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Person

# class PersonModel:
#     def __init__(self,title,content):
#         self.title = title
#         self.content = content

class PersonSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) #удаление поля "пользователь" с таблицы
    class Meta:
        model = Person
        # fields = ("title","content","cat")
        # если нужно вернуть все поля
        fields = "__all__"

# def encode():
#     model = PersonModel('Даша', 'Content: Даша')
#     model_sr = PersonSerializer(model)
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