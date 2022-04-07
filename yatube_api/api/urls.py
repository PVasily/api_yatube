from django.urls import include, path

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import (PostViewSet,
                       GroupViewSet,
                       CommentViewSet)


app_name = 'api'

router = DefaultRouter()

router.register('v1/posts', PostViewSet)
router.register(r'v1/posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')
router.register('v1/groups', GroupViewSet)


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token, name='token'),
    path('', include(router.urls))
]
