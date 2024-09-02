class IssueEvent:
    def __init__(self, issueAction, repository):
        self.issueAction = issueAction
        self.repository = repository

    def __str__(self):
        return f"- {self.issueAction} an issue in {self.repository}"