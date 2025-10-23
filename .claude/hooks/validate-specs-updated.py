#!/usr/bin/env python3
"""
Pre-commit hook to ensure specifications are updated when code changes.
"""
import json
import sys
import subprocess

def get_changed_files():
    """Get list of files being committed."""
    result = subprocess.run(
        ['git', 'diff', '--cached', '--name-only'],
        capture_output=True,
        text=True
    )
    return result.stdout.strip().split('\n')

def find_related_spec(code_file):
    """Find specification file related to code file."""
    parts = code_file.split('/')
    if len(parts) >= 2:
        module = parts[1] if parts[0] == 'src' else parts[0]
        return f"docs/specs/{module}-spec.md"
    return None

def main():
    input_data = json.load(sys.stdin)
    
    changed_files = get_changed_files()
    code_files = [f for f in changed_files if f.endswith(('.ts', '.js', '.py', '.java', '.go', '.rs'))]
    
    if not code_files:
        sys.exit(0)
    
    issues = []
    for code_file in code_files:
        spec_file = find_related_spec(code_file)
        if spec_file and spec_file not in changed_files:
            issues.append(f"Code file '{code_file}' changed but spec '{spec_file}' not updated")
    
    if issues:
        print("⚠️  Specification Update Required", file=sys.stderr)
        for issue in issues:
            print(f"  • {issue}", file=sys.stderr)
        print("\nEither update the specifications or use --no-verify to skip this check.", file=sys.stderr)
        sys.exit(1)
    
    sys.exit(0)

if __name__ == "__main__":
    main()
