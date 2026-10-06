from django.shortcuts import get_object_or_404, render

from fgn.models import Department, ExchangeProgram, HomePageContent, Program


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


def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, "program_detail.html", {"program": program})


def department_detail(request, pk):
    department = get_object_or_404(
        Department,
        pk=pk,
    )
    return render(request, "department_detail.html", {"department": department})


def exchange(request):
    programs = ExchangeProgram.objects.all()
    return render(
        request,
        "exchange.html",
        {"programs": programs},
    )
