from SpaceApp.models import MsgFromSpace
from rest_framework import serializers


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MsgFromSpace
        fields = ('date', 'text', 'read')
