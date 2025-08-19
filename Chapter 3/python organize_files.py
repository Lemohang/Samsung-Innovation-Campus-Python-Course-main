import os
import shutil
from collections import defaultdict

# 📂 Folder you want to organize
source_folder = r"C:\Users\QUEEN ACCA\Desktop"   # change this to your folder

# Define where each type of file should go
file_mappings = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Programs": [".exe", ".msi"],
    "Python Scripts": [".py"],  # ✅ Custom category
}

# Add a Misc folder for uncategorized files
misc_folder = "Misc"
file_mappings[misc_folder] = []

# Create folders if they don’t exist
for folder in file_mappings.keys():
    folder_path = os.path.join(source_folder, folder)
    os.makedirs(folder_path, exist_ok=True)

# Track summary
summary = defaultdict(int)

# Organize files
for file_name in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file_name)

    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file_name)
        ext = ext.lower()

        moved = False
        for folder, extensions in file_mappings.items():
            if ext in extensions:
                shutil.move(file_path, os.path.join(source_folder, folder, file_name))
                print("Moved {} → {}".format(file_name, folder))
                summary[folder] += 1
                moved = True
                break

        if not moved:  # goes to Misc
            shutil.move(file_path, os.path.join(source_folder, misc_folder, file_name))
            print("Moved {} → {}".format(file_name, misc_folder))
            summary[misc_folder] += 1

# Print summary
print("\n📊 Summary:")
for folder, count in summary.items():
    print("- {}: {} file(s)".format(folder, count))

print("\n✅ Organization complete!")
