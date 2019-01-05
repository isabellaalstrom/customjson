"""Create json with information for custom_updater."""
from json import dumps
import requests
from github import Github
import customjson.defaults as DEFAULT

class CreateJson():
    """Class for json creation."""

    def __init__(self, token, user, repo, repos, reuse, json_file, push):
        """Initilalize."""
        self.token = token
        self.user = user
        self.repo = repo
        self.repos = repos
        self.reuse = reuse
        self.json_file = json_file
        self.push = push
        self.github = Github(token)

    def component(self):
        "Generate json for components."
        if self.user is None:
            self.user = DEFAULT.COMPONENT_USER
        if self.repo is None:
            self.repo = DEFAULT.REPO
        if self.json_file is None:
            self.json_file = DEFAULT.JSON_FILE
        if self.reuse:
            info = DEFAULT.REUSE.format(self.user, self.repo, self.json_file)
            data = requests.get(info).json()
        else:
            data = {}
        if self.repos is None:
            repos = []
            for repo in list(self.github.get_user(self.user).get_repos()):
                repos.append(repo.name)
            self.repos = repos
        for repo in self.repos:
            print("Generating json for repo:", repo)
            repo = self.github.get_repo(self.user + '/' + repo)
            name = repo.name
            updated_at = repo.updated_at.isoformat().split('T')[0]
            platform = True if len(name.split('.')) > 1 else False
            if platform:
                location = 'custom_components/{}/{}.py'
                location = location.format(name.split('.')[0],
                                           name.split('.')[1])
            else:
                location = 'custom_components/{}.py'.format(name)
                try:
                    repo.get_file_contents(location)
                except:
                    location = 'custom_components/{}/__init__.py'.format(name)

            updated_at = updated_at
            local_location = '/{}'.format(location)
            remote_location = DEFAULT.REUSE.format(self.user, name, location)
            visit_repo = DEFAULT.VISIT.format(self.user, name)
            changelog = DEFAULT.CHANGELOG.format(self.user, name)

            data[name] = {}
            data[name]['updated_at'] = updated_at
            data[name]['local_location'] = local_location
            data[name]['remote_location'] = remote_location
            data[name]['visit_repo'] = visit_repo
            data[name]['changelog'] = changelog
        if self.push:
            print("push it!")

        else:
            print(dumps(data, indent=4, sort_keys=True))

    def card(self):
        "Generate json for components."
        print("Not implemented")