from django.urls import path
from devices import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url

schema_view = get_swagger_view(title='Home hub API Documentation')

urlpatterns = [
    url(r'^$', schema_view)
]


urlpatterns = [
    path('devices/', views.DeviceList.as_view()),
    path('documentation/', schema_view),
    path('devices/<int:pk>/', views.DeviceDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
