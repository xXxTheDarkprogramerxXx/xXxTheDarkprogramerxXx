import os
import requests

def get_latest_projects():
    print("Fetching the latest projects...")
    url = "https://api.github.com/users/xXxTheDarkprogramerxXx/repos?sort=pushed&direction=desc"
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f"Failed to fetch repositories: {resp.status_code}")
        return []
    projects = resp.json()
    lines = []
    for project in projects[:5]:  # Adjust the number of projects as needed
        if project['full_name'] == "xXxTheDarkprogramerxXx/xXxTheDarkprogramerxXx":
            continue  # Skip the specific project
        line = f"- [{project['name']}]({project['html_url']}) - {project['description']}\n"
        print(f"Adding project: {line.strip()}")
        lines.append(line)
    return lines

def update_readme(projects):
    print("Updating README.md...")
    readme_path = "README.md"
    with open(readme_path, "r") as file:
        lines = file.readlines()
    
    # Find the section to update. Adjust these lines if your README format is different.
    try:
        start = lines.index("### Latest Projects\n") + 1
        end = start + lines[start:].index("\n")
    except ValueError:
        print("Failed to find the 'Latest Projects' section in README.md.")
        return
    
    new_lines = lines[:start] + projects + lines[end:]
    
    with open(readme_path, "w") as file:
        file.writelines(new_lines)
    print("README.md updated successfully.")

if __name__ == "__main__":
    projects = get_latest_projects()
    if projects:
        update_readme(projects)
    else:
        print("No projects to update.")
