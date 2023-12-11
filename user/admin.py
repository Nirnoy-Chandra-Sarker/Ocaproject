from django.contrib import admin
from .models import User, Student, Advisor, Admin, StudentProfile

admin.site.index_title  =  "OCA"

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number','role')
    list_filter = ('is_superuser', 'is_staff', 'role')
    search_fields = ('email',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = list_display = ('id','name', 'email', 'phone_number','role')
    search_fields = ('name',)


@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = list_display = ('name', 'email', 'phone_number','role')
    search_fields = ('email',)


@admin.register(Admin)
class Admin(admin.ModelAdmin):
    list_display = list_display = ('name', 'email', 'phone_number','role')
    search_fields = ('email',)

admin.site.register(StudentProfile)

class AdvisorAdminSite(admin.AdminSite):
    site_header = "Advisor Admin Site"


advisor_site = AdvisorAdminSite(name="Advisor Admin Panel")