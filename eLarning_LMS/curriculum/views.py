from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import TemplateView,DetailView,ListView,FormView,CreateView,UpdateView,DeleteView
from curriculum.models import standard,subject,lesson
from curriculum.forms import createLessonForm,commentForm,replyForm
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



    

class lessonDetailView(DetailView, FormView):
    context_object_name = 'lessons'
    model = lesson
    template_name = 'curriculum/lesson_detail_view.html'

    #comment and reply on lessons
    form_class = commentForm
    second_form_class = replyForm
    '''
    send two forms to page-need to add to context
    see which one is posted
    take action on the form which is posted
    '''
    def get_context_data(self,**kwargs):
        context = super(lessonDetailView,self).get_context_data(**kwargs)
        if 'form' not in context :
            #context['form'] =self.form_class(request=self.request)
            context['form'] =self.form_class()
        if 'form2' not in context :
            #context['form2'] =self.second_form_class(request=self.request)
            context['form2'] =self.second_form_class()
        #context['comments'] = comment.objects.filter(id=self.object.id)
        return context

        #post method for comment and reply form
    def post(self, request,*args, **kwargs):
        self.object =self.get_object()
        if 'form' in request.POST:
            #form_class = self.get_form_class()
            form_class = self.form_class
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'
        
        form =self.get_form(form_class)

        if  form_name == 'form' and form.is_valid():
            print("Comment Form is returned")
            return self.form_valid(form)
        elif form_name == 'form2' and form.is_valid():
            print("Reply Form is returned")
            return self.form2_valid(form)

    
    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        subject = self.object.subject
        return reverse_lazy('curriculum:lesson_details',kwargs = {
            'standard': standard.slug,
            'subject' : subject.slug,
            'slug': self.object.slug,
        })
    
    
    def form_valid(self, form):
        self.object =self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.lesson_name = self.object.comments.name
        fm.lesson_name_id = self.object.id 
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    def form2_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.comment_name_id = self.request.POST.get('comment.id')
        fm.save()
        return HttpResponseRedirect(self.get_success_url())




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

class lessonUpdateView(UpdateView):
    fields =('name','position','video','ppt','notes')
    model=lesson
    template_name='curriculum/lesson_update.html'
    context_object_name='lessons'

class lessonDeleteView(DeleteView):
    context_object_name='lessons'
    model=lesson
    template_name='curriculum/lesson_delete.html'

    def get_success_url(self):
        standard=self.object.standard
        subject = self.object.subject
        return reverse_lazy('curriculum:lesson_list',kwargs={'standard':standard.slug,'slug':subject.slug})