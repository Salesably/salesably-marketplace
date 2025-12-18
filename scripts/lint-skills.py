#!/usr/bin/env python3
import os
import re
import sys

def lint_skill_file(file_path):
    errors = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for YAML frontmatter
    if not content.startswith('---'):
        errors.append("Missing YAML frontmatter start (---)")
    
    frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not frontmatter_match:
        errors.append("Malformed YAML frontmatter")
    else:
        fm_content = frontmatter_match.group(1)
        if 'name:' not in fm_content:
            errors.append("Frontmatter missing 'name' field")
        if 'description:' not in fm_content:
            errors.append("Frontmatter missing 'description' field")

    # Check for em-dashes and en-dashes
    if '—' in content:
        errors.append("Contains forbidden em-dash (—)")
    if '–' in content:
        errors.append("Contains forbidden en-dash (–)")

    return errors

def main():
    # Use CWD instead of file location to find skills
    base_dir = os.getcwd()
    skills_found = []
    all_errors = {}

    print(f"Searching for SKILL.md files in {base_dir}...")
    for root, dirs, files in os.walk(base_dir):
        # Skip .git directory
        if '.git' in root:
            continue
        for file in files:
            if file == 'SKILL.md':
                file_path = os.path.join(root, file)
                skills_found.append(file_path)
                errors = lint_skill_file(file_path)
                if errors:
                    all_errors[file_path] = errors

    if not skills_found:
        print("No SKILL.md files found.")
        return

    print(f"Scanned {len(skills_found)} skill files.")

    if all_errors:
        print("\nFound issues in skill files:")
        for file_path, errors in all_errors.items():
            rel_path = os.path.relpath(file_path, base_dir)
            print(f"\n{rel_path}:")
            for err in errors:
                print(f"  - {err}")
        sys.exit(1)
    else:
        print("\nAll skill files passed validation!")
        sys.exit(0)

if __name__ == "__main__":
    main()
