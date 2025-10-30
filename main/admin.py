from django.contrib import admin
from .models import ContactMessage
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


admin.site.register(ContactMessage)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')