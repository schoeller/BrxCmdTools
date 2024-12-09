import os
from dulwich import porcelain
from dulwich.repo import Repo
from dulwich.client import get_transport_and_path, FetchPackResult

REPO_NAME = "BrxCmdTools"
REPO_URL = "https://github.com/schoeller/BrxCmdTools.git"

def get_repo_dir():
    return os.path.join(os.getenv('APPDATA'), REPO_NAME)

def pull_git_changes():
    repo_dir = get_repo_dir()
    try:
        if not os.path.exists(repo_dir):
            porcelain.clone(REPO_URL, repo_dir)
            print(f"Repository successfully cloned to {repo_dir}.")
        else:
            porcelain.pull(repo_dir)
            print(f"Repository successfully pulled to {repo_dir}.")
    except Exception as e:
        print(f"Error displaying changes: {e}")

def check_for_updates():
    # Local repository directory
    local_repo_path = os.path.join(os.path.join(os.getenv('APPDATA'), REPO_NAME))

    # Check if the local repository exists
    if not os.path.exists(local_repo_path):
        print(f"The local repository '{repo_name}' does not exist.")
        return

    try:
        # Open the local repository
        local_repo = Repo(local_repo_path)

        # Get the remote URL and the branch
        remote_url = REPO_URL

        # Get the transport and path information for the remote repository
        client, remote_path = get_transport_and_path(remote_url)

        # Fetch the references from the remote repository
        fetch_result = client.fetch(remote_path, local_repo)

        # Check if fetch_result is a FetchPackResult object
        if not isinstance(fetch_result, FetchPackResult):
            print("Error fetching references from the remote repository.")
            return

        remote_refs = fetch_result.refs

        # Get the local and remote references for the 'main' branch
        local_ref = local_repo.refs.as_dict().get(b'refs/heads/main')
        remote_ref = remote_refs.get(b'refs/heads/main')

        # Compare the references
        if local_ref == remote_ref:
            print("The local repository is up to date.")
        else:
            print("The local repository is not up to date.")
            print(f"Local reference: {local_ref}")
            print(f"Remote reference: {remote_ref}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_for_updates()
    pull_git_changes()
