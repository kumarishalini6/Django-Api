from django.shortcuts import render,HttpResponse , redirect
from .models import Employee
from .forms import EmployeeForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import DataSerialize

# Create your views here.


def index(request):
    return render(request, 'index.html')


def delete(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('showpage')


def edit(request, id):
    emp = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'emp':emp})


def update(request, id):
    emp = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=emp)
    form.save()
    return redirect('showpage')


def show(request):
    employee = Employee.objects.all
    return render(request, 'show.html', {'emp': employee})


def load_form(request):
    form = EmployeeForm(request.POST)
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['email']
        c = request.POST['password']
        d = request.POST['contact_no']
        form.save()
        return render(request, 'result.html')
    else:
        return render(request, 'welcome.html', {'form': form})


def result(request):
    if request.method == 'POST':
        return redirect('showpage')
    else:
        return render(request, 'result.html')


def result(request):
    return redirect('/show')


def search(request):
    model_name = request.POST['name']
    emp = Employee.objects.filter(name=model_name)
    return render(request, 'show.html', {'emp': emp})


@api_view(['GET'])
def data_list(request):
    obj = Employee.objects.all()
    serialize = DataSerialize(obj, many=True)
    return Response(serialize.data)


