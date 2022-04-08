from multiprocessing.connection import wait
from time import sleep
import typer
import os
import shutil

# CONSTANTES GLOBALES
S : int = 120
C : int = 2000000000
q : float = 0.95
r = [1, 0.96, 0.92, 0.88, 0.84, 0.8]
tolerances = [0.002]
my_lambdas = []
A = []
input_files_path = "./input_cfg/"
output_files_path = "./output_cfg/"
gnuplot_files_path = "./gnuplot_files/"

def main(numero_encaminamiento: int, seed: int):

    typer.echo(f"Ha elegido encaminamiento {numero_encaminamiento} y semilla {seed}")

    # CALCULAMOS TODAS LAS LAMBDAS
    for r_item in r:
        each_lambda = (25 * r_item) / S
        my_lambdas.append(each_lambda)
        A.append(each_lambda * S)

    # ENCAMINAMIENTO 1
    if numero_encaminamiento == 1:

        for i in range(len(r)):

            cfg_file_path = build_cfg_file_encaminamiento_1(i, my_lambdas[i])
            execute_sim_red(cfg_file_path, seed, tolerances[i])
            cfg_out_file_destination = move_cfg_out_file(cfg_file_path)
            blocking_probabilities_dict = parse_cfg_out_file(cfg_out_file_destination)
            highest_blocking_probability = float(get_max_probability_from_dict(blocking_probabilities_dict))
            build_gnuplot_file(i, blocking_probabilities_dict, numero_encaminamiento)

            # Recalcular probabilidad de bloqueo para la siguiente iteracion
            next_tolerance = ((1-highest_blocking_probability)/highest_blocking_probability)*0.002
            tolerances.append(next_tolerance)


    # INVOCACION INCORRECTA
    else:
        typer.echo(f"El encaminamiento que ha escogido no existe")


#################################
#                               #
#         U T I L E S           #
#                               #
#################################

def build_cfg_file_encaminamiento_1(iteration:int, current_lambda:float) -> str:
    file_name = "enc1_r"+str(iteration)+".cfg"
    absolute_file_path = input_files_path + file_name
    f = open(absolute_file_path, "w")

    # CABECERA
    f.write("50 50 50 50\n")
    f.write("8\n")
    f.write("\n")

    # TRAFICOS
    arrivals = 1/current_lambda

    for i in range(4):
        f.write("M "+str(arrivals)+"\n")
        f.write("M "+str(S)+"\n")
        f.write(str(i)+" a\n")
        f.write("\n")

    for i in range(4):
        f.write("M "+str(2*arrivals)+"\n")
        f.write("M "+str(S)+"\n")
        if i != 3:
            f.write(str(i)+","+str(i+1)+" b\n")
        else:
            f.write(str(i)+","+str(0)+" b\n")
        f.write("\n")

    f.close()

    return absolute_file_path


def execute_sim_red(config_file_path:str, seed:int, tolerance:float):
    command = "./SimRedMMkk -s "+str(seed)+" -q "+str(q)+" -t "+str(tolerance)+" -a "+config_file_path
    os.system(command)
    

def move_cfg_out_file(config_file_path:str) -> str:
    # config_file_path = ./input_cfg/encX_rY.cfg
    source = config_file_path + ".out"
    directories = source.split("/")
    directories[1] = output_files_path
    destination = "/".join(directories)
    shutil.move(source, destination)
    return destination


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

def get_max_probability_from_dict(blocking_probabilities_dict:dict) -> float:
    blocking_probabilities_list = []
    for traffic in blocking_probabilities_dict:
        blocking_probabilities_list.append(blocking_probabilities_dict[traffic]["Bmin"])
        blocking_probabilities_list.append(blocking_probabilities_dict[traffic]["Bcentral"])
        blocking_probabilities_list.append(blocking_probabilities_dict[traffic]["Bmax"])

    return max(blocking_probabilities_list)


def build_gnuplot_file(iteration:int, blocking_probabilities_dict:dict, numero_encaminamiento:int):
    file_name = "data_enc"+str(numero_encaminamiento)+".plot"
    file_path = gnuplot_files_path + file_name
    if iteration == 0:
        f = open(file_path, 'w')
    else:
        f = open(file_path, 'a')

    f.write(str(A[iteration])+" ")

    for traffic in blocking_probabilities_dict:
        Ac_max = A[iteration]*(1-float(blocking_probabilities_dict[traffic]["Bmin"]))
        Ac_central = A[iteration]*(1-float(blocking_probabilities_dict[traffic]["Bcentral"]))
        Ac_min = A[iteration]*(1-float(blocking_probabilities_dict[traffic]["Bmax"]))
        traficos_cursados = [str(Ac_min), str(Ac_central), str(Ac_max)]
        f.write(" ".join(traficos_cursados)+" "
        )

    f.write("\n")


if __name__ == "__main__":
    typer.run(main)
