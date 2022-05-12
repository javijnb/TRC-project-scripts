set xlabel 'Tráfico ofrecido'
set ylabel 'Tráfico cursado'
set key bottom right
set title 'Tráfico ofrecido vs cursado - ENC II'

# intervalos
plot 'gnuplot_files/data_enc2_trafA.plot' with yerrorlines title 'Tráfico de 1 salto con estimación', 'gnuplot_files/data_enc2_trafB.plot' with yerrorlines title 'Tráfico de 2 saltos con estimación'
pause 7

# grafica general
plot 'gnuplot_files/data_enc2.plot' with yerrorlines title 'Tráfico total con estimación'

pause -1