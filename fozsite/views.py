from django.shortcuts import render

from fozsite.models import Department, HomePageContent, Program


def programs_list(request):
    programs = Program.objects.all()
    return render(
        request,
        "programs_list.html",
        {"programs": programs},
    )


def departments_list(request):
    departments = Department.objects.all()
    return render(
        request,
        "departments_list.html",
        {"departments": departments},
    )


def home(request):
    homepage_text = HomePageContent.objects.first()
    return render(request, "home.html", {"content": homepage_text})
