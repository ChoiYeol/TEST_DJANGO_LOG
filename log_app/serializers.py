from rest_framework import serializers
from .models import (QuickSeqs)


class QuickSeqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuickSeqs
        # fields = "__all__"
        exclude = ( 'createdat', "updatedat", "deletedat")
    # def create(self, validated_data):
    #      return QuickSeqs(**validated_data)


        # def create(self, validated_data):
        #     user = get_user_model().objects.create_user(
        #     validated_data["username"], None, validated_data["password"], uuids=validated_data["uuids"]
        # )
        # return user


# class QuickSeqs(serializers.Serializer):
    
#     index = serializers.IntegerField()
#     fk_quick_id = serializers.IntegerField()
#     createdat = serializers.DateTimeField()  # Field name made lowercase.
#     updatedat = serializers.DateTimeField()  # Field name made lowercase.

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return QuickSeqs.objects.create(**validated_data)
#         # class Meta:
#         # model = QuickSeqs
#         # fields = "__all__"

class Users(serializers.ModelSerializer):
    class Meta:
        model = QuickSeqs
        fields = "__all__"

