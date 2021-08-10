from rest_framework import generics
from rest_framework import status
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response

from .models import (Organization, BoardMembers)
from .serializers import (OrganizationSerializer, BoardMembersSerializer)


# https://www.django-rest-framework.org/api-guide/generic-views/
class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    # authentication_classes = [authentication.JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    # override the create function by changing the response structure
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(
            {
                'status': 'ok',
                'message': 'Organization Added!',
                'data': serializer.data,
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class OrganizationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    # either include a `queryset` attribute, override the `get_queryset()` method
    # def get_queryset(self):
    #     return Organization.objects.filter(id=self.kwargs.get('pk', None))

    # change the response structure for the PUT operation
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        # return Response(serializer.data)
        return Response({'status': 'ok', 'message': 'Organization Updated!', 'data': serializer.data})


# https://www.django-rest-framework.org/api-guide/viewsets/
class BoardMembersViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        # mixins.DestroyModelMixin,
        viewsets.GenericViewSet):
    queryset = BoardMembers.objects.all()
    serializer_class = BoardMembersSerializer

    # override the create function by changing the response structure
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(
            {
                'status': 'ok',
                'message': 'Board Members Added!',
                'data': serializer.data,
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        # return Response(serializer.data)
        return Response({'status': 'ok', 'message': 'Board Members Updated!', 'data': serializer.data})
