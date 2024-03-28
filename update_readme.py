import os
import requests

def get_latest_projects():
    url = "https://api.github.com/users/xXxTheDarkprogramerxXx/repos?sort=created&direction=desc"
    resp = requests.get(url)
    projects = resp.json()
    lines = []
    for project in projects[:5]: # Get the 5 most recent projects
        lines.append(f"- [{project['name']}]({project['html_url']}) - {project['description']}\n")
    return lines

def update_readme(projects):
    readme_path = "README.md"
    with open(readme_path, "r") as file:
        lines = file.readlines()
    
    # Find the section to update
    start = lines.index("### Latest Projects\n") + 1
    end = start + lines[start:].index("\n")  # Assume there's an empty line after the section
    new_lines = lines[:start] + projects + lines[end:]
    
    with open(readme_path, "w") as file:
        file.writelines(new_lines)

if __name__ == "__main__":
    projects = get_latest_projects()
    update_readme(projects)
