set terminal png size 1920,1080
set xlabel 'Tráfico ofrecido'
set ylabel 'Tráfico cursado'
set key bottom right
set title 'Tráfico ofrecido sin reserva vs Tráfico ofrecido con reserva de 2 circuitos - ENC III'

# grafica general
set output './graph_images/enc3_vs_backup_total.png'
plot 'gnuplot_files/data_enc3.plot' with yerrorlines title 'Tráfico cursado sin reserva', 'gnuplot_files/data_enc3_backup.plot' with yerrorlines title 'Tráfico cursado con reserva'

pause -1