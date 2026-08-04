from .base_template import BaseTemplate
from models.resume_data import ResumeData

class ExperiencedTemplate(BaseTemplate):
    def generate(self, resume_data: ResumeData) -> str:
        """
        Experienced Template prioritizes Work Experience heavily, followed by Skills and Education.
        """
        preamble = self._get_latex_preamble()
        header = self._format_header(resume_data.personal_info)
        experience = self._format_experience(resume_data.experience_list)
        skills = self._format_skills(resume_data.skills)
        projects = self._format_projects(resume_data.project_list)
        education = self._format_education(resume_data.education_list)
        
        body_content = "\n".join([header, experience, skills, projects, education])
        
        return f"{preamble}\n\\begin{{document}}\n\n{body_content}\n\n\\end{{document}}"
