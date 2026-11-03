
from django.urls import path

from accounts.views import AdminCreateView,StudentCreateView
from accounts.views import StudentProfileCompleteView,StudentProfileGetView

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [

    # route to admin register view
    path("admin/register/",AdminCreateView.as_view()),

    # route to student register view
    path("student/register/",StudentCreateView.as_view()),

    # route to create jwt token
    path("jwt/token/",TokenObtainPairView.as_view()),

    # route to refresh jwt token
    path("jwt/token/refresh/",TokenRefreshView.as_view()),

    # route to profile update
    path("profile/complete/",StudentProfileCompleteView.as_view()),

    # route to profile retrieve
    path("profile/get/me/",StudentProfileGetView.as_view()),
]