
from django.urls import path

from evaluation.views import SubmissionStartView,AnswerCreateView
from evaluation.views import SubmissionRetrieveView
from evaluation.views import AnswerUpdateView

urlpatterns = [

    # route to submission start view
    path("assessment/<int:pk>/submission/",SubmissionStartView.as_view()),

    # route to answer create view
    path("submission/<int:pk>/answer/",AnswerCreateView.as_view()),

    # route to submission retrieve view
    path("submission/<int:pk>/",SubmissionRetrieveView.as_view()),

    # route to answer update view
    path("answer/<int:pk>/",AnswerUpdateView.as_view()),
]