from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drfapp.models import Student
from drfapp.serializer import StudentSerializer
from rest_framework.viewsets import ViewSet


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

#Code for viewset

class StudentViewset(ViewSet):
    def list(self,request, *args, **kwargs):
      student = Student.objects.all()
      serializer = StudentSerializer(student, many=True)
      return Response(serializer.data)

    def create(self,request,*args,**kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Create through viewset"}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk, *args, **kwargs):
        if pk:
            student_object= Student.objects.get(id=pk)
            serializer = StudentSerializer(student_object, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"updated"},status=status.HTTP_200_OK)
            return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request, pk):
        if pk:
            student = Student.objects.get(id=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self,request,pk):
        if pk:
            student = Student.objects.get(id=pk)
            serializer = StudentSerializer(student, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"updated"}, status=status.HTTP_200_OK)
            return Response({"errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        if pk:
            Student.objects.get(id=pk).delete()
            return Response({"msg":"Deleted by viewset"},status=status.HTTP_200_OK)





