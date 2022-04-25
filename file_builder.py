from array import array


input_files_path = "./input_cfg/"
gnuplot_files_path = "./gnuplot_files/"

class FileBuilder():

    def build_cfg_file_encaminamiento_1(iteration:int, current_lambda:float, S:int) -> str:

        """
        Creates a new file (or overwrites the existing one) for the specified iteration to store the configuration data for the first routing
        """

        file_name = "enc1_r"+str(iteration)+".cfg"
        absolute_file_path = input_files_path + file_name
        f = open(absolute_file_path, "w")

        # CABECERA
        f.write("50 50 50 50\n")
        f.write("8\n")
        f.write("\n")

        # TRAFICOS
        arrivals = 1/current_lambda

        # Ruta de 1 salto
        for i in range(4):
            f.write("M "+str(arrivals)+"\n")
            f.write("M "+str(S)+"\n")
            f.write(str(i)+" a\n")
            f.write("\n")

        # Ruta dextrógira de 2 saltos
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
    
    def build_cfg_file_encaminamiento_2(iteration:int, current_lambda:float, S:int) -> str:

        """
        Creates a new file (or overwrites the existing one) for the specified iteration to store the configuration data for the second routing
        """

        file_name = "enc2_r"+str(iteration)+".cfg"
        absolute_file_path = input_files_path + file_name
        f = open(absolute_file_path, "w")

        # CABECERA
        f.write("50 50 50 50\n")
        f.write("8\n")
        f.write("\n")

        # TRAFICOS
        arrivals = 1/current_lambda

        # Ruta de 1 salto
        for i in range(4):
            f.write("M "+str(arrivals)+"\n")
            f.write("M "+str(S)+"\n")
            f.write(str(i)+" a\n")
            f.write("\n")

        # Ruta dextrógira de 2 saltos
        # De no poder ser, ruta levógira de 2 saltos
        for i in range(4):
            f.write("M "+str(2*arrivals)+"\n")
            f.write("M "+str(S)+"\n")
            if i == 0:
                f.write("0,1 3,2 b\n")
            elif i == 1:
                f.write("1,2 0,3 b\n")
            elif i == 2:
                f.write("2,3 1,0 b\n")
            elif i == 3:
                f.write("3,0 2,1 b\n")
            f.write("\n")

        f.close()

        return absolute_file_path

    def build_cfg_file_encaminamiento_3(iteration:int, current_lambda:float, S:int) -> str:

        """
        Creates a new file (or overwrites the existing one) for the specified iteration to store the configuration data for the third routing
        """

        file_name = "enc3_r"+str(iteration)+".cfg"
        absolute_file_path = input_files_path + file_name
        f = open(absolute_file_path, "w")

        # CABECERA
        f.write("50 50 50 50\n")
        f.write("8\n")
        f.write("\n")

        # TRAFICOS
        arrivals = 1/current_lambda

        # Ruta de 1 salto
        # De no poder ser, ruta en sentido contrario
        for i in range(4):
            f.write("M "+str(arrivals)+"\n")
            f.write("M "+str(S)+"\n")

            if i == 0:
                f.write("0 3,2,1 a\n")
            elif i == 1:
                f.write("1 0,3,2 a\n")
            elif i == 2:
                f.write("2 1,0,3 a\n")
            elif i == 3:
                f.write("3 2,1,0 a\n")
            
            f.write("\n")

        # Ruta dextrógira de 2 saltos
        # De no poder ser, ruta levógira de 2 saltos
        for i in range(4):
            f.write("M "+str(2*arrivals)+"\n")
            f.write("M "+str(S)+"\n")
            if i == 0:
                f.write("0,1 3,2 b\n")
            elif i == 1:
                f.write("1,2 0,3 b\n")
            elif i == 2:
                f.write("2,3 1,0 b\n")
            elif i == 3:
                f.write("3,0 2,1 b\n")
            f.write("\n")

        f.close()

        return absolute_file_path

    def build_gnuplot_file(iteration:int, blocking_probabilities_dict:dict, numero_encaminamiento:int, A):

        """
        Creates a new file (or overwrites the existing one) for the specified iteration to store the configuration data for the second routing
        """

        file_name_trafA = "data_enc"+str(numero_encaminamiento)+"_trafA.plot"
        file_name_trafB = "data_enc"+str(numero_encaminamiento)+"_trafB.plot"
        file_name_overall = "data_enc"+str(numero_encaminamiento)+".plot"

        file_path_trafA = gnuplot_files_path + file_name_trafA
        file_path_trafB = gnuplot_files_path + file_name_trafB
        file_path_overall = gnuplot_files_path + file_name_overall

        if iteration == 0:
            f_A = open(file_path_trafA, 'w')
            f_B = open(file_path_trafB, 'w')
            f_overall = open(file_path_overall, 'w')

            f_A.write("# Trafico A\n")
            f_B.write("# Trafico B\n")
            f_overall.write('# Trafico total\n')
        else:
            f_A = open(file_path_trafA, 'a')
            f_B = open(file_path_trafB, 'a')
            f_overall = open(file_path_overall, 'a')

        Ac_max_overall = 0
        Ac_central_overall = 0
        Ac_min_overall = 0
        
        for traffic in blocking_probabilities_dict:

            if traffic == "trafico_a":
                f = f_A
            elif traffic == "trafico_b":
                f = f_B
            
            # Escribir los datos del tráfico particular
            f.write(str(A[iteration])+" ")
            Ac_max = A[iteration]*(1-float(blocking_probabilities_dict[traffic]["Bmin"]))
            Ac_central = A[iteration]*(1-float(blocking_probabilities_dict[traffic]["Bcentral"]))
            Ac_min = A[iteration]*(1-float(blocking_probabilities_dict[traffic]["Bmax"]))
            traficos_cursados = [str(Ac_central), str(Ac_min), str(Ac_max)]
            f.write(" ".join(traficos_cursados)+" \n")

            # Guardar los datos totales de los tráficos en un único fichero (overall)
            Ac_max_overall += Ac_max
            Ac_central_overall += Ac_central
            Ac_min_overall += Ac_min
        
        trafico_total_ofrecido = 2*(float(A[iteration]))
        traficos_totales = [str(trafico_total_ofrecido), str(Ac_central_overall), str(Ac_min_overall), str(Ac_max_overall)]
        f_overall.write(" ".join(traficos_totales)+" \n")