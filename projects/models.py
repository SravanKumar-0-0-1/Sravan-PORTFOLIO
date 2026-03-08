from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.project.title}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


class Resume(models.Model):
    title = models.CharField(max_length=100, default="Resume")
    file = models.FileField(upload_to='resumes/')
    uploaded = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True, help_text="Allow others to view/download")

    class Meta:
        ordering = ['-uploaded']

    def __str__(self):
        return self.title
