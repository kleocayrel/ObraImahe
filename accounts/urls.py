from django.urls import path
from .views import SignUp
from .views import ProfileDetailView, ProfileUpdateView, ProfileDeleteView

urlpatterns = [
    path('signup/', SignUp.as_view(), name='Signup'),
    path('profile/', ProfileDetailView.as_view(), name='Profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='Profile_update'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='Profile_delete'),
]