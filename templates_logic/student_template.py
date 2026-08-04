from .base_template import BaseTemplate
from models.resume_data import ResumeData

class StudentTemplate(BaseTemplate):
    def generate(self, resume_data: ResumeData) -> str:
        """
        Student Template prioritizes Education and Projects over Experience.
        """
        preamble = self._get_latex_preamble()
        header = self._format_header(resume_data.personal_info)
        education = self._format_education(resume_data.education_list)
        skills = self._format_skills(resume_data.skills)
        projects = self._format_projects(resume_data.project_list)
        experience = self._format_experience(resume_data.experience_list)
        
        body_content = "\n".join([header, education, skills, projects, experience])
        
        return f"{preamble}\n\\begin{{document}}\n\n{body_content}\n\n\\end{{document}}"
