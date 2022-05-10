set xlabel 'Tráfico ofrecido'
set ylabel 'Tráfico cursado'
set key bottom right
set title 'Tráfico ofrecido vs cursado - ENC I'

# intervalos
plot 'gnuplot_files/data_enc1_trafA.plot' with yerrorlines title 'Tráfico simple con estimación', 'gnuplot_files/data_enc1_trafB.plot' with yerrorlines title 'Tráfico dual con estimación'
pause 7

# grafica general
plot 'gnuplot_files/data_enc1.plot' with yerrorlines title 'Tráfico total con estimación'

pause -1