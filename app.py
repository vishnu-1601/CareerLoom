import os
from flask import Flask, render_template, request, session, redirect, url_for, send_file
from models.resume_data import ResumeData
from templates_logic.template_selector import get_template

app = Flask(__name__)
app.secret_key = 'careerloom_secret_key' # In production, use os.environ.get('SECRET_KEY')
app.config['OUTPUT_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')

# Ensure output directory exists
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    # If session has data, we can either clear it or pass it. 
    # Let's start fresh on index, but pass empty data.
    return render_template('form.html', resume_data={})

@app.route('/edit')
def edit():
    # Pre-fill form from session data
    resume_data = session.get('resume_data', {})
    return render_template('form.html', resume_data=resume_data)

@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        # Parse basic info
        experience_level = request.form.get('experience_level', 'Student')
        personal_info = {
            'full_name': request.form.get('full_name', ''),
            'email': request.form.get('email', ''),
            'phone': request.form.get('phone', ''),
            'links': request.form.get('links', '')
        }
        
        # Parse arrays of data
        # To handle dynamic fields, we use arrays in HTML: name="edu_degree[]"
        education_list = []
        edu_degrees = request.form.getlist('edu_degree[]')
        edu_institutions = request.form.getlist('edu_institution[]')
        edu_years = request.form.getlist('edu_year[]')
        edu_scores = request.form.getlist('edu_score[]')
        
        for i in range(len(edu_degrees)):
            if edu_degrees[i].strip():
                education_list.append({
                    'degree': edu_degrees[i],
                    'institution': edu_institutions[i] if i < len(edu_institutions) else '',
                    'year': edu_years[i] if i < len(edu_years) else '',
                    'score': edu_scores[i] if i < len(edu_scores) else ''
                })

        project_list = []
        proj_titles = request.form.getlist('proj_title[]')
        proj_techs = request.form.getlist('proj_tech[]')
        proj_descs = request.form.getlist('proj_desc[]')
        
        for i in range(len(proj_titles)):
            if proj_titles[i].strip():
                project_list.append({
                    'title': proj_titles[i],
                    'tech_stack': proj_techs[i] if i < len(proj_techs) else '',
                    'description': proj_descs[i] if i < len(proj_descs) else ''
                })

        experience_list = []
        exp_roles = request.form.getlist('exp_role[]')
        exp_companies = request.form.getlist('exp_company[]')
        exp_durations = request.form.getlist('exp_duration[]')
        exp_resps = request.form.getlist('exp_resp[]')
        
        for i in range(len(exp_roles)):
            if exp_roles[i].strip():
                experience_list.append({
                    'role': exp_roles[i],
                    'company': exp_companies[i] if i < len(exp_companies) else '',
                    'duration': exp_durations[i] if i < len(exp_durations) else '',
                    'responsibilities': exp_resps[i] if i < len(exp_resps) else ''
                })
        
        skills = request.form.get('skills', '')

        # Build raw dict for session
        resume_data_dict = {
            'experience_level': experience_level,
            'personal_info': personal_info,
            'education_list': education_list,
            'project_list': project_list,
            'experience_list': experience_list,
            'skills': skills
        }

        # Save to session
        session['resume_data'] = resume_data_dict

        # Build ResumeData object and generate text
        resume_data_obj = ResumeData.from_dict(resume_data_dict)
        template = get_template(experience_level)
        generated_text = template.generate(resume_data_obj)
        
        # Save generated text in session for easy preview/download access
        session['generated_text'] = generated_text

        return render_template('preview.html', generated_text=generated_text)

@app.route('/download')
def download():
    generated_text = session.get('generated_text', '')
    resume_data = session.get('resume_data', {})
    name = resume_data.get('personal_info', {}).get('full_name', 'Resume').replace(" ", "_")
    
    if not generated_text:
        return redirect(url_for('index'))
    
    filename = f"{name}_Resume.tex"
    filepath = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(generated_text)
        
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
