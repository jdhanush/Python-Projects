import glob
import os
from datetime import time as tm
#from time import time


current_wd = os.getcwd()        # gets the current working directory
all_file_Paths = sorted(glob.glob(os.path.join(current_wd, "SpectralData[1-5].dat")))


beam_start_time_list_calc = []      # values stored in this list will be used for calculation
beam_start_time_list_disp = []      # values stored in this list will be used for display



for indfile in all_file_Paths:
    with open(indfile, 'r') as f:
        bulk_lines = f.readlines()
        bulk_lines[1].split()
        
        hh = int(bulk_lines[1].split()[0])
        mm = int(bulk_lines[1].split()[1])
        ss = int(bulk_lines[1].split()[2])
        beam_start_time_calc = tm(hh, mm, ss)  
        beam_start_time_disp = f"{hh}:{mm}:{ss}"
        
        beam_start_time_list_calc.append(beam_start_time_calc)
        beam_start_time_list_disp.append(beam_start_time_disp)
    

# converting time into seconds
beam_start_time_list_sec = [t.hour*3600 + t.minute*60 + t.second for t in beam_start_time_list_calc]  

print("\nFiles detected along with their paths\n")
for indfile in all_file_Paths:
    print(f"{indfile} \ntype:{type(indfile)}")

print(f"\nBeam start time for display: \n{beam_start_time_list_disp}")
print(f"\nBeam start time for calculations: \n{beam_start_time_list_calc}")
print(f"\nBeam start time in seconds: \n{beam_start_time_list_sec}")
    
