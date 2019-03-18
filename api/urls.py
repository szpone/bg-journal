from django.urls import path
from .views import UserListView, BoardGameListView, MatchListView, ExpansionListView, TopThreeListView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('users/', UserListView.as_view(), name="users"),
    path('boardgames/', BoardGameListView.as_view(), name="boardgames"),
    path('matches/', MatchListView.as_view(), name="matches"),
    path('matches/top-three/', TopThreeListView.as_view(), name="top-three"),
    path('expansions/', ExpansionListView.as_view(), name="expansions"),
    path('auth/obtain_token/', obtain_jwt_token),
    path('auth/refresh_token/', refresh_jwt_token),
    path('auth/verify_token/', verify_jwt_token),
]
