import os
folder_structure = {
    "MinGW-QuickSetup": [
        "src",
        "docs/screenshots",
        "tests",
        "build/logs",
        ".vscode"
    ]
}

files_to_create = {
    "MinGW-QuickSetup": [
        "README.md",
        "requirements.txt",
        "Makefile",
        "LICENSE",
        "CONTRIBUTING.md",
        ".gitignore"
    ],
    "MinGW-QuickSetup/src": [
        "main.py",
        "downloader.py",
        "utils.py",
        "main.cpp",
        "installer.cpp",
        "utils.cpp"
    ],
    "MinGW-QuickSetup/docs": [
        "setup_instructions.md"
    ],
    "MinGW-QuickSetup/.vscode": [
        "settings.json",
        "launch.json",
        "tasks.json"
    ],
    "MinGW-QuickSetup/tests": [
        "test_downloader.py",
        "test_installer.cpp"
    ]
}

for base, subfolders in folder_structure.items():
    for subfolder in subfolders:
        folder_path = os.path.join(base, subfolder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")


for folder, files in files_to_create.items():
    for file in files:
        file_path = os.path.join(folder, file)
        with open(file_path, "w") as f:
            if file.endswith(".md"):
                f.write(f"# {file.split('.')[0]}\n")
            elif file.endswith(".cpp"):
                f.write("// C++ source file\n")
            elif file.endswith(".py"):
                f.write("# Python script\n")
            elif file.endswith(".json"):
                f.write("{}")
            print(f"Created file: {file_path}")

print("Folder structure and files created successfully!")
