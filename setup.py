import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["cv2", "os"],
    "include_files": [
        ("dnn_model", "dnn_model"),  # include the entire folder
        "gui_buttons.py"             # include your custom module
    ]
}

setup(
    name="Simple Object Detection Software",
    version="0.1",
    description="This software detects objects in realtime",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base="Console")]  # for debug, keep Console base
)
