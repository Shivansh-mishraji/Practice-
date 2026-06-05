import os
import subprocess

def main():
    print("Checking for modified or untracked files...")
    
    # Get all modified and untracked files
    status_cmd = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    if status_cmd.returncode != 0:
        print("Error running git status. Is this a git repository?")
        return
        
    lines = status_cmd.stdout.splitlines()
    if not lines:
        print("No changes to commit. Everything is up to date!")
        return
        
    commit_count = 0
    for line in lines:
        # line format: " M path/to/file" or "?? path/to/file"
        state = line[:2]
        filepath = line[3:].strip()
        
        # Remove quotes if git added them
        if filepath.startswith('"') and filepath.endswith('"'):
            filepath = filepath[1:-1]
            
        if not os.path.isfile(filepath):
            continue
            
        # Add and commit the specific file
        subprocess.run(['git', 'add', filepath])
        
        commit_msg = f"Auto-update: refined {os.path.basename(filepath)}"
        commit_res = subprocess.run(['git', 'commit', '-m', commit_msg], capture_output=True, text=True)
        
        if commit_res.returncode == 0:
            print(f"Committed: {filepath}")
            commit_count += 1
            
    if commit_count > 0:
        print(f"\nCreated {commit_count} commits. Pushing to remote...")
        push_res = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
        if push_res.returncode == 0:
            print("Successfully pushed all commits!")
        else:
            print(f"Failed to push. Error:\n{push_res.stderr}")
    else:
        print("No files were successfully committed.")

if __name__ == '__main__':
    main()
