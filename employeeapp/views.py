from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee

# Create your views here.
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')

        if not name or not age:  # Check if fields are filled
            return HttpResponse("Both name and age are required!", status=400)

        try:
            age = int(age)  # Ensure age is an integer
        except ValueError:
            return HttpResponse("Age must be a valid number!", status=400)

        employee = Employee(name=name, age=age)
        employee.save()

        return redirect('list')  # Redirect to the employee list page

    return render(request, 'add.html')  # Render the form if GET request


def list(request):
    employees = Employee.objects.all()  # Fetch all employees from DB
    return render(request, 'list.html', {'employees': employees})  # Render the list of employees
