import subprocess, sys

command = sys.argv[1:]

def execute_shell_to_commit_push_jsonkpifile():
    print("Commiting file to remote repository ")
    subprocess.run(command[0], shell = True, executable="/bin/bash")
    print("Finishing process on remote repository")