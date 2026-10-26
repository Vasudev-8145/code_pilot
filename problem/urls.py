
from django.urls import path

from problem.views import QuestionCreateView,QuestionRetriveupdateDeleteView

urlpatterns = [

    # route to question create view
    path("assessment/<int:pk>/question/",QuestionCreateView.as_view()),

    # route to question retrieve,update,delete view
    path("question/<int:pk>/",QuestionRetriveupdateDeleteView.as_view()),
]