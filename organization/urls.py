from django.urls import path
from rest_framework import routers

from . import views

# https://docs.djangoproject.com/en/3.2/intro/tutorial03/#namespacing-url-names
app_name = 'organization'

urlpatterns = [
    path('', views.OrganizationListCreateAPIView.as_view(), name='organization-list'),
    path('<int:pk>/', views.OrganizationRetrieveUpdateDestroyAPIView.as_view(),
         name='organization-detail'),
]

router = routers.SimpleRouter()
router.register('board-members', views.BoardMembersViewSet)
urlpatterns += router.urls
