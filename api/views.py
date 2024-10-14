from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.views import APIView
from api.models import Student
from api.seriliazers import Student_Serializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


def home(request):
    return HttpResponse("<h1>CURD API Project </h1>")


#  This is Class for CURD API
class Students_Data(APIView):
    # this method is use to show data if we enter any id show that data other whise show all data
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
         
            stu = Student.objects.get(id=id)
            seriliazer=Student_Serializer(stu)
            return Response(seriliazer.data)
        stu = Student.objects.all()
        seriliazer=Student_Serializer(stu,many=True)
        return Response(seriliazer.data)
    
    #  this method used for post data 
    def post(self,request,format=None):
        seriliazer=Student_Serializer(data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response({'msg':'Data is Created......'},status.HTTP_400_BAD_REQUEST)
        return Response(seriliazer.errors,status.HTTP_400_BAD_REQUEST)
    
    #  this method is used for update all data
    def put(self,request,pk,format=None):
        stu = Student.objects.get(id=pk)
        serilizer=Student_Serializer(stu,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data is Put......'})
        return Response(serilizer.errors,status.HTTP_400_BAD_REQUEST)
    
    #  this method is used for update some data
    def patch(self,request,pk,format=None):
        stu = Student.objects.get(id=pk)
        serilizer=Student_Serializer(stu,data=request.data,partial=True)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data is Patch......'})
        return Response(serilizer.errors,status.HTTP_400_BAD_REQUEST)
    #  this method is used for delete any data by id
    def delete(self,request,pk,format=None):
        id=pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Dtata is Deleted....'})        


    
