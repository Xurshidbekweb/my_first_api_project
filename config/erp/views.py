from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Student

# Create your views here.

class IndexApiView(APIView):
    def get(self,request: Request):
        students = Student.objects.all()
        new_students = []
        for student in students:
            new_students.append({
                "id": student.id,
                "group": student.group.name,
                "full_name": student.full_name,
                "age": student.age,
                "address": student.address,
                "phone_number": student.phone_number,
                "email": student.email,
            })
        return Response({"students":new_students})
