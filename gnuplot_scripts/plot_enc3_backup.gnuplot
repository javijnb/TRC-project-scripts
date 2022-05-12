set terminal png size 1920,1080
set xlabel 'Tráfico ofrecido'
set ylabel 'Tráfico cursado'
set key bottom right
set title 'Tráfico ofrecido vs cursado - ENC III con reserva'

# intervalos
set output './graph_images/enc3_backup_traffics.png
plot 'gnuplot_files/data_enc3_backup_trafA.plot' with yerrorlines lw 2 title 'Tráfico de 1 salto con estimación', 'gnuplot_files/data_enc3_backup_trafB.plot' with yerrorlines lw 2 title 'Tráfico de 2 saltos con estimación'
pause 1

# grafica general
set output './graph_images/enc3_backup_total.png
plot 'gnuplot_files/data_enc3_backup.plot' with yerrorlines lw 2 title 'Tráfico total con estimación'

pause -1