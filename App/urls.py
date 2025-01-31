from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Project import settings
from .views import (HomePage, AboutPage, FeedPage, FeedDetail, FeedCreate,
                    FeedUpdate, FeedDelete, CommentCreate, CommentUpdate,
                    CommentDelete, ReplyCreate)

urlpatterns = [
    path('',HomePage.as_view(), name='Home'),
    path('about/', AboutPage.as_view(), name='About'),
    path('feed/', FeedPage.as_view(), name='Feed'),
    path('feed/<int:pk>', FeedDetail.as_view(), name='Feed_Detail'),
    path('feed/new', FeedCreate.as_view(), name='Feed_Create'),
    path('feed/<int:pk>/edit', FeedUpdate.as_view(), name='Feed_Update'),
    path('feed/<int:pk>/delete', FeedDelete.as_view(), name='Feed_Delete'),
    path('feed/<int:pk>/comment', CommentCreate.as_view(), name='Comment_Create'),
    path('feed/<int:post_pk>/comment/<int:pk>/update', CommentUpdate.as_view(),name='Comment_Update'),
    path('feed/<int:post_pk>/comment/<int:pk>/delete', CommentDelete.as_view(), name='Comment_Delete'),
    path('post/<int:pk>/comment/<int:comment_id>/reply/', ReplyCreate.as_view(), name='Reply_Create'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

