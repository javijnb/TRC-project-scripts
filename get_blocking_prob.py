import typer
from file_builder import FileBuilder
from utils import Utils

# CONSTANTES GLOBALES
S : int = 120
C : int = 2000000000
q : float = 0.95
r = [1, 0.96, 0.92, 0.88, 0.84, 0.8]
tolerances = [0.002]
my_lambdas = []
A = []

def main(numero_encaminamiento: int, seed: int):

    print(range(1,3))

    # COMPROBAR NUMERO DE ENCAMINAMIENTO VALIDO:
    is_between = numero_encaminamiento in range(1,5)
    if not is_between:
        print("ERROR: No ha introducido un número de encaminamiento válido (1 - 4)")
        return

    typer.echo(f"Ha elegido encaminamiento {numero_encaminamiento} y semilla {seed}")

    # CALCULAMOS TODAS LAS LAMBDAS
    for r_item in r:
        each_lambda = (25 * r_item) / S
        my_lambdas.append(each_lambda)
        A.append(each_lambda * S)

    # SIMULAMOS
    for i in range(len(r)):

        if numero_encaminamiento == 1:
            cfg_file_path = FileBuilder.build_cfg_file_encaminamiento_1(i, my_lambdas[i], S)
            Utils.execute_sim_red(cfg_file_path, seed, tolerances[i], q, False)
            cfg_out_file_destination = Utils.move_cfg_out_file(cfg_file_path, False)

        elif numero_encaminamiento == 2:
            cfg_file_path = FileBuilder.build_cfg_file_encaminamiento_2(i, my_lambdas[i], S)
            Utils.execute_sim_red(cfg_file_path, seed, tolerances[i], q, False)
            cfg_out_file_destination = Utils.move_cfg_out_file(cfg_file_path, False)

        elif numero_encaminamiento == 3:
            cfg_file_path = FileBuilder.build_cfg_file_encaminamiento_3(i, my_lambdas[i], S, False)
            Utils.execute_sim_red(cfg_file_path, seed, tolerances[i], q, False)
            cfg_out_file_destination = Utils.move_cfg_out_file(cfg_file_path, False)

        elif numero_encaminamiento == 4:
            cfg_file_path = FileBuilder.build_cfg_file_encaminamiento_3(i, my_lambdas[i], S, True)
            Utils.execute_sim_red(cfg_file_path, seed, tolerances[i], q, True)
            cfg_out_file_destination = Utils.move_cfg_out_file(cfg_file_path, True)
        
        blocking_probabilities_dict = Utils.parse_cfg_out_file(cfg_out_file_destination)
        highest_blocking_probability = float(Utils.get_max_probability_from_dict(blocking_probabilities_dict))
        if numero_encaminamiento != 4:
            FileBuilder.build_gnuplot_file(i, blocking_probabilities_dict, numero_encaminamiento, A, False)
        else:
            FileBuilder.build_gnuplot_file(i, blocking_probabilities_dict, numero_encaminamiento, A, True)

        # Recalcular probabilidad de bloqueo para la siguiente iteracion
        next_tolerance = ((1-highest_blocking_probability)/highest_blocking_probability)*0.002
        tolerances.append(next_tolerance)


if __name__ == "__main__":
    typer.run(main)
