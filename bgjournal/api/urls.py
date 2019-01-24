from django.urls import path
from .views import UserListView, BoardGameListView, MatchListView

urlpatterns = [
    path('users/', UserListView.as_view(), name="users"),
    path('boardgames/', BoardGameListView.as_view(), name="boardgames"),
    path('matches/', MatchListView.as_view(), name="matches"),
    path('expansions/', ExpansionListView.as_view(), name="expansions"),

]

