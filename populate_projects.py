#!/usr/bin/env python
"""
Populate initial projects based on Sravan's resume
Run this after migrations: python populate_projects.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from projects.models import Project

# Define projects from Sravan's resume
projects_data = [
    {
        'title': 'Drowsiness Detection System',
        'description': 'A real-time driver drowsiness detection system built with Python and OpenCV. Uses CNN/MCNN for feature extraction and detection. Integrated with Flask for web deployment. Features include real-time video processing, alert system, and accurate driver state classification.'
    },
    {
        'title': 'Weather Detection Application',
        'description': 'A desktop GUI application built with PyQt5 that displays real-time weather information using the OpenWeather API. Features robust error handling for invalid inputs and API errors. Includes weather forecasting, location search, and intuitive user interface.'
    },
    {
        'title': 'AI-Powered Tic Tac Toe Game',
        'description': 'An AI-based Tic Tac Toe game implementation using the Minimax algorithm. The AI makes optimal decisions demonstrating advanced game theory and decision-making logic. Includes both human vs AI and AI vs AI modes with difficulty levels.'
    }
]

# Check if projects already exist
existing_count = Project.objects.count()

if existing_count == 0:
    print("Creating projects...")
    for project_info in projects_data:
        project, created = Project.objects.get_or_create(
            title=project_info['title'],
            defaults={'description': project_info['description']}
        )
        if created:
            print(f"✓ Created: {project.title}")
        else:
            print(f"• Already exists: {project.title}")
    
    print(f"\nTotal projects: {Project.objects.count()}")
    print("Projects populated successfully!")
else:
    print(f"Projects already exist ({existing_count} projects found).")
    print("Skipping population to avoid duplicates.")
