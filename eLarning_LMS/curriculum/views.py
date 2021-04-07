from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,ListView,FormView
from curriculum.models import standard,subject,lesson

class standardListView(ListView):
    context_object_name = 'standards'
    model = standard 
    template_name = 'curriculum/standards_list_view.html'

class subjectListView(DetailView):
    context_object_name='standards'
    model=standard
    template_name='curriculum/subject_list_view.html'
