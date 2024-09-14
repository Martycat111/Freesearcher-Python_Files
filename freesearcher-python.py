import requests

def list_github_repo_files(repo_owner, repo_name):
    # GitHub API URL to get the repository contents
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        
        # Parse the response and check if it's a directory
        contents = response.json()
        if isinstance(contents, list):
            print(f"Files in the repository '{repo_name}':")
            for content in contents:
                if content['type'] == 'file':
                    print(f"- {content['path']}")
                elif content['type'] == 'dir':
                    print(f"[Directory] {content['path']}")
        else:
            print(f"Failed to list files: Unexpected response format.")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get user input to run the command
    command = input("Enter command: ").strip().lower()
    
    if command == "list":
        # Use the repo owner 'Martycat111' and the repository 'Freesearcher-Python_Files'
        repo_owner = "Martycat111"
        repo_name = "Freesearcher-Python_Files"

        # List the files in the specified repository
        list_github_repo_files(repo_owner, repo_name)
    else:
        print("Invalid command. Type 'list' to list all files in the GitHub repo.")
