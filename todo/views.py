from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import status

from rest_framework.response import Response
Response

class RegisterView(APIView):
    def post(self,request):
        user_serializer=UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response(status=status.HTTP_201_CREATED)


