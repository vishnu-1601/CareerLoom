from .student_template import StudentTemplate
from .fresher_template import FresherTemplate
from .experienced_template import ExperiencedTemplate

def get_template(experience_level: str):
    """
    Returns the appropriate template instance based on experience level.
    Uses Strategy Pattern.
    """
    if experience_level.lower() == 'student':
        return StudentTemplate()
    elif experience_level.lower() == 'fresher':
        return FresherTemplate()
    elif experience_level.lower() == 'experienced':
        return ExperiencedTemplate()
    else:
        # Default fallback
        return StudentTemplate()
