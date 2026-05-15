
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .models import Art, Bid


class ArtSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Art
        fields = ['id', 'user', 'user_name', 'item_name','item_description', 'image', 'price','category']



class RegisterUserAccount(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



class BidSerializer(serializers.ModelSerializer):
    bidder_name = serializers.ReadOnlyField(source='bidder.username')
    class Meta:
        model = Bid
        fields = ['id', 'art', 'bidder', 'bidder_name', 'bid_amount', 'timestamp']

    def validate(self, data):
        art = data['art']
        bid_amount = data['bid_amount']
        user = self.context['request'].user

        if art.user == user:
            raise serializers.ValidationError("You cannot bid on your own art.")

        if bid_amount <= art.price:
            raise serializers.ValidationError(f"Bid must be higher than the current price: {art.price}")
        return data



