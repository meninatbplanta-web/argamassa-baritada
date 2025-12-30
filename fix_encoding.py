import os
import glob

directory = r"c:\Users\User\Desktop\github\argamassa-baritada"
files = glob.glob(os.path.join(directory, "*.html"))

print(f"Found {len(files)} HTML files.")

for filepath in files:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # The key logic: reverse the Windows-1252 misinterpretation
        # We assume the content is currently "Double Encoded"
        # i.e., correct UTF-8 bytes were read as cp1252, resulting in garbage chars, then saved as UTF-8.
        # To fix: take the garbage string -> encode to bytes using cp1252 (recovering the original UTF-8 bytes) -> decode as utf-8.
        
        fixed_content = content.encode("cp1252").decode("utf-8")
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(fixed_content)
            
        print(f"Fixed: {os.path.basename(filepath)}")
        
    except UnicodeEncodeError:
        print(f"Skipped (Not cp1252 consistent): {os.path.basename(filepath)}")
    except UnicodeDecodeError:
        print(f"Skipped (Not valid UTF-8 after fix): {os.path.basename(filepath)}")
    except Exception as e:
        print(f"Error on {os.path.basename(filepath)}: {e}")
