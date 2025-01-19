from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Project import settings
from .views import (HomePage, AboutPage, FeedPage, FeedDetail, FeedCreate,
                    FeedUpdate, FeedDelete, CommentCreate, CommentUpdate,
                    CommentDelete)

urlpatterns = [
    path('',HomePage.as_view(), name='Home'),
    path('about/', AboutPage.as_view(), name='About'),
    path('feed/', FeedPage.as_view(), name='Feed'),
    path('feed/<int:pk>', FeedDetail.as_view(), name='Feed_Detail'),
    path('feed/new', FeedCreate.as_view(), name='Feed_Create'),
    path('feed/<int:pk>/edit', FeedUpdate.as_view(), name='Feed_Update'),
    path('feed/<int:pk>/delete', FeedDelete.as_view(), name='Feed_Delete'),
    path('feed/<int:pk>/comment', CommentCreate.as_view(), name='Comment_Create'),
    path('feed/<int:pk>/comment/update', CommentUpdate.as_view(), name='Comment_Update'),
    path('feed/<int:pk>/comment/delete', CommentDelete.as_view(), name='Comment_Delete')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

