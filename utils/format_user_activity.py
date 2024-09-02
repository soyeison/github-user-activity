from integrations.github.github_type_activity.push_event import PushEvent
from integrations.github.github_type_activity.issue_event import IssueEvent
from integrations.github.github_type_activity.watch_event import WatchEvent
from integrations.github.github_type_activity.fork_event import ForkEvent
from integrations.github.github_type_activity.create_event import CreateEvent

def formatUserActivity(activities):
    listMapped = []

    for activity in activities:
        formatToSave = activity['type']

        if formatToSave == "PushEvent":
            numberOfCommits = len(activity["payload"]["commits"])
            repository = activity["repo"]["name"]

            pushEventInstance = PushEvent(numberOfCommits, repository)

            listMapped.append(pushEventInstance)

        elif formatToSave == "IssueCommentEvent":
            issueAction = activity["payload"]["action"].capitalize()
            repository = activity["repo"]["name"]
    
            issueEventInstance = IssueEvent(issueAction, repository)

            listMapped.append(issueEventInstance)

        elif formatToSave == "WatchEvent":
            repository = activity["repo"]["name"]

            watchEventInstance = WatchEvent(repository)

            listMapped.append(watchEventInstance)

        elif formatToSave == "ForkEvent":
            repository = activity["repo"]["name"]

            forkEventInstance = ForkEvent(repository)

            listMapped.append(forkEventInstance)

        elif formatToSave == "CreateEvent":
            objectType = activity["payload"]["ref_type"]
            repository = activity["repo"]["name"]

            createEventInstance = CreateEvent(objectType, repository)

            listMapped.append(createEventInstance)

    return listMapped