from rest_framework import serializers
from devices.models import Device
from django.contrib.auth.models import User

# id = serializers.IntegerField(read_only=True)
# name = serializers.CharField(required=False, allow_blank=True, max_length=100)
# category = serializers.CharField(required=False, allow_blank=True, max_length=100)
# location = serializers.CharField(required=False, allow_blank=True, max_length=100)
# device_id = serializers.CharField(required=False, allow_blank=True, max_length=100)


class DeviceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Device
        fields = ('id', 'name', 'category', 'location',
                  'status','reading','created', 'owner')

# Because 'snippets' is a reverse relationship on the User model, it will not be included by default
#  when using the ModelSerializer class, so we needed to add an explicit field for it.


class UserSerializer(serializers.ModelSerializer):
    devices = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Device.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'devices']
