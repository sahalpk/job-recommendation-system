class User:
    def __init__(self, _id, name, skills, experience_level, preferences):
        self._id = _id
        self.name = name
        self.skills = skills
        self.experience_level = experience_level
        self.preferences = preferences

    def to_dict(self):
        return {
            '_id': str(self._id),
            'name': self.name,
            'skills': self.skills,
            'experience_level': self.experience_level,
            'preferences': self.preferences
        }
