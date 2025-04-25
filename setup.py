import sys
from cx_Freeze import setup, Executable
import os

# Define build options
build_exe_options = {
    "packages": ["cv2", "os"],
    "include_files": [
        ("dnn_model", "dnn_model"),  # Include model files folder
        "gui_buttons.py"             # Include other necessary files
    ]
}

# Setup the cx_Freeze build
setup(
    name="Simple Object Detection Software",
    version="0.1",
    description="This software detects objects in real-time",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base="Console")]
)
