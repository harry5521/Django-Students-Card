from django.shortcuts import render, HttpResponse
from .models import Department, Student, Subject, Marks
from django.db.models import *
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    # students_all = Student.objects.all()

    search_item = request.GET.get('search', '')

    if search_item:
        students_all = Student.objects.filter(
            Q(std_id__icontains = search_item) |
            Q(std_name__icontains = search_item) |
            Q(department__dep_name__icontains = search_item)
        )
    else:
        students_all = Student.objects.all()
    
    paginator = Paginator(students_all, 20)  # Show 25 contacts per page.
    page_number = request.GET.get("page", 1)
    students = paginator.get_page(page_number)
    # return render(request, "list.html", {"page_obj": page_obj})
    return render(request, 'home.html', {'students': students, 'search_item': search_item})

def about(request):
    return HttpResponse('About page')

def marks(request, std_id):
    marks = Marks.objects.filter(student__std_id = std_id)
    total_marks = Marks.objects.filter(student__std_id = std_id).aggregate(total=Sum('marks'))['total']
    if total_marks:
        total_marks = round(total_marks, 2)
    else:
        total_marks = 0
    return render(request, 'marks.html', context={'marks': marks, 'total_marks': total_marks})
