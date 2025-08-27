from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("student/", views.IndexView.as_view(), name="student_list"),
    path("professor/", views.ProfessorView.as_view(), name="professor_list"),
    path("course/", views.CourseView.as_view(), name="course_list"),
    path("faculty/", views.FacultyView.as_view(), name="faculty_list"),
    path("create/", views.CreateStudent.as_view(), name="create"),
]