class PushEvent:
    def __init__(self, numberOfCommits, repo):
        self.numberOfCommits = numberOfCommits
        self.repo = repo

    def __str__(self):
        if self.numberOfCommits == 1:
            return f"- Pushed {self.numberOfCommits} commit to {self.repo}"
        else:
            return f"- Pushed {self.numberOfCommits} commits to {self.repo}"