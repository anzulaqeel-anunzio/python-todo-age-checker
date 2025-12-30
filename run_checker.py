# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os
from datetime import datetime

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from linter.core import TodoChecker

def main():
    parser = argparse.ArgumentParser(description="TODO Comment Age Checker")
    parser.add_argument("path", help="Directory or file to scan (defaults to current dir)", nargs='?', default=".")
    parser.add_argument("--days", "-d", type=int, default=30, help="Flag TODOs older than X days (default: 30)")
    parser.add_argument("--no-git", action="store_true", help="Skip git blame check (just list checking)")

    args = parser.parse_args()
    path = os.path.abspath(args.path)
    
    # 1. Gather all TODOs
    all_todos = []
    
    if os.path.isfile(path):
        all_todos = TodoChecker.scan_file(path)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            if 'node_modules' in dirs: dirs.remove('node_modules')
            if '.git' in dirs: dirs.remove('.git')
            for file in files:
                # Basic filter for textual files only?
                if file.endswith(('.py', '.js', '.ts', '.java', '.cpp', '.h', '.md', '.txt')):
                    fpath = os.path.join(root, file)
                    all_todos.extend(TodoChecker.scan_file(fpath))
    else:
        print(f"Error: Path '{path}' not found.")
        sys.exit(1)

    if not all_todos:
        print("No TODOs found! Great job!")
        sys.exit(0)

    # 2. Check ages if not skipped
    flagged = []
    now = datetime.now()
    
    print(f"Scanning {len(all_todos)} TODOs for age > {args.days} days...\n")
    
    for todo in all_todos:
        age_str = " (Unknown age)"
        is_old = False
        
        if not args.no_git:
            date = TodoChecker.get_git_blame_date(todo['file'], todo['line'])
            if date:
                delta = now - date
                days_old = delta.days
                age_str = f" ({days_old} days old)"
                if days_old > args.days:
                    is_old = True
        
        # If no-git, we just list them all maybe? Or logic implies we can't check age.
        # If is_old or no-git (show all)
        if is_old or args.no_git:
            print(f"[{todo['file']}:{todo['line']}] TODO: {todo['content']}{age_str}")
            flagged.append(todo)

    if flagged and not args.no_git:
        sys.exit(1)
    
    if not flagged and not args.no_git:
        print("All TODOs are fresh!")

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
