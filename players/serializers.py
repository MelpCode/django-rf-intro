from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
  substitute = serializers.BooleanField()
  class Meta:
    model = Player
    fields = ('id','fullname','age','height','substitute','country','price','created_at')
    read_only_fields = ('created_at', )