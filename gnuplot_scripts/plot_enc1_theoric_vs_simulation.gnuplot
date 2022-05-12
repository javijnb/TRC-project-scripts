set xlabel 'Tráfico ofrecido'
set ylabel 'Tráfico cursado'
set key bottom right
set title 'Tráfico teórico vs simulado - ENC I'

# intervalos
plot 'gnuplot_files/data_enc1_trafA_theoric.plot' with linespoints title 'Tráfico ofrecido teórico de 1 salto', 'gnuplot_files/data_enc1_trafA.plot' with yerrorlines lw 2 title 'Tráfico ofrecido simulado de 1 salto'
pause -1

plot 'gnuplot_files/data_enc1_trafB_theoric.plot' with linespoints title 'Tráfico ofrecido teórico de 2 saltos', 'gnuplot_files/data_enc1_trafB.plot' with yerrorlines lw 2 title 'Tráfico ofrecido simulado de 2 saltos'
pause -1

plot 'gnuplot_files/data_enc1_theoric.plot' with linespoints title 'Tráfico ofrecido total (Valor teórico)', 'gnuplot_files/data_enc1.plot' with yerrorlines lw 2 title 'Tráfico ofrecido total (Simulación)'
pause -1