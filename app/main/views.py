from django.shortcuts import render
from main.models import Teacher, LessonTopic, Lesson,Slide
from django.core.paginator import Paginator

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def topic_list(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    topics = LessonTopic.objects.filter(teacher=teacher)
    return render(request, 'topic_list.html', {'teacher': teacher, 'topics': topics})

def lesson_list(request, topic_id):
    topic = LessonTopic.objects.get(pk=topic_id)
    lessons = Lesson.objects.filter(topic=topic)
    return render(request, 'lesson_list.html', {'topic': topic, 'lessons': lessons})

def lesson_detail(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    topic = lesson.topic
    lesson_list = list(topic.lesson_set.all())
    current_index = lesson_list.index(lesson)
    previous_lesson = lesson_list[current_index - 1] if current_index > 0 else None
    next_lesson = lesson_list[current_index + 1] if current_index < len(lesson_list) - 1 else None
    return render(request, 'lesson_detail.html', {'lesson': lesson, 'previous_lesson': previous_lesson, 'next_lesson': next_lesson})

def slide_list(request, lesson_id):
    page = request.GET.get('page', 1)
    lesson = Lesson.objects.get(pk=lesson_id)
    slides = Slide.objects.filter(lesson=lesson)
    paginator = Paginator(slides, 1)
    # current_page = request.GET.get('page')
    current_page= paginator.page(int(page))



    return render(request, 'slide_list.html', {'lesson': lesson, 'slides': current_page})