from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import CommentView, FollowView, GroupView, PostView

router = DefaultRouter()
router.register('posts', PostView, basename='posts')
router.register('group', GroupView, basename='group')
router.register('follow', FollowView, basename='follow')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentView,
                basename="comments")

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
