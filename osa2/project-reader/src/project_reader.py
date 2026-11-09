from urllib import request
from project import Project
import toml



class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)
        
        project_data = data["project"]
        
        name = project_data["name"]
        description = project_data["description"]
        dependencies = project_data.get("dependencies", [])
        
        dev_dependencies = data.get("dependency-groups", {}).get("dev", [])
        license = project_data.get("license", "")
        
        authors = [
                author["name"]
                for author in project_data.get("authors", [])
            ]
        
        dependencies = [dep.split(">=")[0] for dep in dependencies]
        dev_dependencies = [dep.split(">=")[0] for dep in dev_dependencies]
        
        return Project(
                name,
                description,
                dependencies,
                dev_dependencies,
                license,
                authors
            )
        