import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"
list_of_files = [
    ".github/workflows/.gitkeep",                   # GitHub Actions workflow configuration directory.
    f"src/{project_name}/__init__.py",              # Python package marker for the project's source code.
    f"src/{project_name}/components/__init__.py",   # Python package marker for the components subpackage.
    f"src/{project_name}/utils/__init__.py",        # Python package marker for the utils subpackage.
    f"src/{project_name}/utils/common.py",           # Utility functions or classes module.
    f"src/{project_name}/logging/__init__.py",       # Python package marker for the logging subpackage.
    f"src/{project_name}/config/__init__.py",        # Python package marker for the config subpackage.
    f"src/{project_name}/config/configuration.py",   # Configuration settings module.
    f"src/{project_name}/pipeline/__init__.py",      # Python package marker for the pipeline subpackage.
    f"src/{project_name}/entity/__init__.py",        # Python package marker for the entity subpackage.
    f"src/{project_name}/constants/__init__.py",     # Python package marker for the constants subpackage.
    "config/config.yaml",                            # Project configuration settings in YAML format.
    "params.yaml",                                   # Parameters or hyperparameters for the project.
    "app.py",                                        # Application code script.
    "main.py",                                       # Main entry point script.
    "Dockerfile",                                    # Docker container configuration file.
    "requirements.txt",                              # List of required Python packages and versions.
    "setup.py",                                      # Script for packaging and distribution of the project.
    "research/trials.ipynb",                        # Jupyter Notebook for research and experimentation.
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")