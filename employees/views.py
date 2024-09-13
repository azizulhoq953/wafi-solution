from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm
from django.core.paginator import Paginator
from django.db.models import Q

def employee_list(request):
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort_by', 'first_name')

    # Filter by first name, email, mobile, and date_of_birth
    employees = Employee.objects.filter(
        Q(first_name__icontains=search_query) |
        Q(last_name__icontains=search_query) |
        Q(email__icontains=search_query) |
        Q(mobile__icontains=search_query) |
        Q(date_of_birth__icontains=search_query)  # assuming date_of_birth is in string format like 'YYYY-MM-DD'
    ).order_by(sort_by)

    paginator = Paginator(employees, 10)  # 10 employees per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employees/employee_list.html', {'page_obj': page_obj, 'sort_by': sort_by})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/edit_employee.html', {'form': form})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/delete_employee.html', {'employee': employee})
