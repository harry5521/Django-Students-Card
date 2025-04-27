from django.db import models

# Create your models here.
class Department(models.Model):
    dep_id = models.CharField(max_length=10, unique=True, null=False)
    dep_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.dep_id} {self.dep_name}'
    
class Student(models.Model):
    department = models.ForeignKey(Department, related_name='students', on_delete=models.CASCADE)
    std_id = models.CharField(max_length=20, unique=True, null=False)
    std_name = models.CharField(max_length=100, null=False)
    std_age = models.IntegerField(null=False)

    def __str__(self):
        return self.std_name
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.subject_name

class Marks(models.Model):
    student = models.ForeignKey(Student, related_name='Student', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='Subject', on_delete=models.CASCADE)
    marks = models.FloatField()
    grade = models.CharField(max_length=2)

    def save(self, *args, **kwargs):
        self.marks = round(self.marks, 2)  # Always round before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.std_name} - {self.subject.subject_name}: {self.marks} ({self.grade})"
    
    class Meta:
        unique_together = ('student', 'subject')

