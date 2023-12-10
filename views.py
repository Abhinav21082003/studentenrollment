from django.shortcuts import render

from .forms import SSForm, StudForm,SForm
from .models import stud
# Create your views here.
def show(request):
    return render(request,"home.html ")
def register(request):
    title="Student Registration"
    form = StudForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        clas=form.cleaned_data['s_class']
        addr =form.cleaned_data['s_addr']
        school=form.cleaned_data['s_school']
        mail=form.cleaned_data['s_email']

        p=stud(s_name=name,s_class=clas,s_addr=addr,s_school=school,s_email=mail)   
        p.save() 
        return render(request,'ack.html',{"title":"Registered Successfully"})
    context={
        "title":title,
        "form":form,
    }
    return render(request,'register.html',context)
def existing(request):
    title="All Registered Students"
    queryset = stud.objects.all()

    context={
        "title":title,
        "queryset":queryset,
    }
    return render(request,'existing.html',context) 
def search(request):
    title = "Search Student"
    form = SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['s_name']
        # nam = stud.objects.filter(s_name=name)
        # filter used for searching based on condition
        queryset=stud.objects.filter(s_name=name)
        context={
            "title":title,
            "queryset":queryset,
        }
        return render(request,'existing.html',context)
    context={
    "title":title,
    "form":form   
          }
    return render(request,'search.html',context)

def delete_student(request):
    title = "Delete Student info by name"
    form = SSForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['s_name']
        # Get the queryset for the selected student(s)
        queryset = stud.objects.filter(s_name=name)

        # Check if any matching records were found
        if queryset.exists():
            # Delete the matching records
            queryset.delete()

            # Redirect to a success page or any other desired page
            # return redirect('')  # Replace 'success_page' with your actual success page name
        else:
            # If no matching records were found, display an appropriate message
            context = {
                "title": title,
                "form": form,
                # "error_message": "No records found for the specified name.",
            }
            return render(request, 'ack.html', context)

    context = {
        "title": title,
        "form": form,
    }
    return render(request, 'delete.html', context)
