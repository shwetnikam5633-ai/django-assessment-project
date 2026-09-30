from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Other paths...
    path('/submit/', views.submit, name='submit'),
    path('/submission//', views.show_exam_result, name='show_exam_result'),
]
