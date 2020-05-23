from rest_framework import serializers

from .models import Entrepreneur
class EntrepreneurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entrepreneur
        fields = ('first_name', 'email_id', 'password')