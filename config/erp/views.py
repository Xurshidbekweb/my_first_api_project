from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
# Create your views here.

class StudentApiView(APIView):
    def get(self,request: Request,pk=None):

        if pk:
            try:
                student = Student.objects.get(pk=pk)
                return Response(StudentSerializer(student).data)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)



        students = Student.objects.all()
        return Response(StudentSerializer(students,many=True).data)


    def post(self,request: Request,pk=None):
        if pk:
            return Response(status=status.HTTP_404_NOT_FOUND)


        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        """ Buni o'rniga qisqaroq yo'li serializer.py  da  create function yoziladi va shu faylga chaqiriladi 42 qator """
        # student = Student.objects.create(
        #     group_id = request.data["group_id"],
        #     full_name = request.data["full_name"],
        #     address = request.data["address"],
        #     age = request.data["age"],
        #     phone_number = request.data["phone_number"],
        #     email = request.data["email"],
        # )
#------------------------------------------

        student = serializer.save()

        return Response(StudentSerializer(student).data)


    def put(self,request: Request,pk=None):
        if not pk:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_student = serializer.update(student,serializer.validated_data)
            return Response(StudentSerializer(updated_student).data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)



    def delete(self,request: Request,pk=None):
        if not pk:
            return Response("ochiirb bomidi",status=status.HTTP_404_NOT_FOUND)

        try:
            student = Student.objects.get(pk=pk)
            student.delete()
            return Response({"message":"success"})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
