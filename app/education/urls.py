
from django.urls import path

from education.views import school_list, school_detail, student_list, student_detail

urlpatterns = [
    path('schools/', school_list, name='school-list'),
    path('schools/<int:school_id>/', school_detail, name='school-detail'),
    path('students/', student_list, name='student-list'),
    path('students/<int:student_id>/', student_detail, name='student-detail'),

]