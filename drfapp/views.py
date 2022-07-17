from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drfapp.models import Student
from drfapp.serializer import StudentSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


# Create your views here.

class Std(APIView):
    def get(self, request, format=None):
        std = Student.objects.all()
        serializer = StudentSerializer(std, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Created'}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#MODELVIEWSET

class StudentModelViewset(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


#Readonly MODELVIEWSET
class StudentModelViewsetReadonly(ReadOnlyModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()