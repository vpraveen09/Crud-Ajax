from django.urls import path
from .views import login_view
from django.contrib.auth import views as auth_views
from . import views

app_name = 'myapp' 

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    
    path('index/', views.index, name='index'),
    path('get-students/', views.get_students, name='get_students'),
     path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('add/', views.add_student, name='add_student'),
    path('update-student/<int:student_id>/', views.update_student, name='update_student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('get-student/<int:student_id>/', views.get_student, name='get_student'),
    
   
]