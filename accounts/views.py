from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from accounts.serializers import AccountSerializer
from accounts.models import Account
from accounts.serializers import UserSerializer
from accounts.models import completedTask
from accounts.serializers import TaskSerializer
from accounts.models import App
from accounts.serializers import AppSerializer
from accounts.serializers import completedTaskSerializer
from rest_framework.parsers import MultiPartParser,FormParser
# Create your views here.
class RegisterUser(APIView):
    def post(self, request):
        try:
            user=request.data
            print(request.data)
            userserializer=AccountSerializer(data=request.data)
            datas={} #to pass data to front end just for verification not nessery
            if userserializer.is_valid():
                acc = userserializer.save()
                if acc:
                    print('aadsfasdfasdf',acc)
                    print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
                    return Response(status=status.HTTP_201_CREATED)
                else:
                    print('error is here',acc)    
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            print("errors",userserializer.errors)
            datas["error"] = userserializer.errors
            
            return  Response(
                datas,status=status.HTTP_400_BAD_REQUEST)

class Profile(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        try:
            user=request.user
            print(user.id)
            user_data= Account.objects.filter(username=user)
            print(user_data)
            userserializer=UserSerializer(user_data,many=True)
            if userserializer.is_valid: 
                return Response(userserializer.data,status=status.HTTP_200_OK)
            else:
                return Response(userserializer.errors,status=status.HTTP_404_NOT_FOUND)

        except:
            return Response(userserializer.errors,status=status.HTTP_404_NOT_FOUND)
            
class UserTask(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        serializer=None
        u_data={}
        try:
            user=request.user
            user_data= completedTask.objects.filter(users=user.id)
            print(user_data)
           
            serializer=TaskSerializer(user_data,many=True)
            if serializer.is_valid:
                return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

            

class Showapp(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        serializer=None
        try:
            app_data=App.objects.all()
            serializer=AppSerializer(app_data,many=True)
            if serializer.is_valid: 
                return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


class Completetask(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes=(MultiPartParser, FormParser)
    def post(self,request):
        print(request.data)

        value=request.data
        tasking=completedTaskSerializer(data=request.data)
        if tasking.is_valid():
            tasking.save()
            user=request.user
            app=App.objects.get(id=value["app"])
            print(app)
            user.my_points=int(user.my_points)+int(app.points)
            user.save()
            return Response(status=200)
        else:
            data=tasking.errors
            return Response(data,status=status.HTTP_404_NOT_FOUND)
class Addapp(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        tasking=None
        data={}
        try:
            user=user=request.user
            if user.is_admin:
                print(request.data)
                tasking=AppSerializer(data=request.data)
                if tasking.is_valid():
                    tasking.save()
                    return Response(status=status.HTTP_201_CREATED)
                else:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(datastatus=status.HTTP_403_FORBIDDEN)
        except:
            return Response(data,status=status.HTTP_403_FORBIDDEN)

class Adminapps(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        print("dfkkkkkkkkkkkkkkkkkkkk")
        tasking=None
        
        try:
            user=request.user
            if user.is_admin:
                print("fffffffffffffffffffffA",user.id)
                app_data=App.objects.filter(creator=user.id)
                print("kllkkkkkkkkkkkkk")
                tasking=AppSerializer(data=app_data,many=True)
                print("jjjjjjjjjjjjjjjjjjjjjjj")
                tasking.is_valid()
                print("KKKKKKKKKKKKKKKKKKKKKKKKK")
                return Response(tasking.data,status=status.HTTP_200_OK)
                # else:
                #     return Response(tasking.data,status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(tasking.errors,status=status.HTTP_403_FORBIDDEN)





