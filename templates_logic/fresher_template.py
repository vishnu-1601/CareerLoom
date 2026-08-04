from .base_template import BaseTemplate
from models.resume_data import ResumeData

class FresherTemplate(BaseTemplate):
    def generate(self, resume_data: ResumeData) -> str:
        """
        Fresher Template prioritizes Education, then Projects, then some Experience (if any).
        """
        preamble = self._get_latex_preamble()
        header = self._format_header(resume_data.personal_info)
        skills = self._format_skills(resume_data.skills)
        education = self._format_education(resume_data.education_list)
        experience = self._format_experience(resume_data.experience_list)
        projects = self._format_projects(resume_data.project_list)
        
        body_content = "\n".join([header, skills, education, experience, projects])
        
        return f"{preamble}\n\\begin{{document}}\n\n{body_content}\n\n\\end{{document}}"
