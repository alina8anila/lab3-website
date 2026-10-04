from django.urls import path

from fozsite import views

urlpatterns = [
    # path('', views.home, name='home'),
    path("programs/", views.programs_list, name="programs_list")
    # path('/programs/<int:program_id>/', views.program_details, name='program_details')
    # path('departments/', views.departments_list, name='departments_list')
    # path('/departments/<int:departament_id>/', views.department_details, name='department_details')
]
