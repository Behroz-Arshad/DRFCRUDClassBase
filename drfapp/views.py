from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drfapp.models import Student
from drfapp.serializer import StudentSerializer


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


class Studentapi(APIView):
    def put(self, request, pk):
        std = Student.objects.get(id=pk)
        serializer = StudentSerializer(std, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "updated", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        std = Student.objects.get(id=pk)
        serializer = StudentSerializer(std, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "updated", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self ,request,  pk, format = None):
        Student.objects.get(id=pk).delete()
        return Response({"msg": "Deleted"})

    def get(self, request,pk):
        std = Student.objects.get(id=pk)
        serializer = StudentSerializer(std)
        return Response(serializer.data)
