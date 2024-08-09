from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import User
from .serializers import (
    VerifyOTPSerializer,
    UserSerializer,
    LoginSerialiazer,
)


# La clase `VerityOTPView` en Python define un método POST que verifica OTP usando un serializador y
# devuelve información de inicio de sesión en una respuesta.
class VerityOTPView(APIView):
    serializer_class = VerifyOTPSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        login_info: dict = serializer.save()
        return Response(login_info,status=200)


# Esta clase de Python representa una vista que devuelve detalles del perfil de usuario usando un serializador y
# requiere autenticación.
class  UserProfileView(APIView):
    """Returns user profile details"""
    permission_classes =  [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, format=None):
        user = self.request.user
        serializer = self.serializer_class(user)
        return Response({"success": True, "data": serializer.data}, status=200)




# La clase `LoginView` es una vista API en Python para manejar el inicio de sesión del usuario con correo electrónico y contraseña.
# incluida la generación de un código QR para la autenticación de dos factores.
class LoginView(APIView):
    """Login with email and password"""

    permission_classes = [AllowAny]
    serializer_class = LoginSerialiazer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user: User = serializer.save()
        return Response(
            {
                "success": True,
                "user": user.id,
                "qr_code": user.qr_code.url,
                "message": "Login Successful. Proceed to 2FA",
            },
            status=200,
        )



# La clase `CreateUserView` en Python define una vista para crear cuentas de usuario con permiso para
# cualquier usuario y un serializador de usuario.
class CreateUserView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "success": True, 
                "message": "Registration Successful!"
            }, 
            status=200
        )