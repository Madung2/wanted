from django.urls import path
from . import views
urlpatterns = [
    path('', views.RecruitmentView.as_view()),
    path('<int:pk>/', views.MyRecruitmentView.as_view()),
    path('search/', views.SearchView.as_view()),
    path('recruiting/', views.RecruitingView.as_view()),
]
