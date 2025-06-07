from django.shortcuts import render
from rest_framework.views import APIView


class Clase_Seguridad_Registro (APIView) :
    
    def post (self, request) :
        pass

class Clase_Seguridad_Validacion (APIView) :
    
    def get (self, request, token) :
        pass

class Clase_Seguridad_LogIn (APIView) :
    
    def post (self, request) :
        pass