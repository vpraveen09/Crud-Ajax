from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Student
from .forms import StudentForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth import logout

def custom_logout(request):
    logout(request)
    return redirect('login')



def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/index')
            else:
                form.add_error(None, "Invalid username or password")

    return render(request, 'login.html', {'form': form})  



def index(request):
    students = Student.objects.all()  # Query all students from the database
    return render(request, 'index.html', {'students': students})

def get_students(request):
    students = Student.objects.all().values('id', 'name', 'email', 'password')
    return JsonResponse(list(students), safe=False)

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            # Return detailed error messages
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = StudentForm()
    
    return render(request, 'add.html', {'form': form})


def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'edit.html', {'student': student})

@require_POST


def update_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=student_id)
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.password = request.POST.get('password')
        student.save()
        
        # Check if the request is AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})
        
        # Redirect to index page if it's a standard POST request
        return redirect('myapp:index')
    
    # If method is not POST, return error or handle it accordingly
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

    

@csrf_exempt
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return JsonResponse({'message': 'Student deleted successfully.'})
    else:
        return JsonResponse({'error': 'POST method required.'}, status=405)

def get_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    data = {
        'id': student.id,
        'name': student.name,
        'email': student.email,
        'password': student.password
    }
    return JsonResponse(data)
