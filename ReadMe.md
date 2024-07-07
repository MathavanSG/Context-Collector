# Context Collector

Context Collector is a Python script designed to gather and concatenate

Uploading Screen%20Recording%202024-07-07%20at%206.mp4…

 all Python files within a specified directory. This tool is particularly useful for projects with multiple `.py` files spread across various directories, allowing you to compile them into a single file for easier analysis, context gathering, or documentation purposes.

## Features

- **Automated Gathering**: Recursively collects all `.py` files in the specified directory, excluding specified directories such as `env`, `venv`, `__pycache__`, and `site-packages`.
- **Exclusion Handling**: Allows exclusion of specific directories to avoid unwanted files.
- **Concatenation**: Combines the contents of all gathered Python files into a single output file, with each file's content prefixed by its file path.

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MathavanSG/Context-Collector.git
   cd Context-Collector
   ```

2. **Create a Python Script**:
   Create a new Python file (e.g., `context_collector.py`) and paste the following code:

   ```python
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
   ```

3. **Run the Script**:
   Execute the script in your terminal or command prompt:
   ```bash
   python context_collector.py
   ```

4. **Specify the Output File**:
   When prompted, enter the name of the output file (including `.py` extension) where you want to save the concatenated contents. For example:
   ```
   Enter the name of the output file (including .py extension): combined_project.py
   ```

5. **Output**:
   The script will gather all `.py` files from the current working directory and its subdirectories, concatenate their contents, and save them into the specified output file. Each file's content will be prefixed by a comment indicating its original path.

## Explanation of the Code

- **`gather_py_files(directory)`**:
  - Recursively walks through the given directory.
  - Collects paths of all `.py` files, excluding directories specified in `exclude_dirs`.
  - Excludes the script file itself to avoid self-inclusion.

- **`concatenate_files(files, output_file)`**:
  - Opens the specified output file for writing.
  - Reads and writes the content of each gathered `.py` file to the output file.
  - Adds a comment indicating the file path before the content of each file.

- **`main()`**:
  - Prompts the user to enter the name of the output file.
  - Uses the current working directory to gather `.py` files.
  - Calls `gather_py_files()` and `concatenate_files()` to process and save the files.

## Benefits

- **Efficiency**: Eliminates the need for manual copying and pasting of code across multiple files.
- **Context Gathering**: Provides a consolidated view of all your project's Python files, aiding in understanding and documentation.
- **Scalability**: Handles projects with a large number of files and complex directory structures.

## Example Use Case

Imagine you have a project with over 1500 lines of code spread across different `.py` files in various directories. Using Context Collector, you can easily gather all the code into a single file, making it easier to provide a broader context of your project for review, analysis, or documentation.

Feel free to contribute to the project or raise issues if you encounter any problems!

---

If you find this tool useful, consider starring the repository on GitHub!

---

[GitHub Repository](https://github.com/MathavanSG/Context-Collector)
