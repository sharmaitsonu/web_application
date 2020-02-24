from django.shortcuts import render,redirect
from web_app.forms import EmployeeForm
from web_app.models import Employee


# Create your views here.

def emp(request):
    if request.method=="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form=EmployeeForm()
    return render(request,"index.html",{'form':form})


def show(request):
    employee= Employee.objects.all()
    return render(request,"show.html",{'employee':employee})

def edit(request,id):
    employee= Employee.objects.get(id=id)
    return render(request,"edit.html",{'employee':employee})

def update(request, id):
    employee= Employee.objects.get(id=id)
    form =EmployeeForm(request.POST,instance=Employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,"edit.html", {'employee':employee})

def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")



