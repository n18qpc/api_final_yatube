from django_filters.rest_framework import CharFilter, DateFilter, FilterSet

from .models import Follow, Post


class PostFilter(FilterSet):
    date_from = DateFilter(
        field_name='pub_date', lookup_expr='gte')
    date_to = DateFilter(
        field_name='pub_date', lookup_expr='lte')

    class Meta:
        model = Post
        fields = ['date_from', 'date_to']


class FollowFilter(FilterSet):
    user = CharFilter(
        field_name='user__username',
        lookup_expr='exact'
    )
    following = CharFilter(
        field_name='following__username',
        lookup_expr='exact'
    )

    class Meta:
        model = Follow
        fields = ['user', 'following']
