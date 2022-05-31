from django.urls import path
from .views import (ActivityView, CreateRoom, DeleteMessage, 
                    DeleteRoom, HelpfulView, JoinRoomView, LeaveRoomView, NothelpfulView,
                    UpdateRoom, home, rooms, TopicView, UploadMessageView
                    )


urlpatterns = [
    path("", home, name="home"),
    path("room/<str:pk>/", rooms, name="room"),
    path("join/<str:pk>/", JoinRoomView, name="join"),
    path("leave/<str:pk>/", LeaveRoomView, name="leave"),
    path("create-room/", CreateRoom, name="create-room"),
    path("update-room/<str:pk>/", UpdateRoom, name="update-room"),
    path("delete-room/<str:pk>/", DeleteRoom, name="delete-room"),
    path("delete-message/<str:pk>/", DeleteMessage, name="delete-message"),
    path("topics/", TopicView, name="topics"),
    path("activites/", ActivityView, name="activities"),
    path("helpful/<str:pk>/<str:room>/", HelpfulView, name="helpful"),
    path("nothelpful/<str:pk>/<str:room>/", NothelpfulView, name="not-helpful"),
    path("message-body/<str:pk>/", UploadMessageView, name="message"),
]
