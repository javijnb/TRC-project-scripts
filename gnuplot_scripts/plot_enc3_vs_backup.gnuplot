set terminal png size 1920,1080
set xlabel 'Tráfico ofrecido'
set ylabel 'Tráfico cursado'
set key top left
set title 'Tráfico ofrecido sin reserva vs Tráfico ofrecido con reserva de 2 circuitos - ENC III'

# grafica de traficos
set output './graph_images/enc3_vs_backup_traffics.png'
plot 'gnuplot_files/data_enc3_trafA.plot' with yerrorlines lt rgb 'light-green' lw 2 title 'Tráfico cursado de 1 salto sin reserva', 'gnuplot_files/data_enc3_backup_trafA.plot' with yerrorlines lt rgb 'dark-green' lw 2 title 'Tráfico cursado de 1 salto con reserva', 'gnuplot_files/data_enc3_trafB.plot' with yerrorlines lt rgb 'violet' lw 2 title 'Tráfico cursado de 2 saltos sin reserva', 'gnuplot_files/data_enc3_backup_trafB.plot' with yerrorlines lt rgb 'dark-violet' lw 2 title 'Tráfico cursado de 2 saltos con reserva'
pause 1

# grafica general
set output './graph_images/enc3_vs_backup_total.png'
plot 'gnuplot_files/data_enc3.plot' with yerrorlines lw 2 title 'Tráfico cursado sin reserva', 'gnuplot_files/data_enc3_backup.plot' with yerrorlines lw 2 title 'Tráfico cursado con reserva'

pause -1