from xml.dom.minidom import Document
from django.urls import path
from .views import ( LoginView, LogoutView, ProfileView, RegisterView,
 ProfileUpdateView,)
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('register/', RegisterView, name="register"),
    path('login/', LoginView, name="login"),
    path('logout/', LogoutView, name="logout"),
    path("profile-update/",ProfileUpdateView, name="profileupdate"),
    path('<str:name>/', ProfileView, name="profile"),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)