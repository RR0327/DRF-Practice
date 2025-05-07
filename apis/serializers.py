from rest_framework import serializers
from .models import RRModel
from dj_rest_auth.registration.serializers import RegisterSerializer

# Model serializer for RRModel
class RRModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RRModel
        fields = ('id', 'title', 'description')

# Custom user registration serializer
class CustomRegisterSerializer(RegisterSerializer):
    full_name = serializers.CharField(required=True)
    mood = serializers.CharField(required=False)
    motivation = serializers.CharField(required=False)

    def custom_signup(self, request, user):
        user.full_name = self.validated_data.get('full_name', '')
        user.mood = self.validated_data.get('mood', '')
        user.motivation = self.validated_data.get('motivation', '')
        user.save()
