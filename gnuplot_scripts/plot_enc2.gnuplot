set terminal png size 1920,1080
set xlabel 'Tráfico ofrecido'
set ylabel 'Tráfico cursado'
set key bottom right
set title 'Tráfico ofrecido vs cursado - ENC II'

# intervalos
set output './graph_images/enc2_traffics.png'
plot 'gnuplot_files/data_enc2_trafA.plot' with yerrorlines title 'Tráfico de 1 salto con estimación', 'gnuplot_files/data_enc2_trafB.plot' with yerrorlines title 'Tráfico de 2 saltos con estimación'
pause 1

# grafica general
set output './graph_images/enc2_total.png'
plot 'gnuplot_files/data_enc2.plot' with yerrorlines title 'Tráfico total con estimación'

pause -1