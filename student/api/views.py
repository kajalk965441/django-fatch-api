from api.models import Student
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StudentSerializer

@api_view(['GET'])
def index(request):
    student = Student.objects.all()
    serialstudent = StudentSerializer(student, many=True)
    return JsonResponse(serialstudent.data, safe=False)
