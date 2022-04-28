import os
import shutil

output_files_path = "./output_cfg/"

class Utils():
    def get_max_probability_from_dict(blocking_probabilities_dict:dict) -> float:
        blocking_probabilities_list = []
        for traffic in blocking_probabilities_dict:
            blocking_probabilities_list.append(blocking_probabilities_dict[traffic]["Bmin"])
            blocking_probabilities_list.append(blocking_probabilities_dict[traffic]["Bcentral"])
            blocking_probabilities_list.append(blocking_probabilities_dict[traffic]["Bmax"])

        return max(blocking_probabilities_list)

    def parse_cfg_out_file(cfg_out_file_path:str) -> dict:
        f = open(cfg_out_file_path, 'r')
        lines = f.readlines()

        # Trafico A:
        # (Bmin,Bmax): str
        min_max_blocking_values_raw_A = lines[5].split()[3]
        # [Bmin, Bmax]: array
        min_max_blocking_values_A = min_max_blocking_values_raw_A[1:-1].split(",")

        # Trafico B:
        # (Bmin,Bmax): str
        min_max_blocking_values_raw_B = lines[15].split()[3]
        # [Bmin, Bmax]: array
        min_max_blocking_values_B = min_max_blocking_values_raw_B[1:-1].split(",")
        

        blocking_probabilities_dict = {
            "trafico_a": {
                "Bmin": min_max_blocking_values_A[0],
                "Bcentral": lines[4].split()[-1],
                "Bmax": min_max_blocking_values_A[1]
            },
            "trafico_b": {
                "Bmin": min_max_blocking_values_B[0],
                "Bcentral": lines[14].split()[-1],
                "Bmax": min_max_blocking_values_B[1]
            }
        }
        return blocking_probabilities_dict

    def execute_sim_red(config_file_path:str, seed:int, tolerance:float, q:float, backup:bool):
        if backup:
            command = "./SimRedMMkk -s "+str(seed)+" -q "+str(q)+" -t "+str(tolerance)+" -n 2 -a "+config_file_path
        else:
            command = "./SimRedMMkk -s "+str(seed)+" -q "+str(q)+" -t "+str(tolerance)+" -a "+config_file_path
        os.system(command)
    

    def move_cfg_out_file(config_file_path:str, backup:bool) -> str:
        # config_file_path = ./input_cfg/encX_rY.cfg

        if backup:
            source = config_file_path + ".2k.out"
        else:
            source = config_file_path + ".out"

        directories = source.split("/")
        directories[1] = output_files_path
        destination = "/".join(directories)
        shutil.move(source, destination)
        return destination