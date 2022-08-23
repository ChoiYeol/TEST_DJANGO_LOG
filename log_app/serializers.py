from rest_framework import serializers
from .models import (QuickSeqs)

class QuickSeqs(serializers.ModelSerializer):
    class Meta:
        model = QuickSeqs
        fields = "__all__"

class Users(serializers.ModelSerializer):
    class Meta:
        model = QuickSeqs
        fields = "__all__"

