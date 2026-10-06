from django.urls import path

from fgn import views

urlpatterns = [
    path("", views.home, name="home"),
    path("programs/", views.programs_list, name="programs_list"),
    path("programs/<int:pk>/", views.program_detail, name="program_detail"),
    path("departments/", views.departments_list, name="departments_list"),
    path(
        "departments/<int:pk>/",
        views.department_detail,
        name="department_detail",
    ),
    path("exchange/", views.exchange, name="exchange"),
]
