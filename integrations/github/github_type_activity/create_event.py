class CreateEvent:
    def __init__(self, objectType, repo):
        self.objectType = objectType
        self.repo = repo

    def __str__(self):
        return f"- Created {self.objectType} in {self.repo}"