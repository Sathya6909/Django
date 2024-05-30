from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny

class HelloWorldisView(APIView):
    def get(self, request):
        permission_classes = [IsAuthenticated]
        return Response({"message": "Hello, world!"})
    
    def post(self, request, *args, **kwargs):
        # Get the JSON data from the request
        json_data = request.data
        
        # Return a response
        return Response({"message": "JSON received", "data": json_data}, status=status.HTTP_200_OK)
    



class CreateUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
