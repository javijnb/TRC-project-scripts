set xlabel 'Tráfico ofrecido'
set ylabel 'Tráfico cursado'
set key bottom right
set title 'Tráfico ofrecido sin reserva vs Tráfico ofrecido con reserva de 2 circuitos - ENC III'

# grafica general
set xrange [39:51]
plot 'gnuplot_files/data_enc3.plot' with yerrorlines title 'Tráfico ofrecido sin reserva', 'gnuplot_files/data_enc3_backup.plot' with yerrorlines title 'Tráfico ofrecido con reserva'

pause -1