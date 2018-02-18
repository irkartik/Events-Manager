from .models import User, Event
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'email', 'phone', 'created_date')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'name', 'unique_code', 'barcode', 'description', 'price', 'organized_by', 'date', 'time', 'picture', 'location', 'created_on', 'updated_on')




