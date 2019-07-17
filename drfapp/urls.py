from django.conf import path, include
from .views import UserViewSet, GroupViewSet, api_root, ConstituencyViewSet
from rest_framework.urlpatterns import format_suffix_patterns


user_list = UserViewSet.as_view({
'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy'
})


group_list = GroupViewSet.as_view({
    'get': 'list'
})
group_detail = GroupViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy'
})


constituency_list = ConstituencyViewSet.as_view({
    'get': 'list'
})
constituency_detail = ConstituencyViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy'
})


urlpatterns = [
    path('', api_root),
    path('users', user_list, name=user_list),
    path('user/<int:pk>/', user_detail, name=user_detail),
    path('groups', user_list, name=group_list),
    path('groups/<int:pk>/', user_detail, name=group_detail),
    path('constituencies', constituency_list, name=constituency_list),
    path('constituencies/<int:pk>/', constituency_detail, name=constituency_detail)
]  
# Login and logout views for the browsable API
urlpatterns += [
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]