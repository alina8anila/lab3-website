from django.shortcuts import render

from fozsite.models import Department, HomePageContent, Program


def programs_list(request):
    programs = Program.objects.all()
    return render(
        request,
        "fozsite/programs_list.html",
        {"programs": programs},
    )


def departments_list(request):
    departments = Department.objects.all()
    return render(
        request,
        "fozsite/departments_list.html",
        {"departments": departments},
    )


def home(request):
    homepage_text = HomePageContent.objects.first()
    return render(request, "fozsite/home.html", {"content": homepage_text})
