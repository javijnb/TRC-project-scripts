set xlabel 'Tráfico ofrecido'
set ylabel 'Tráfico cursado'
set key bottom right
set title 'Tráfico teórico vs simulado - ENC I'

# intervalos
set xrange [19:26]
plot 'gnuplot_files/data_enc1_trafA_theoric.plot' with linespoints title 'Tráfico teórico de primer salto', 'gnuplot_files/data_enc1_trafA.plot' with yerrorlines title 'Tráfico simulado de primer salto'
pause 7

set xrange [19:26]
plot 'gnuplot_files/data_enc1_trafB_theoric.plot' with linespoints title 'Tráfico teórico de segundo salto', 'gnuplot_files/data_enc1_trafB.plot' with yerrorlines title 'Tráfico simulado de segundo salto'
pause -1