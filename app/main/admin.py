from django.contrib import admin
from main.models import LessonTopic, Teacher,Lesson,Slide
# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_filter = ('category',)
    search_fields = ('name',)

@admin.register(LessonTopic)
class LessonTopicAdmin(admin.ModelAdmin):
    list_display = ('topic',)
    # list_filter = ('category',)
    search_fields = ('topic',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    # list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('content','image')
    # list_filter = ('category',)
    search_fields = ('content','image')