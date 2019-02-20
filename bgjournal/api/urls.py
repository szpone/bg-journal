from django.urls import path
from .views import UserListView, BoardGameListView, MatchListView, ExpansionListView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('users/', UserListView.as_view(), name="users"),
    path('boardgames/', BoardGameListView.as_view(), name="boardgames"),
    path('matches/', MatchListView.as_view(), name="matches"),
    path('expansions/', ExpansionListView.as_view(), name="expansions"),
    path('auth/obtain_token/', obtain_jwt_token),
    path('auth/refresh_token/', refresh_jwt_token),
    path('auth/verify_token/', verify_jwt_token),

]

