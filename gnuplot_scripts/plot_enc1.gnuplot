set terminal png size 1920,1080
set xlabel 'Tráfico ofrecido'
set ylabel 'Tráfico cursado'
set key bottom right
set title 'Tráfico ofrecido vs cursado - ENC I'

# intervalos
set output './graph_images/enc1_traffics.png'
plot 'gnuplot_files/data_enc1_trafA.plot' with yerrorlines lw 2 title 'Tráfico de 1 salto con estimación', 'gnuplot_files/data_enc1_trafB.plot' with yerrorlines lw 2 title 'Tráfico de 2 saltos con estimación'
pause 1

# grafica general
set output './graph_images/enc1_total.png'
plot 'gnuplot_files/data_enc1.plot' with yerrorlines lw 2 title 'Tráfico total con estimación'

pause -1