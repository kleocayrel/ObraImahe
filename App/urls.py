from django.urls import path
from .views import (HomePage, AboutPage, FeedPage, FeedDetail, FeedCreate,
                    FeedUpdate, FeedDelete)

urlpatterns = [
    path('',HomePage.as_view(), name='Home'),
    path('about/', AboutPage.as_view(), name='About'),
    path('feed/', FeedPage.as_view(), name='Feed'),
    path('feed/<int:pk>', FeedDetail.as_view(), name='Feed/Detail'),
    path('feed/new', FeedCreate.as_view(), name='Feed_Create'),
    path('feed/<int:pk>/edit', FeedUpdate.as_view(), name='Feed_Update'),
    path('feed/<int:pk>/delete', FeedDelete.as_view(), name='Feed_Delete'),
]

