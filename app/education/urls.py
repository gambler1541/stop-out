from django.conf.urls import url

from education.views import school_list, school_detail, student_list, student_detail

urlpatterns = [
    url(r'^$', school_list, name='school-list'),
    url(r'^(\d+)/$', school_detail, name='school-detail'),
    url(r'students/', student_list, name='student-list'),
    url(r'/students/(\d+)/$', student_detail, name='student-detail'),

]