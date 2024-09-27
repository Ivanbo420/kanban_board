from rest_framework import generics
from .serializers import LoginSerializer
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "Login successful"}, status=200)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializer.data,
            "message": "Usuario creado exitosamente"
        }, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):

    
    serializer_class = LoginSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer, RegisterSerializer
from .models import User  # Ajusta si el modelo no es 'User'

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    # Método POST para login
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    # Obtener una lista de usuarios (GET)
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = self.get_serializer(users, many=True)
        return Response({
            "users": serializer.data,
            "message": "Lista de usuarios obtenida correctamente"
        }, status=status.HTTP_200_OK)

    # Crear un nuevo usuario (POST)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializer.data,
            "message": "Usuario creado exitosamente"
        }, status=status.HTTP_201_CREATED)

    # Actualizar un usuario existente (PUT)
    def put(self, request, pk=None, *args, **kwargs):
        user = User.objects.get(pk=pk)
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "user": serializer.data,
            "message": "Usuario actualizado correctamente"
        }, status=status.HTTP_200_OK)

    # Actualizar parcialmente un usuario existente (PATCH)
    def patch(self, request, pk=None, *args, **kwargs):
        user = User.objects.get(pk=pk)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "user": serializer.data,
            "message": "Usuario actualizado parcialmente"
        }, status=status.HTTP_200_OK)

    # Eliminar un usuario existente (DELETE)
    def delete(self, request, pk=None, *args, **kwargs):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({
            "message": "Usuario eliminado correctamente"
        }, status=status.HTTP_204_NO_CONTENT)
