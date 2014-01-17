#!/usr/bin/env python

import re
import subprocess
import time

def run_server():
    subprocess.check_call(['python', 'setup.py', 'build'])
    return subprocess.Popen(['python', 'build/lib/bunny1/bunny650.py', '--host=localhost'])

def check_git_updates():
    subprocess.check_call(['git', 'fetch'])
    output = subprocess.check_output(['git', 'log', 'HEAD..origin/master', '--oneline'])
    commits = re.findall(r'^[a-f\d]+\b', output, re.M)
    return bool(commits)

def check_git_updates_safe():
    try:
        return check_git_updates()
    except Exception as e:
        print e.message
        return False

def update_git_repo():
    subprocess.check_call(['git', 'stash'])
    subprocess.check_call(['git', 'clean', '-dfx'])
    subprocess.check_call(['git', 'rebase', 'origin'])

def main():
    while True:
        server_process = run_server()
        try:
            while not check_git_updates_safe():
                time.sleep(60)
            update_git_repo()
        except Exception as e:
            print e.message
        finally:
            server_process.terminate()

if __name__ == '__main__':
    main()
