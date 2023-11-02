from django.shortcuts import render
from .models import Course
from student.models import Review
from django.db.models import Avg
from django.views.generic import DetailView
from django import forms


#for selecting course due to key words
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


# Create your views here.
def home(request):
     return render(request, 'wisdom/home.html', {
        "hello":"Hello"
    })
     
def join(request):
         return render(request, 'wisdom/login.html', {
        "hello":"Hello"
    })
         
def register(request):
         return render(request, 'wisdom/register.html', {
        "hello":"Hello"
    })
         
def about(request):
         return render(request, 'wisdom/about.html', {
        "hello":"Hello"
    })
         
def contact(request):

         return render(request, 'wisdom/contact.html', {
        "hello":"Hello"
    })    
         
def course(request):
    active_courses = Course.objects.filter(is_active=True)

    inactive_courses = Course.objects.filter(is_active=False)
    courses = Course.objects.all()

    for course in inactive_courses:
        total_ratings = Review.objects.filter(course=course).aggregate(Avg('rating'))['rating__avg']
        if total_ratings is not None:
            course.total_ratings = round(total_ratings, 1)
        else:
            course.total_ratings = 0.0 
    

    return render(request, 'wisdom/course.html', {
        "courses":course,
        "active_courses":active_courses,
        "inactive_courses":inactive_courses,
    })


class CourseDetailView(DetailView):
    model = Course
    template_name = 'wisdom/course-details.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the current course
        course = context['course']
        
        # Calculate the total ratings for the current course
        total_ratings = Review.objects.filter(course=course).aggregate(Avg('rating'))['rating__avg']

        # Round the total_ratings to 1 decimal places
        if total_ratings is not None:
            total_ratings = round(total_ratings, 1)
        else:
            total_ratings = 0.0  # No reviews yet

        # Add the total_ratings to the context
        context['total_ratings'] = total_ratings

        # display part of the reviews
        half_review = Review.objects.filter(course=course)[:5]

        context['reviews'] = half_review
        current_course = Course.objects.get(id=course.id)

        return context



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

def add_review(request, course_id):
    course = Course.objects.get(pk=course_id)  # Assuming you have a Course model
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.course = course
            review.save()
            
            # Redirect back to the same course detail page
            return redirect('course-detail', course_id=course_id)
    else:
        form = ReviewForm()
    
    # Render the course details page, including the review form
    return render(request, 'wisdom/course-details.html', {'form': form, 'course': course})
