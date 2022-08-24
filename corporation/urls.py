from django.urls import path

urlpatterns = [
    path('', views.RecruitmentView.as_view()),
]
