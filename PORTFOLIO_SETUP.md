# 🚀 Sravan Kumar's Portfolio - Quick Start Guide

Your modern, professional portfolio is ready! Here's what has been updated:

## ✨ What Was Created/Updated

### 1. **Base Template (`base.html`)**
- Modern gradient header with Sravan Kumar branding
- Navigation menu (Home, Projects, About, Contact)
- Social media links (GitHub, LinkedIn, Email, Phone)
- Professional styling with responsive design
- Smooth animations and hover effects

### 2. **Home Page (`home.html`)**
- Hero section with gradient background
- Headline and professional description
- Call-to-action buttons (View Projects, Let's Talk)
- Featured projects grid
- Services section (Web Dev, AI/ML, Problem Solving)

### 3. **About Page (`about.html`)**
- Full professional profile
- All technical skills organized by category:
  - Languages: Python, C, SQL, Java
  - Web: HTML5, CSS3, Bootstrap, Django
  - AI/ML: OpenCV, CNN, MCNN, Deep Learning
  - Tools: PyQt5, SQLite, Git, etc.
- Education section with details
- Certifications & Courses
- Languages spoken (English, Hindi, Telugu)
- Soft skills badges
- Contact CTA

### 4. **Projects from Resume**
Three amazing projects auto-populated:
1. **Drowsiness Detection System** - Deep Learning with CNN/MCNN
2. **Weather Detection App** - PyQt5 + OpenWeather API  
3. **AI Tic Tac Toe Game** - Minimax Algorithm

### 5. **Database Model**
- Added `Contact` model to store visitor messages
- Admin interface to view all inquiries

---

## 📋 Next Steps (BEFORE Running Server)

### Step 1: Apply Migrations
```powershell
cd c:\Portfolio
c:/Portfolio/.venv/Scripts/python.exe manage.py makemigrations
c:/Portfolio/.venv/Scripts/python.exe manage.py migrate
```

### Step 2: Populate Projects (Optional but Recommended)
This will add your 3 projects automatically:
```powershell
c:/Portfolio/.venv/Scripts/python.exe populate_projects.py
```

### Step 3: Create Superuser (if you haven't already)
```powershell
c:/Portfolio/.venv/Scripts/python.exe manage.py createsuperuser
```
Follow the prompts to create your admin account.

### Step 4: Run Development Server
```powershell
c:/Portfolio/.venv/Scripts/python.exe manage.py runserver
```

---

## 🌐 Access Your Portfolio

Once the server is running:

- **Portfolio Homepage**: http://127.0.0.1:8000/
- **Projects Page**: http://127.0.0.1:8000/projects/
- **About Page**: http://127.0.0.1:8000/about/
- **Contact Page**: http://127.0.0.1:8000/contact/
- **Admin Dashboard**: http://127.0.0.1:8000/admin/

---

## 🎨 Styling Highlights

✓ Modern gradient color scheme (Purple #667eea - Deep Purple #764ba2)  
✓ Responsive design (mobile, tablet, desktop)  
✓ Smooth animations and transitions  
✓ Professional typography with Poppins font  
✓ Skill boxes with checkmarks  
✓ Experience timeline design  
✓ Project cards with hover effects  
✓ Contact forms with styled inputs  
✓ Social media icons in header & footer  

---

## 📞 Features Available

✅ **Home Page** - Hero section with projects showcase  
✅ **Projects** - List view of all projects with filtering  
✅ **Project Details** - Full details page for each project  
✅ **About** - Complete resume, skills, education, certifications  
✅ **Contact Form** - Visitors can send messages (stored in database)  
✅ **Social Links** - GitHub, LinkedIn, Email, Phone  
✅ **Admin Panel** - Manage projects and view contact submissions  
✅ **Responsive Design** - Works on mobile, tablet, desktop  

---

## 🔧 Customization Tips

### Add More Skills
Edit `about.html` and add items to the `<ul>` tags in the skills-container.

### Change Colors
Update the gradient colors in `base.html`:
- Current: `#667eea` to `#764ba2`
- Edit all `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`

### Add Project Images
Go to `/admin/` → Projects → Edit a project → Upload an image.

### Update Certifications
Edit the certifications section in `about.html` to add more courses.

### Customize Hero Text
Edit the first hero section in `home.html` or `about.html`.

---

## 📊 Admin Features

In `/admin/`:
- Add/Edit/Delete Projects
- View Contact Messages from visitors
- Filter projects by date
- Search by title or email

---

## 🎯 Next Features You Can Add

1. **Blog/Articles** - Showcase your technical writing
2. **Testimonials** - From colleagues or clients
3. **Dark Mode Toggle** - Add theme switching
4. **Portfolio Statistics** - "X projects completed", etc.
5. **Resume Download** - Add a PDF download link  
6. **Project Categories** - Filter by Web Dev, AI/ML, etc.
7. **Search Functionality** - Search projects by title/keywords
8. **Analytics** - Track visitor statistics
9. **Newsletter Signup** - Collect emails
10. **Testimonials Carousel** - Auto-rotating feedback

---

## ⚙️ Environment Info

- **Framework**: Django 6.0.2
- **Python**: 3.13.1
- **Database**: SQLite (default)
- **Installed Packages**: Pillow (image support), asgiref, sqlparse

---

## 🌟 It's Live!

Your portfolio is now a modern, professional showcase of your skills and projects. 
The design is responsive, the code is clean, and it's ready to impress!

**Now run the commands above and see your portfolio in action!** 🚀

