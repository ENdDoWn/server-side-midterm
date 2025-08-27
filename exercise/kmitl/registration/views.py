from django.shortcuts import redirect, render
from django.views import View
from django.db.models import Count

# Create your views here.
from .models import *

class IndexView(View):

    def get(self, request):
        filter = request.GET.get("filter")
        search = request.GET.get("search")
        if filter == "email":
            data = Student.objects.filter(studentprofile__email__icontains=search)
        elif filter == "faculty":
            data = Student.objects.filter(faculty__name__icontains=search)
        elif filter == "fullname":
            data = Student.objects.filter(first_name__icontains=search)
        else:
            data = Student.objects.all()
        context = {"student_list": data,
                   "filter": filter,
                   "search": search
        }
        return render(request, "index.html", context)

class ProfessorView(View):

    def get(self, request):
        filter = request.GET.get("filter")
        search = request.GET.get("search")
        if filter == "faculty":
            data = Professor.objects.filter(faculty__name__icontains=search)
        elif filter == "fullname":
            data = Professor.objects.filter(first_name__icontains=search)
        else:
            data = Professor.objects.all()
        context = {"professor_list": data,
                   "filter": filter,
                   "search": search
        }
        return render(request, "professor.html", context)

class CourseView(View):

    def get(self, request):
        search = request.GET.get("search")
        if search:
            data = Course.objects.filter(course_name__icontains=search)
        else:
            data = Course.objects.all()
        context = {"course_list": data,
                   "search": search
        }
        return render(request, "course.html", context)

class FacultyView(View):
    
    def get(self, request):
        search = request.GET.get("search")
        if search:
            data = Faculty.objects.filter(name__icontains=search)
        else:
            data = Faculty.objects.all()
        context = {"faculty_list": data,
                   "search": search
        }
        return render(request, "faculty.html", context)

class CreateStudent(View):
    
    def get(self, request):
        data = Faculty.objects.all()
        sec = Section.objects.all()
        context = {"faculties": data, "sections": sec}
        return render(request, "create_student.html", context)

    def post(self, request):
        if request.method == "POST":
            fac_name = request.POST.get("faculty")
            fac = Faculty.objects.get(name=fac_name)
            code = request.POST.getlist("section_ids")
            print(code)
            stu_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            phone_number = request.POST.get("phone_number")
            address = request.POST.get("address")
            student_id = request.POST.get("student_id")

            stu = Student.objects.create(
                student_id = student_id,
                first_name = stu_name,
                last_name = last_name,
                faculty = fac,
            )
            stu.enrolled_sections.set(code)

            StudentProfile.objects.create(
                student = stu,
                email = email,
                phone_number = phone_number,
                address = address
            )
            return redirect('student_list')
