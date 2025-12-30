# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import re
import os
import subprocess
from datetime import datetime

class TodoChecker:
    # Match TODO: string
    TODO_PATTERN = re.compile(r'TODO[:\s]+(.*)', re.IGNORECASE)

    @staticmethod
    def get_git_blame_date(filepath, line_num):
        try:
            # git blame -L line,line --porcelain filepath
            cmd = ['git', 'blame', '-L', f'{line_num},{line_num}', '--porcelain', filepath]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                return None
            
            # Parse output for author-time
            # author-time 1600000000
            for line in result.stdout.splitlines():
                if line.startswith('author-time '):
                    timestamp = int(line.split()[1])
                    return datetime.fromtimestamp(timestamp)
        except:
            return None
        return None

    @staticmethod
    def scan_file(filepath):
        issues = []
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    match = TodoChecker.TODO_PATTERN.search(line)
                    if match:
                        issues.append({
                            'line': line_num,
                            'file': filepath,
                            'content': match.group(1).strip()
                        })
        except Exception:
            pass
        return issues

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
