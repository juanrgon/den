from build.__main__ import build_package, build_package_via_sdist
import argparse
import os

def build(args):
    project_path = args.project_path or os.getcwd()
    output_directory = args.output_directory or os.path.join(project_path, "dist")
    config_settings = {}  # You can customize the config settings if needed.
    no_isolation = False  # Change to True if you don't want to use an isolated environment.
    skip_dependency_check = False  # Change to True if you want to skip the dependency check.

    distributions = []
    if args.sdist:
        distributions.append('sdist')
    if args.wheel:
        distributions.append('wheel')

    if not distributions:
        distributions = ['wheel']
        build_call = build_package_via_sdist
    else:
        build_call = build_package

    try:
        built = build_call(
            project_path, output_directory, distributions, config_settings, not no_isolation, skip_dependency_check
        )
        print(f"Successfully built the project at {project_path}")
        print("Built artifacts:")
        for artifact in built:
            print(f"  {artifact}")
    except Exception as e:
        print(f"Error: {e}")
        print("Failed to build the project.")
