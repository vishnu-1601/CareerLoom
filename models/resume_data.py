class ResumeData:
    def __init__(self, experience_level, personal_info, education_list, project_list, experience_list, skills):
        self.experience_level = experience_level
        self.personal_info = personal_info
        self.education_list = education_list
        self.project_list = project_list
        self.experience_list = experience_list
        self.skills = skills

    def to_dict(self):
        # Useful for storing in Flask session
        return {
            'experience_level': self.experience_level,
            'personal_info': self.personal_info.__dict__,
            'education_list': [edu.__dict__ for edu in self.education_list],
            'project_list': [proj.__dict__ for proj in self.project_list],
            'experience_list': [exp.__dict__ for exp in self.experience_list],
            'skills': self.skills
        }
    
    @classmethod
    def from_dict(cls, data):
        from .personal_info import PersonalInfo
        from .education import Education
        from .project import Project
        from .experience import Experience

        return cls(
            experience_level=data.get('experience_level', 'Student'),
            personal_info=PersonalInfo(**data.get('personal_info', {})),
            education_list=[Education(**edu) for edu in data.get('education_list', [])],
            project_list=[Project(**proj) for proj in data.get('project_list', [])],
            experience_list=[Experience(**exp) for exp in data.get('experience_list', [])],
            skills=data.get('skills', '')
        )
