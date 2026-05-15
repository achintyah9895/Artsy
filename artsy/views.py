from django.contrib.auth import authenticate
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import  RefreshToken
from rest_framework.views import APIView
from .models import *
from .serializers import *


class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterUserAccount(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "User created"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({ "refresh": str(refresh),"access": str(refresh.access_token)})

        return Response({"Message": "Invalid data"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token_refresh = request.data['refresh']
        if  token_refresh:
            token = RefreshToken(token_refresh)
            token.blacklist()
            return Response({"message": "Logged out successfully"})

        return Response({"error": "Refresh token required"}, status=400)

class BidView(CreateAPIView):
    serializer_class = BidSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        bid = serializer.save(bidder=self.request.user)
        art = bid.art
        art.price = bid.bid_amount
        art.save()


class ArtsyViewSet(ModelViewSet):
        serializer_class = ArtSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]

        def get_queryset(self):
            return Art.objects.filter().order_by('-id')

        def perform_create(self, serializer):
            serializer.save(user=self.request.user)

        @action(detail=False, permission_classes=[IsAuthenticated])
        def my_art(self, request):
            art = Art.objects.filter(user=request.user)
            serializer = self.get_serializer(art, many=True)
            return Response(serializer.data)
