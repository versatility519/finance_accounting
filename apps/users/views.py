from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignUpSerializer, SignInSerializer
from rest_framework.authtoken.models import Token

class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User created successfully",
                "user": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SigninView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            # Optionally regenerate the token if it already exists
            if not created:
                token.delete()
                token = Token.objects.create(user=user)

            # return Response({"token": token.key}, status=status.HTTP_200_OK)
            return Response({"message": "User authenticated"}, status=status.HTTP_200_OK)

        else:
            # return Response({"token": token.key}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

