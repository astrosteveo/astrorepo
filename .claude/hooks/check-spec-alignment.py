#!/usr/bin/env python3
"""
Post-edit hook to check if edits maintain spec alignment.
"""
import json
import sys
import re

def check_alignment(file_path, edit_content):
    """Check if edit aligns with specification."""
    spec_refs = re.findall(r'SPEC-[A-Z]+-\d+', edit_content)
    
    if spec_refs:
        return True
    
    critical_patterns = ['/services/', '/controllers/', '/api/']
    if any(pattern in file_path for pattern in critical_patterns):
        return False
    
    return True

def main():
    input_data = json.load(sys.stdin)
    
    if input_data.get("tool_name") != "Edit":
        sys.exit(0)
    
    file_path = input_data.get("tool_input", {}).get("file_path", "")
    new_string = input_data.get("tool_input", {}).get("new_string", "")
    
    alignment_ok = check_alignment(file_path, new_string)
    
    if not alignment_ok:
        print("ℹ️  Consider reviewing specification alignment after this edit", file=sys.stderr)
        print(f"   File: {file_path}", file=sys.stderr)
        print("   Tip: Add spec reference (e.g., // SPEC-AUTH-001) to critical code", file=sys.stderr)
    
    sys.exit(0)

if __name__ == "__main__":
    main()
