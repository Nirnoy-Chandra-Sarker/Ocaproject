from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .manager import BaseUserManager, StudentManager, AdvisorManager, AdminManager


NAME_LENGTH = 50
EMAIL_LENGTH = 30


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        ADVISOR = "ADVISOR", "Advisor"
        STUDENT = "STUDENT", "Student"
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, default=None)
    photo = models.ImageField(upload_to='profiles/', default='profiles/defaultuserprofile.png')
    base_role = Role.ADMIN
    role = models.CharField(max_length=20, choices=Role.choices)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number']

    objects = BaseUserManager()

    class Meta:
        verbose_name_plural = "All Users"

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.name
    
    def is_advisor(self):
        return True if self.role == 'ADVISOR' else False
    
    def is_student(self):
        return True if self.role == 'STUDENT' else False
            

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        super().save(*args, **kwargs)


class Admin(User):
    base_role = User.Role.ADMIN
    objects = AdminManager()

    class Meta:
        proxy = True

    def __str__(self):
        return self.name


class Student(User):
    base_role = User.Role.STUDENT
    objects = StudentManager()

    class Meta:
        proxy = True

    def __str__(self):
        return self.name


class Advisor(User):
    base_role = User.Role.ADVISOR
    objects = AdvisorManager()

    class Meta:
        proxy = True


class StudentProfile(models.Model):
    class Departments(models.TextChoices):
        CSE = "CSE", "CSE"
        EEE = "EEE", "EEE"
        ECE = "ECE", "ECE"

    class Semesters(models.TextChoices):
        FALL = "FALL", "Fall"
        SPRING = "SPRING", "Spring"
        SUMMER = "SUMMER", "Summer"

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    std_id = models.CharField(max_length=15, null=True, blank=True)
    department = models.CharField(max_length=10, choices=Departments.choices, null=True, blank=True)
    semester = models.CharField(max_length=10, choices=Semesters.choices, null=True, blank=True)
    add_year = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return self.student.name

