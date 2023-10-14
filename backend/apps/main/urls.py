from django.urls import path
from main.views.group import GroupApiView
from main.views.student import StudentApiView
from main.views.sciences import ScienceApiView
from main.views.lessons import LessonApiView
from main.views.question import QuestionApiView
from main.views.option import OptionApiView
from main.views.control import ControlApiView
from main.views.answer import AnswerApiView

urlpatterns = [
    path("science/", ScienceApiView.as_view()),
    path("student/", StudentApiView.as_view()),
    path("group/", GroupApiView.as_view()),
    path("lessons/", LessonApiView.as_view()),
    path("question/", QuestionApiView.as_view()),
    path("option/", OptionApiView.as_view()),
    path("control/", ControlApiView.as_view()),
    path("answer/", AnswerApiView.as_view()),
]