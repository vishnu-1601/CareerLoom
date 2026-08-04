# CareerLoom
> Craft the perfect resume tailored dynamically to your career stage.

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/flask-%23000.svg?logo=flask&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-In%20Development-orange)

---

## Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Key Features](#key-features)
- [Demo / Screenshots](#demo--screenshots)
- [Tech Stack](#tech-stack)
- [Architecture / How It Works](#architecture--how-it-works)
- [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Routes / API Reference](#routes--api-reference)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Author / Contact](#author--contact)

---

## Overview
CareerLoom is a full-stack web application designed to help students, freshers, and experienced professionals build resumes tailored specifically to their experience level. By collecting user data through a dynamic form and applying intelligent, role-based template structuring, the app ensures that the most relevant qualifications are emphasized for every job seeker.

---

## Problem Statement
Building a resume can be a frustrating and confusing process for many job seekers:
* **One-Size-Fits-All Templates:** Generic resume builders rarely adapt their structure based on whether the user is a student (who should emphasize academics) or an experienced professional (who should emphasize work history).
* **High Barrier to Entry:** Professional resume generation tools like LaTeX/Overleaf have a steep learning curve and require technical knowledge.
* **Analysis Paralysis:** Freshers and students often struggle with deciding what to include and how to arrange their sections effectively.

---

## Key Features

### Core Features
- [x] **Role-Based Dynamic Generation:** Automatically selects and restructures the resume layout based on your chosen level (Student / Fresher / Experienced).
- [x] **Dynamic Form Inputs:** Add, edit, or remove multiple projects, educational degrees, and work experiences on the fly.
- [x] **Real-Time Progress Tracking:** Visual indicator showing form completion percentage in real-time.
- [x] **Live Preview:** Review your generated resume instantly in a clean, readable layout.
- [x] **Edit & Regenerate:** Seamlessly toggle back to the form with all fields pre-filled to correct mistakes.
- [x] **Download to LaTeX/Plaintext:** Export the final generated resume as a beautifully formatted `.tex` file for easy compilation.
- [x] **Fully Responsive UI:** Built with CSS Grid/Flexbox to ensure a seamless experience on mobile, tablet, and desktop.

### Planned Features
- [ ] ATS keyword matching against job descriptions.
- [ ] PDF export functionality.
- [ ] Database integration and user authentication.
- [ ] Multiple saved resume versions per user.

---

## Demo / Screenshots
*(Screenshots coming soon)*
> Placeholders for UI imagery demonstrating the dynamic form, progress bar, and generated resume previews.

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3, Flask |
| **Templating** | Jinja2 |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Data Storage** | Flask `session` (In-memory, no external database) |

---

## Architecture / How It Works

CareerLoom utilizes a lightweight, session-based architecture coupled with the **Strategy design pattern** to handle resume generation dynamically without the overhead of a database.

### Request Flow
```text
User Input → Flask Route (/generate) → Template Selector → Generated Resume → Preview
```
1. **Form Submission:** The user submits their details via the frontend form.
2. **Session Storage:** The Flask backend parses the nested form data into a structured `ResumeData` object and caches it in the user's session.
3. **Template Selection:** Based on the `experience_level` selected, the backend delegates rendering to a specific strategy class (e.g., `StudentTemplate`).
4. **Generation & Preview:** The strategy class orders the data optimally, generates the text, and serves it back to the frontend for preview.

### The Strategy Pattern
Instead of messy `if/else` logic to reorder resume sections, CareerLoom implements a clean Strategy pattern. A generic `BaseTemplate` provides formatting rules, while interchangeable concrete classes (`StudentTemplate`, `FresherTemplate`, `ExperiencedTemplate`) dictate the structural layout. Adding a new resume style is as simple as adding a new class.

---

## Folder Structure

```text
careerloom/
├── app.py                     # Main Flask application and route definitions
├── requirements.txt           # Python dependencies
├── .gitignore                 # Ignored files and environment variables
├── models/                    # Data models representing resume sections
│   ├── __init__.py
│   ├── personal_info.py
│   ├── education.py
│   ├── project.py
│   ├── experience.py
│   └── resume_data.py
├── templates_logic/           # Strategy pattern implementations for rendering
│   ├── __init__.py
│   ├── base_template.py       
│   ├── student_template.py
│   ├── fresher_template.py
│   ├── experienced_template.py
│   └── template_selector.py
├── templates/                 # Jinja2 HTML views
│   ├── form.html
│   └── preview.html
├── static/                    # Frontend assets
│   ├── css/
│   │   └── style.css          # Responsive glassmorphic styling
│   └── js/
│       └── script.js          # Dynamic form logic and progress bar
└── output/                    # Exported .tex resumes
```

---

## Getting Started

### Prerequisites
Make sure you have the following installed on your machine:
* Python 3.9 or higher
* `pip` (Python package manager)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/CareerLoom.git
   cd CareerLoom
   ```

2. **Create and activate a virtual environment (Recommended):**
   ```bash
   # Create the virtual environment
   python -m venv venv
   
   # Activate on macOS/Linux
   source venv/bin/activate
   
   # Activate on Windows
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```
   
5. **Open in Browser:**
   Navigate to `http://localhost:5000` to access the application.

---

## Usage

1. **Fill the Form:** Enter your personal information, add educational degrees, list projects, and detail your work experience.
2. **Select Role:** Choose your current career stage from the dropdown (Student, Fresher, Experienced).
3. **Generate:** Hit the generate button to process your data.
4. **Preview:** Review the live preview of your generated resume text.
5. **Edit / Download:** Click `Edit Form` to make changes with your data preserved, or hit `Download .tex` to save the resume to your local machine.

---

## Routes / API Reference

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Displays the dynamic resume input form. |
| `POST` | `/generate` | Processes form data, builds the resume, stores session, and shows preview. |
| `GET` | `/edit` | Returns the user to the form, pre-filling it with their existing session data. |
| `GET` | `/download` | Exports and downloads the generated resume as a `.tex` file. |

---

## Roadmap

- [x] Initial full-stack setup with Flask and Jinja2
- [x] Responsive glassmorphic UI design
- [x] Dynamic JavaScript form interactions
- [x] Strategy pattern integration for role-based templates
- [x] LaTeX `.tex` export functionality
- [ ] Implement `.pdf` native export
- [ ] Add user authentication (login/register)
- [ ] Database integration to save multiple resumes
- [ ] ATS keyword analysis feature

---

## Contributing

Contributions, issues, and feature requests are welcome! 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License
Distributed under the MIT License. See `LICENSE` for more information. *(Note: LICENSE file to be added)*

---

## Author / Contact

**Your Name**  
*Full Stack Development Enthusiast*  
- **LinkedIn:** [Your Profile](https://linkedin.com/in/yourprofile)  
- **GitHub:** [@yourusername](https://github.com/yourusername)  
- **Email:** your.email@example.com

---

*If you found this project useful, consider giving it a ⭐*
