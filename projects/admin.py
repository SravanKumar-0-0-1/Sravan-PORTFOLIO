from django.contrib import admin
from .models import Project, Contact, Resume, ProjectImage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)
    list_filter = ('created',)


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption', 'uploaded')
    search_fields = ('project__title', 'caption')
    list_filter = ('uploaded',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created')
    search_fields = ('name', 'email')
    list_filter = ('created',)
    readonly_fields = ('created',)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_public', 'uploaded')
    list_filter = ('is_public', 'uploaded')
    readonly_fields = ('uploaded',)
