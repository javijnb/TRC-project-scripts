set xlabel 'Trafico ofrecido'
set ylabel 'Trafico cursado'
set key bottom right
set title 'Trafico ofrecido vs cursado - ENC III'

# intervalos
set xrange [19:26]
plot 'gnuplot_files/data_enc3_trafA.plot' with yerrorlines title 'Trafico simple con estimación', 'gnuplot_files/data_enc3_trafB.plot' with yerrorlines title 'Trafico dual con estimación'
pause 7

# grafica general
set xrange [39:51]
plot 'gnuplot_files/data_enc3.plot' with yerrorlines title 'Trafico total con estimación'

pause -1