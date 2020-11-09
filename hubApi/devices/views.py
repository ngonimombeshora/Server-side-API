from devices.models import Device
from devices.serializers import DeviceSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from devices.permissions import IsOwnerOrReadOnly


class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# @api_view(['GET', 'POST'])
# def device_list(request, format=None):
#     """
#     List all devices, or create a new device.
#     """
#     if request.method == 'GET':
#         devices = Device.objects.all()
#         serializer = DeviceSerializer(devices, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = DeviceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def device_detail(request, pk, format=None):  # ToDo change from pk to name and test
#     """
#     Retrieve, update or delete a `device`.
#     """
#     try:
#         device = Device.objects.get(pk=pk)
#     except Device.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = DeviceSerializer(device)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = DeviceSerializer(device, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         device.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
