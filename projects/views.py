from django.shortcuts import render

from projects.models import Project

# Create your views here.
def all_projects(request):
    # query db to return all project objects
    projects_records = Project.objects.all()
    print(projects_records[0].title)
    return render(request, 'projects/all_projects.html', {'projects': projects_records})

