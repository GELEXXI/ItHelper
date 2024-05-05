from django.urls import path


from main import views

app_name = 'main'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('teachers/', views.teacher_list, name='teacher_list'),
    path('', views.teacher_list, name='index'),
    path('topics/<int:teacher_id>/', views.topic_list, name='topic_list'),
    path('lessons/<int:topic_id>/', views.lesson_list, name='lesson_list'),
    path('lessons/slides/<int:lesson_id>/', views.slide_list, name='slide_list'),
    # path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
   
]
