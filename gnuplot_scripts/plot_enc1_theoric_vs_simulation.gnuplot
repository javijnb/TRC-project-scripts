set xlabel 'Tráfico ofrecido'
set ylabel 'Tráfico cursado'
set key bottom right
set title 'Tráfico teórico vs simulado - ENC I'

# intervalos
set xrange [39:51]
plot 'gnuplot_files/data_enc1_theoric.plot' with linespoints title 'Tráfico teórico', 'gnuplot_files/data_enc1.plot' with yerrorlines title 'Tráfico simulado'
pause -1