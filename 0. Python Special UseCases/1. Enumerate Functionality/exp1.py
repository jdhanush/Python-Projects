import glob
import sys
import os


def get_exe_directory():
    if getattr(sys, 'frozen', False):
        # Running as EXE
        return os.path.dirname(sys.executable)
    elif '__file__' in globals():
        # Running as script
        return os.path.dirname(os.path.abspath(__file__))
    else:
        # Running in Spyder / Jupyter
        return os.getcwd()


# Get the current working directory
current_working_dir = get_exe_directory()

all_file_Paths = glob.glob(os.path.join(current_working_dir, "SpectralData[1-5].dat"))

# for f1 in all_file_Paths:
#     print(f"filepath:{f1} and type:{type(f1)}")

    
for iteration, f2 in enumerate(all_file_Paths):
    print(f"{iteration}")
    print(f"filepath:{f2} and type:{type(f2)}")
    
print(__name__)    