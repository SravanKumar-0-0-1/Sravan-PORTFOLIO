from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse, FileResponse
from django.db.models import Q
from .models import Project, Contact, Resume
from .forms import ContactForm


class HomepageView(TemplateView):
    template_name = 'projects/home.html'
    context_object_name = 'homepage'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_projects'] = Project.objects.all()[:3]
        context['total_projects'] = Project.objects.count()
        # extract technologies from project descriptions
        tech_keywords = ['Python','Django','CNN','PyQt5','OpenCV','Deep Learning','AI','Machine Learning','GUI','Multiscale','Minimax','Weather','Tic-Tac-Toe']
        technologies = set()
        for p in Project.objects.all():
            desc = p.description or ''
            for kw in tech_keywords:
                if kw.lower() in desc.lower():
                    technologies.add(kw)
        context['technologies'] = sorted(technologies)
        return context


class AboutView(TemplateView):
    template_name = 'projects/about.html'


class ResumeView(TemplateView):
    template_name = 'projects/resume.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume'] = Resume.objects.filter(is_public=True).first()
        # also provide techs from projects
        tech_keywords = ['Python','Django','CNN','PyQt5','OpenCV','Deep Learning','AI','Machine Learning','GUI','Multiscale','Minimax','Weather','Tic-Tac-Toe']
        technologies = set()
        for p in Project.objects.all():
            desc = p.description or ''
            for kw in tech_keywords:
                if kw.lower() in desc.lower():
                    technologies.add(kw)
        context['technologies'] = sorted(technologies)
        return context


def resume_download(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, is_public=True)
    response = FileResponse(resume.file.open('rb'))
    response['Content-Disposition'] = f'attachment; filename="{resume.title}.pdf"'
    return response


class ContactView(TemplateView):
    template_name = 'projects/contact.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['form'] = self.form_class(self.request.POST)
        else:
            context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('projects:contact_success')
        return self.get(request, *args, **kwargs)


class ContactSuccessView(TemplateView):
    template_name = 'projects/contact_success.html'


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/project_list.html'
    paginate_by = 6


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'projects/project_detail.html'
