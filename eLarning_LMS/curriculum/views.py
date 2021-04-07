from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import TemplateView,DetailView,ListView,FormView,CreateView,UpdateView,DeleteView
from curriculum.models import standard,subject,lesson
from curriculum.forms import createLessonForm
from django.urls import reverse_lazy
class standardListView(ListView):
    context_object_name = 'standards'
    model = standard 
    template_name = 'curriculum/standards_list_view.html'

class subjectListView(DetailView):
    context_object_name='standards'
    model=standard
    template_name='curriculum/subject_list_view.html'

class lessonListView(DetailView):
    context_object_name = 'subjects'
    model= subject
    template_name = 'curriculum/lesson_list_view.html'

class lessonDetailView(DetailView):
    context_object_name = 'lessons'
    model = lesson
    template_name = 'curriculum/lesson_detail_view.html'

class lessonCreateView(CreateView):
    form_class= createLessonForm
    context_object_name = 'subjects'
    model= subject
    template_name ='curriculum/lesson_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('curriculum:lesson_list',kwargs={
            'standard' : standard.slug,'slug':self.object.slug})



    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit = False)
        fm.created_by = self.request.user
        fm.standard = self.object.standard
        fm.subject = self.object
        fm.save()

        return HttpResponseRedirect(self.get_success_url())