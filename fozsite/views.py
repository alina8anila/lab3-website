from django.shortcuts import render

from fozsite.models import Program


def programs_list(request):
    programs = Program.objects.all()
    return render(
        request,
        "fozsite/programs_list.html",
        {"programs": programs},
    )
