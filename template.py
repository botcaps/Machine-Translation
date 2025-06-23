# Import necessary libraries
import os                         # For creating directories and working with the file system
from pathlib import Path           # For handling file paths in a clean, cross-platform way
import logging                     # For logging the process of file and directory creation

# Configure logging: INFO level, and a readable log message format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Define the project name (used as the base package folder)
project_name = "Machine_Translation"

# List of all the files and folders you want to create for your project structure
list_of_files = [
    ".github/workflows/.gitkeep",                               # Placeholder file to ensure the workflows directory is tracked by git (for CI/CD)
    f"src/{project_name}/__init__.py",                          # Makes the src/Machine_Translation directory a Python package
    f"src/{project_name}/components/__init__.py",               # Makes the components directory a Python package (for modular code)
    f"src/{project_name}/components/data_ingestion.py",         # Script for data ingestion logic (downloading, reading, etc.)
    f"src/{project_name}/components/data_transformation.py",    # Script for data transformation logic (cleaning, preprocessing)
    f"src/{project_name}/components/model_trainer.py",          # Script for model training logic
    f"src/{project_name}/components/model_monitor.py",          # Script for model monitoring logic (performance, drift, etc.)
    f"src/{project_name}/utils/__init__.py",                    # Makes the utils directory a Python package
    f"src/{project_name}/utils/common.py",                      # Common utility/helper functions used across the project
    f"src/{project_name}/logging/__init__.py",                  # Makes the logging directory a Python package (custom logging logic)
    f"src/{project_name}/config/__init__.py",                   # Makes the config directory a Python package
    f"src/{project_name}/config/configuration.py",              # Script to manage configuration loading and parsing
    f"src/{project_name}/pipeline/__init__.py",                 # Makes the pipeline directory a Python package
    f"src/{project_name}/pipelines/training_pipelines.py",      # Script to define and run training pipelines
    f"src/{project_name}/pipelines/testing_pipelines.py",       # Script to define and run testing pipelines
    f"src/{project_name}/exception.py",                         # Custom exception classes for the project
    f"src/{project_name}/entity/__init__.py",                   # Makes the entity directory a Python package (for data schemas/classes)
    f"src/{project_name}/constants/__init__.py",                # Makes the constants directory a Python package (for constants)
    "config/config.yaml",                                       # Main configuration file for the project (YAML format)
    "params.yaml",                                              # Parameters for model and pipeline (hyperparameters, etc.)
    "app.py",                                                   # Entry point for the web application (Streamlit/Flask)
    "main.py",                                                  # Main script to orchestrate the project (training, prediction, etc.)
    "Dockerfile",                                               # Docker configuration file for containerizing the project
    "requirements.txt",                                         # List of Python dependencies required for the project
    "setup.py",                                                 # Script for installing the package and its dependencies
    "research/trials.ipynb",                                    # Jupyter notebook for research, experiments, and prototyping
]   

# Loop through each file path and create files/folders if they don't already exist
for filepath in list_of_files:
    filepath = Path(filepath)                         # Convert string to Path object for cross-platform support
    filedir, filename = os.path.split(filepath)       # Separate directory path and filename

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)           # Create the directory if it doesn't exist
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create the file if it doesn't exist or if it exists but is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass                                      # Create an empty file (no content yet)
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}")  # Skip creating the file if it already exists with content
