from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        #exclude = ['id','name']
        # read_only_fields = ['id']
        depth = 1










# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     group_id = serializers.IntegerField()
#     full_name = serializers.CharField(max_length=150)
#     age = serializers.IntegerField(max_value=100,min_value=6)
#     address = serializers.CharField(max_length=150)
#     phone_number = serializers.CharField(max_length=13)
#     email = serializers.EmailField()
#
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.group_id = validated_data.get("group_id",instance.group_id)
#         instance.full_name = validated_data.get("full_name",instance.full_name)
#         instance.age = validated_data.get("age",instance.age)
#         instance.address = validated_data.get("address",instance.address)
#         instance.phone_number = validated_data.get("phone_number",instance.phone_number)
#         instance.email = validated_data.get("email",instance.email)
#         instance.save()
#         return instance
