import os

def gather_py_files(directory):
    py_files = []
    exclude_dirs = {'env', 'venv', '__pycache__', 'site-packages'}  # Add other directories to exclude if needed
    for root, dirs, files in os.walk(directory):
        # Exclude specified directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file.endswith(".py") and file != os.path.basename(__file__):  # Exclude this script itself
                py_files.append(os.path.join(root, file))
    return py_files

def concatenate_files(files, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file in files:
            with open(file, 'rb') as infile:
                content = infile.read().decode('utf-8', errors='ignore')
                outfile.write(f"# Contents of {file}\n")
                outfile.write(content)
                outfile.write("\n\n")

def main():
    output_file = input("Enter the name of the output file (including .py extension): ")

    if output_file:
        directory = os.getcwd()  # Use the current working directory
        py_files = gather_py_files(directory)
        if py_files:
            concatenate_files(py_files, output_file)
            print(f"All .py files have been concatenated into {output_file}")
        else:
            print("No .py files found in the current directory.")
    else:
        print("Please provide the name of the output file.")

if __name__ == '__main__':
    main()
