
from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken
from exams.views import AssessmentListCreateView,AssessmentRetrieveUpdateDeleteView

urlpatterns = [

    # route to token authentication
    path("assessment/token/",ObtainAuthToken.as_view()),   

    # route to assessment list,create view
    path("assessment/",AssessmentListCreateView.as_view()),

    # route to assessment retrieve,update,delete view
    path("assessment/<int:pk>/",AssessmentRetrieveUpdateDeleteView.as_view()),
]