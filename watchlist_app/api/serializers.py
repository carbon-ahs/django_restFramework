from django.db import models
from django.db.models import fields
from django.utils.translation import activate
from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['name', 'desription']
        # exclude = ['name']

    def get_len_name(self, object):
        return len(object.name)


    def validate(self, data): #object lvl validator
        if data['name'] == data['description']:
            raise serializers.ValidationError('name and des is same')
        return data

    def validate_description(self, value): #field validation 'validate_filedName'
        if len(value) > 200:
            raise serializers.ValidationError('too long!!')
        return value


# def lenght_check(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Too Short!!')

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[lenght_check])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         #instance.name = validated_data.get('name', instance.name)
#         #instance. = validated_data.get('', instance.)
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)        
#         instance.save()
#         return instance
    
#     def validate(self, data): #object lvl validator
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('name and des is same')
#         return data

#     def validate_description(self, value): #field validation 'validate_filedName'
#         if len(value) > 200:
#             raise serializers.ValidationError('too long!!')
