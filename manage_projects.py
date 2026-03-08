#!/usr/bin/env python
"""
Easy Project Manager for Portfolio
Run: python manage_projects.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from projects.models import Project

def add_project():
    """Interactive function to add a new project"""
    print("\n" + "="*60)
    print("⚡ ADD NEW PROJECT TO PORTFOLIO ⚡")
    print("="*60 + "\n")
    
    title = input("Project Title: ").strip()
    if not title:
        print("❌ Title is required!")
        return False
    
    description = input("Project Description: ").strip()
    if not description:
        print("❌ Description is required!")
        return False
    
    # Check if project already exists
    if Project.objects.filter(title=title).exists():
        print(f"❌ Project '{title}' already exists!")
        return False
    
    # Create project
    project = Project.objects.create(title=title, description=description)
    print(f"\n✅ Project created successfully!")
    print(f"   Title: {project.title}")
    print(f"   Description: {project.description[:50]}...")
    print(f"   ID: {project.id}\n")
    return True

def list_projects():
    """List all projects"""
    projects = Project.objects.all()
    if not projects:
        print("\n❌ No projects found!\n")
        return
    
    print("\n" + "="*60)
    print("📊 ALL PROJECTS IN PORTFOLIO")
    print("="*60 + "\n")
    for i, project in enumerate(projects, 1):
        print(f"{i}. {project.title}")
        print(f"   Description: {project.description[:60]}...")
        print(f"   Created: {project.created.strftime('%Y-%m-%d %H:%M')}")
        print()

def delete_project():
    """Delete a project"""
    list_projects()
    try:
        project_id = int(input("Enter Project ID to delete: "))
        project = Project.objects.get(id=project_id)
        title = project.title
        project.delete()
        print(f"\n✅ Project '{title}' deleted successfully!\n")
        return True
    except (Project.DoesNotExist, ValueError):
        print("\n❌ Invalid project ID!\n")
        return False

def edit_project():
    """Edit an existing project"""
    list_projects()
    try:
        project_id = int(input("Enter Project ID to edit: "))
        project = Project.objects.get(id=project_id)
        
        print(f"\nCurrent Title: {project.title}")
        new_title = input("New Title (press Enter to keep): ").strip()
        if new_title:
            project.title = new_title
        
        print(f"Current Description: {project.description}")
        new_desc = input("New Description (press Enter to keep): ").strip()
        if new_desc:
            project.description = new_desc
        
        project.save()
        print(f"\n✅ Project updated successfully!\n")
        return True
    except (Project.DoesNotExist, ValueError):
        print("\n❌ Invalid project ID!\n")
        return False

def main():
    while True:
        print("\n" + "="*60)
        print("🤖 PORTFOLIO PROJECT MANAGER")
        print("="*60 + "\n")
        print("1. ➕ Add New Project")
        print("2. 📋 List All Projects")
        print("3. ✏️  Edit Project")
        print("4. 🗑️  Delete Project")
        print("5. 📊 Project Stats")
        print("6. ❌ Exit\n")
        
        choice = input("Select option (1-6): ").strip()
        
        if choice == '1':
            add_project()
        elif choice == '2':
            list_projects()
        elif choice == '3':
            edit_project()
        elif choice == '4':
            delete_project()
        elif choice == '5':
            count = Project.objects.count()
            print(f"\n📊 Total Projects: {count}\n")
        elif choice == '6':
            print("\n👋 Goodbye!\n")
            break
        else:
            print("\n❌ Invalid option!\n")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Exiting...\n")
