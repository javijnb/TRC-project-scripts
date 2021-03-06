# TRC-project-scripts
TRC scripts to automate simulation tasks

## Descripción
Este repositorio contiene todas las herramientas para automatizar las tareas de creación de ficheros de simulación, así como la obtención de los datos de salida y la creación de ficheros para graficar posteriormente en gnuplot

## Funcionamiento
Para ejecutarlo:

~~~
python3 get_blocking_prob.py [numero de encaminamiento] [semilla del simulador]
~~~

Ambos parámetros son obligatorios

## Directorios
- `input_cfg`: contiene los ficheros de entrada para el simulador SimRedMMkk acorde a los parámetros del enunciado del proyecto 21/22
- `output_cfg`: almecanará los ficheros de salida devueltos por el simulador a partir de los ficheros de entrada del directorio anterior
- `gnuplot_cfg`: almacenará los ficheros con los datos a graficar por gnuplot. En caso de ordenar simular una misma configuración, los ficheros correspondientes serán sobreescritos
- `gnuplot_scripts`: almacenará los ficheros .gnuplot que contienen las instrucciones para mostrar por pantalla las gráficas

## Scripts
- `clean_cfg_files.sh`: script shell para eliminar todos los ficheros que haya en las carpetas mencionadas en el apartado anterior. Usar con cuidado, los ficheros serán eliminados permanentemente.
Funcionamiento:
~~~
chmod +x clean_cfg_files.sh
./clean_cfg_files.sh
~~~

- `plot_routing.sh`: script para graficar los datos obtenidos con la herramienta Gnuplot. Las gráficas serán aquellas indicadas en los ficheros `plot_encX.gnuplot` en el directorio `gnuplot_scripts`. 
Funcionamiento:
~~~
chmod +x plot_routing.sh
./plot_routing.sh
~~~
Tras su ejecución, se abrirá un menú de opciones a elegir.
