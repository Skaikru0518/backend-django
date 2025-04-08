from rest_framework import serializers
from .models import Varos, Bejelentes

class VarosSerializer(serializers.ModelSerializer):
  class Meta:
    model = Varos
    fields = "__all__"

class BejelentesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bejelentes
    fields = '__all__'
    depth = 1