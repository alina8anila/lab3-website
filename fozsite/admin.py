from django.contrib import admin

from fozsite.models import Department, HomePageContent, Program, Teacher

# Register your models here.


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "head")
    search_fields = ("name", "head")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "degree", "department")
    search_fields = ("name", "position", "degree", "department")
    list_filter = ("degree", "department")


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "department", "coordinator_name")
    list_filter = ("department",)
    search_fields = ("name", "code", "coordinator_name")


@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_at")
