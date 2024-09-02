class ForkEvent:
    def __init__(self, repo):
        self.repo = repo

    def __str__(self):
        return f"- Forked {self.repo}"