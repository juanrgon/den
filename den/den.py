#!/usr/bin/env python3

import argparse
import sys
from den.new import create_new_project
from den.build import build
from den.check import check

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        check(sys.argv[2:])

    parser = argparse.ArgumentParser(description="A Python package manager and build tool")
    subparsers = parser.add_subparsers(help="Sub-commands", dest="command")

    # Build command
    parser_build = subparsers.add_parser("build", help="Build the Python package")
    parser_build.add_argument("project_path", nargs="?", help="The path to the project.")
    parser_build.add_argument("--output-directory", help="The directory to store the built package.")
    parser_build.add_argument("--sdist", action="store_true", help="Build a source distribution.")
    parser_build.add_argument("--wheel", action="store_true", help="Build a wheel distribution.")

    # Check command
    parser_check = subparsers.add_parser("check", help="Lint the package with ruff")

    # Doc command
    parser_doc = subparsers.add_parser("doc", help="Build the package's documentation")

    # New command
    parser_new = subparsers.add_parser("new", help="Create a new Python project")
    parser_new.add_argument("project_name", help="The name of the project")

    # Init command
    parser_init = subparsers.add_parser("init", help="Create a new Python package in an existing directory")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add dependencies to the pyproject.toml")
    parser_add.add_argument("dependencies", nargs="+", help="Dependencies to add")

    # Test command
    parser_test = subparsers.add_parser("test", help="Run the tests")

    # Update command
    parser_update = subparsers.add_parser("update", help="Update dependencies")

    # Publish command
    parser_publish = subparsers.add_parser("publish", help="Publish this Python package on PyPI")

    # Install command
    parser_install = subparsers.add_parser("install", help="Install the package")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if args.command == "build":
        # Import and call build function
        build(args)
    elif args.command == "doc":
        # Import and call doc function
        pass
    elif args.command == "new":
        # Import and call new function
        create_new_project(args)
    elif args.command == "init":
        # Import and call init function
        pass
    elif args.command == "add":
        # Import and call add function
        pass
    elif args.command == "test":
        # Import and call test function
        pass
    elif args.command == "update":
        # Import and call update function
        pass
    elif args.command == "publish":
        # Import and call publish function
        pass
    elif args.command == "install":
        # Import and call install function
        pass
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
