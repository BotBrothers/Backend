from rest_framework import serializers
from . import models


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'author_id',
            'recipient_id',
            'text',
            'message_id'
        )
        model = models.Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'user_id',
            'name',
            'surname',
            'user_type'
        )
        model = models.User