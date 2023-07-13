from rest_framework import viewsets,generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, LoginSerializer,RideSerializer, RideStatusUpdateSerializer
from .models import Ride




class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer
   

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': 'Login successful'})
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
       
class CreateRideView(generics.CreateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

class RideDetailView(generics.RetrieveAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

class ListRidesView(generics.ListAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

class UpdateRideStatusView(generics.UpdateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideStatusUpdateSerializer
