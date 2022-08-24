from django.urls import path
from . import views
urlpatterns = [
    path('', views.RecruitmentView.as_view()),
    path('<int:pk>/', views.MyRecruitmentView.as_view()),
]
