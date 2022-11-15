from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import *
from main.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # view sets n routers url
    path('api/v1/', include(router.urls)),

    # default drf auth
    path('api/v1/drf-auth/', include('rest_framework.urls')),

    #
    # path('api/v1/articlelist/', ArticleAPIView.as_view()),
    # path('api/v1/articlelist/<int:pk>/', ArticleUpdateAPIView.as_view()),
    # path('api/v1/articledelete/<int:pk>/', ArticleDeleteAPIView.as_view()),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
