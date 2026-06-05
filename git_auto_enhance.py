import os
import subprocess
import re

def enhance_markdown(content, filename):
    # Add emojis to headers if not already present
    content = re.sub(r'^# (?![🚀✨🔍])', '🚀 # ', content, flags=re.MULTILINE)
    content = re.sub(r'^## (?![🚀✨🔍])', '✨ ## ', content, flags=re.MULTILINE)
    content = re.sub(r'^### (?![🚀✨🔍])', '🔍 ### ', content, flags=re.MULTILINE)
    
    # Add a structured footer if not present
    if "🎯 **Pro Tip**" not in content:
        footer = "\n\n---\n*🎯 **Pro Tip**: Consistency is key in Machine Learning. Keep building and exploring!*"
        content += footer
        
    return content

def enhance_python(content, filename):
    if "=================================================================" not in content:
        header = f'"""\n=================================================================\n'
        header += f' 🚀 File: {os.path.basename(filename)}\n'
        header += f' ✨ Purpose: Advanced Data Science & MLOps\n'
        header += f' 📅 Last Updated: 2026\n'
        header += f'=================================================================\n"""\n\n'
        content = header + content
    return content

def main():
    print("Fetching files to enhance...")
    # List all tracked files
    result = subprocess.run(['git', 'ls-files'], stdout=subprocess.PIPE, text=True)
    files = result.stdout.splitlines()
    
    enhanced_count = 0
    for f in files:
        if not os.path.isfile(f) or os.path.basename(f) in ['git_auto_commit.py', 'git_auto_enhance.py', 'push_all_files.py']:
            continue
            
        try:
            with open(f, 'r', encoding='utf-8') as file:
                original_content = file.read()
        except UnicodeDecodeError:
            continue # Skip binary or non-utf8 files
            
        new_content = original_content
        
        if f.endswith('.md'):
            new_content = enhance_markdown(original_content, f)
        elif f.endswith('.py'):
            new_content = enhance_python(original_content, f)
            
        if new_content != original_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Enhanced structure for: {f}")
            
            # Commit the enhancement
            subprocess.run(['git', 'add', f])
            commit_msg = f"✨ Enhanced {os.path.basename(f)} with rich structure"
            subprocess.run(['git', 'commit', '-m', commit_msg], capture_output=True)
            enhanced_count += 1
            
    if enhanced_count > 0:
        print(f"\nSuccessfully enhanced and committed {enhanced_count} files. Pushing to GitHub...")
        subprocess.run(['git', 'push', 'origin', 'main'])
        print("Push complete!")
    else:
        print("All files are already fully enhanced!")

if __name__ == '__main__':
    main()
