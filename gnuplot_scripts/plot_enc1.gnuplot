set xlabel 'Tráfico ofrecido'
set ylabel 'Tráfico cursado'
set key bottom right
set title 'Tráfico ofrecido vs cursado - ENC I'

# intervalos
set xrange [19:26]
plot 'gnuplot_files/data_enc1_trafA.plot' with yerrorlines title 'Tráfico simple con estimación', 'gnuplot_files/data_enc1_trafB.plot' with yerrorlines title 'Tráfico dual con estimación'
pause 7

# grafica general
set xrange [39:51]
plot 'gnuplot_files/data_enc1.plot' with yerrorlines title 'Tráfico total con estimación'

pause -1