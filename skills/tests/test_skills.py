
from skills import skills

class TestSkills:
    def test_get_contains_vibrator(self):
        test_skills = skills.Skills()
        results = test_skills.get()
        assert "vibrato" in results