from django.contrib import admin
from .models import Department, Student, Subject, Marks

# Register your models here.
admin.site.register(Department)
admin.site.register(Subject)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('std_id', 'std_name', 'std_age', 'department_name')

    def department_name(self, obj):
        return obj.department.dep_name

    # Set columns header in admin
    department_name.short_description = 'Department'

class MarksAdmin(admin.ModelAdmin):
    list_display = ('std_id', 'std_name', 'std_age', 'department_name')

    def department_name(self, obj):
        return obj.department.dep_name

    # Set columns header in admin
    department_name.short_description = 'Department'
    

admin.site.register(Student, StudentAdmin)  # ✅ Register model

class MarksAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks', 'grade', 'student_department')  # Show department
    search_fields = ('student__std_name', 'subject__subject_name', 'student__department__dep_name')  # Search by name and department
    list_filter = ('student__department', 'subject')  # Filter by department and subject

    def student_department(self, obj):
        return obj.student.department.dep_name  # Access department via student

    student_department.short_description = "Department"

admin.site.register(Marks, MarksAdmin)