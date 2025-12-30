import os
import re

# Directory to scan
directory = r"c:\Users\User\Desktop\github\argamassa-baritada"

# Replacements map (Regex -> Replacement)
# Using regex for flexible matching (case insensitivity handled in logic)
replacements = [
    (r"Nossa\s+(?:<[^>]+>)?\s*argamassa\s+baritada", "A argamassa baritada certificada"), 
    (r"nossa\s+(?:<[^>]+>)?\s*argamassa\s+baritada", "a argamassa baritada certificada"),
    (r"Fornecemos", "Nossos parceiros fornecem"),
    (r"fornecemos", "nossos parceiros fornecem"),
    (r"Fabricamos", "Homologamos fabricantes de"),
    (r"fabricamos", "homologamos fabricantes de"),
    (r"Nossos sacos", "Os sacos"),
    (r"nossos sacos", "os sacos"),
]

def update_files():
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                original_content = content
                changed = False
                
                for pattern, replacement in replacements:
                    if re.search(pattern, content):
                        # Simple string replace for safety, or regex sub if needed
                        # Here using replace for exact phrase matches identified
                        content = re.sub(pattern, replacement, content)
                        changed = True
                
                if changed:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"Updated: {file}")
                    count += 1
    
    print(f"Total files updated: {count}")

if __name__ == "__main__":
    update_files()
