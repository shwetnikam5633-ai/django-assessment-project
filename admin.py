
from django.contrib import admin
from .models import Question, Choice, Submission, Lesson

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('id', 'question_text', 'pub_date')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Submission)
