from django.shortcuts import render
from .models import Course  
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage
from django.shortcuts import render, get_object_or_404




## Home Page View
    
def home(request):
    courses = Course.objects.all()
    tagline = "Learn the Holy Quran Online Anytime, Anywhere"
    # You can send context data like courses, hero text later.
    context = {
        'site_name': 'AR Online Quran Academy',
        'tagline': 'Learn the Holy Quran Online Anytime, Anywhere',
    }
    return render(request, 'main/home.html', {'courses': courses, 'tagline': tagline})

def about(request):
    return render(request, 'main/about.html')

# def courses(request):
#     return render(request, 'main/courses.html')

def contact(request):
    return render(request, 'main/contact.html')

from .models import Course


def courses(request):
    all_courses = Course.objects.all()
    return render(request, 'main/courses.html', {'courses': all_courses})

## Contact Form Submission Handling


def contact(request):
    success = False
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save message to database
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Send email notification (optional)
        full_message = f"Message from {name} ({email}):\n\n{message}"
        try:
            send_mail(
                subject="New Contact Form Message - AR Online Quran Academy",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['hawkak2464@gmail.com'],
                fail_silently=True,
            )
            success = True
        except Exception as e:
            print("Email send failed:", e)

    return render(request, 'main/contact.html', {'success': success})





def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'main/course_detail.html', {'course': course})
