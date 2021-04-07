from django.urls import path
from curriculum import views
from django.conf.urls.static import static


app_name = 'curriculum'
urlpatterns = [
    path('',views.standardListView.as_view(),name='standard_list'),
    path('<slug:slug>/',views.subjectListView.as_view(),name='subject_list'),
    path('<str:standard>/<slug:slug>/', views.lessonListView.as_view(),name='lesson_list'),
    path('<str:standard>/<slug:slug>/create/',views.lessonCreateView.as_view(),name='lesson_create'),
    path('<str:standard>/<str:subject>/<slug:slug>/',views.lessonDetailView.as_view(),name='lesson_details'),
    path('<str:standard>/<str:subject>/<slug:slug>/update/',views.lessonUpdateView.as_view(),name='lesson_update'),
    path('<str:standard>/<str:subject>/<slug:slug>/delete/',views.lessonDeleteView.as_view(),name='lesson_delete'),

    
]
