import classfile as clsf
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
filepath = glob.glob(os.path.join(current_working_dir, "SpectralData1.dat"))[0]


def run_plot():
    O1 = clsf.DataExtractorClass(filepath)
    x = O1.firstline[:100]
    y = O1.secondline[:100]
          
      
    O2 = clsf.PlottingClass(x, y)
    O2.plotfunc()    


    
