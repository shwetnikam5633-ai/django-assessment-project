from django.shortcuts import render, get_object_or_404
from .models import Course, Submission

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # Logic to evaluate the exam, calculate score, and save Submission goes here
    # After grading, it redirects or renders the result:
    return render(request, 'onlinecourse/exam_result_bootstrap.html', {
        'course': course,
        # include score and question context here
    })

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    return render(request, 'onlinecourse/exam_result_bootstrap.html', {
        'course': course,
        'submission': submission,
    })
