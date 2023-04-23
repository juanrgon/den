import os
import datetime
import re

def prompt(message, default=""):
    return input(f"{message} [{default}]: ") or default

def create_file(path, content=""):
    with open(path, "w") as file:
        file.write(content)

def create_new_project(args):
    print("This utility will walk you through creating a new Python package.")
    print("Press ^C at any time to quit.")

    project_name = args.project_name
    package_name = prompt("Package name:", os.path.basename(project_name))
    version = prompt("Version:", "0.0.1")
    author_name = prompt("Author name:")
    author_email = prompt("Author email:")
    description = prompt("Description:", "A small example package")
    homepage = prompt("Homepage URL:")
    bug_tracker = prompt("Bug tracker URL:")
    src_path = os.path.join(project_name, "src")
    package_path = os.path.join(src_path, package_name)

    os.makedirs(package_path, exist_ok=True)

    create_file(os.path.join(package_path, "__init__.py"))
    create_file(os.path.join(package_path, "example.py"), "def add_one(number):\n    return number + 1\n")

    # Create the tests directory
    os.makedirs(os.path.join(project_name, "tests"), exist_ok=True)

    # Create pyproject.toml
    pyproject_toml_content = f"""[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{package_name}"
version = "{version}"
authors = [
  {{ name="{author_name}", email="{author_email}" }},
]
description = "{description}"
readme = "README.md"
requires-python = ">=3.7"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
"Homepage" = "{homepage.strip()}"
"Bug Tracker" = "{bug_tracker.strip()}"
"""

    # HACK: This is a hack to make sure the pyproject.toml file is valid TOML
    pyproject_toml_content = pyproject_toml_content.replace('"Homepage" = ""', "")
    pyproject_toml_content = pyproject_toml_content.replace('"Bug Tracker" = ""', "")

    pyproject_toml_content.strip()
    create_file(os.path.join(project_name, "pyproject.toml"), pyproject_toml_content)

    # Create README.md
    readme_content = f"""# {package_name}

{description}

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.
"""
    create_file(os.path.join(project_name, "README.md"), readme_content)

    # Create LICENSE
    LICENSE = """Copyright (c) {year} The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
    current_year = datetime.datetime.now().year
    license_content = LICENSE.format(year=current_year)
    create_file(os.path.join(project_name, "LICENSE"), license_content)

    print(f"Successfully created project {project_name} with package {package_name}.")
