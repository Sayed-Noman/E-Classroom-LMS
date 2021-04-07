from django.urls import path
from curriculum import views
from django.conf.urls.static import static


app_name = 'curriculum'
urlpatterns = [
    path('',views.standardListView.as_view(),name='standard_list'),
    path('<slug:slug>/',views.subjectListView.as_view(),name='subject_list'),
]
