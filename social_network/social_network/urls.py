"""
URL configuration for social_network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views
from core.views import CustomAuthToken, register
from django.conf import settings
from django.conf.urls.static import static



router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'discussions', views.DiscussionViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'hashtags', views.HashtagViewSet)
router.register(r'likes', views.LikeViewSet)
router.register(r'follows', views.FollowViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/search/users/', views.SearchUserView.as_view(), name='search-users'),
    path('api/search/discussions/text/', views.SearchDiscussionByTextView.as_view(), name='search-discussions-text'),
    path('api/search/discussions/hashtags/', views.SearchDiscussionByHashtagView.as_view(), name='search-discussions-hashtags'),
    path('api/login/', CustomAuthToken.as_view(), name='login'),
    path('api/register/', register, name='register'),
    
]

#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
