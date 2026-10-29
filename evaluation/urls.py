
from django.urls import path

from evaluation.views import SubmissionStartView,AnswerCreateView
from evaluation.views import SubmissionRetrieveView

urlpatterns = [

    # route to submission start view
    path("assessment/<int:pk>/submission/",SubmissionStartView.as_view()),

    # route to answer create view
    path("submission/<int:pk>/answer/",AnswerCreateView.as_view()),

    # route to submission retrieve view
    path("submission/<int:pk>/",SubmissionRetrieveView.as_view()),
]