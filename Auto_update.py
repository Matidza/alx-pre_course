import subprocess

def update_vscode_libraries():
    # Run the system command to update all libraries for VS Code
    command = "sudo apt update && sudo apt upgrade code-insiders"
    process = subprocess.Popen(command, shell=True)
    process.wait()

if __name__ == "__main__":
    update_vscode_libraries()
    print("VS Code libraries have been updated.")
