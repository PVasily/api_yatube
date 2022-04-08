from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import (PostViewSet,
                       GroupViewSet,
                       CommentViewSet)


app_name = 'api'

router = DefaultRouter()

router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')
router.register('groups', GroupViewSet)


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token, name='token'),
    path('v1/', include(router.urls))
]
