import requests

def check_for_update(repo_owner, repo_name, current_version):
    # GitHub API endpoint to get the latest release version
    api_url = f'https://api.github.com/repos/{iamroyalmayor}/{hash-Algorithim-Detector}/releases/latest'
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            latest_version = response.json()['tag_name']
            if latest_version != current_version:
                return f"A new version ({latest_version}) is available. Please update your code."
            else:
                return "You have the latest version."
        else:
            return "Failed to fetch update information."
    except Exception as e:
        return f"Error checking for updates: {str(e)}"

if __name__ == '__main__':
    repo_owner = 'iamroyalmayor'  # Your GitHub username or organization name
    repo_name = 'hash-Algorithim-Detector'  # Your repository name
    current_version = '1.0'  # Your current version number

    result = check_for_update(repo_owner, repo_name, current_version)
    print(result)
