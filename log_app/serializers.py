from rest_framework import serializers
from .models import (QuickSeqs)


# class QuickSeqsSerializer(serializers.Serializer):
#     class Meta:
#         model = QuickSeqs
#         fields = "__all__"
#         exclude = ( 'createdat', "updatedat", "deletedat")

#     def create(self, validated_data):  
#         return QuickSeqs.objects.create(**validated_data) 

#     def update(self, instance, validated_data): 
#         instance.fk_quick_id = validated_data.get('fk_quick_id', instance.author)
#         instance.save()
#         return instance

class QuickSeqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuickSeqs
        fields = "__all__"
        exclude = ( 'createdat', "updatedat", "deletedat")
 

class Users(serializers.ModelSerializer):
    class Meta:
        model = QuickSeqs
        fields = "__all__"

