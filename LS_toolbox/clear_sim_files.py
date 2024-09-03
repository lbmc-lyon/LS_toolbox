import os
import re


sim_files_names = ["d3dump", "d3hsp", "d3plot+", "messag", "bndout", "glstat", "spcforc", "elout", "nodout", "part_des",
                   "status\.out", "d3dump+"]

def clear_sim_files(sim_dir_path: str):
    """
    Clear simulation files in the given directory.
    :param sim_dir_path: Path to the simulation directory.
    """
    for sim_file_name in sim_files_names:
        for file in os.listdir(sim_dir_path):
            if os.path.isdir(os.path.join(sim_dir_path, file)):
                continue
            elif re.match(sim_file_name, file):
                os.remove(os.path.join(sim_dir_path, file))