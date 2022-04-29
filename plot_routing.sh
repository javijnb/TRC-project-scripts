#!/bin/bash
echo "------------------------------------------------------------------------------"
echo "-                              GRÁFICAS BÁSICAS                              -"
echo "------------------------------------------------------------------------------"
echo ""
echo "1) ENC I - Tráficos simples y duales. Tráfico total ofrecido vs cursado"
echo "2) ENC II - Tráficos simples y duales. Tráfico total ofrecido vs cursado"
echo "3) ENC III - - Tráficos simples y duales. Tráfico total ofrecido vs cursado"
echo "4) ENC III con reserva de 2 circuitos - Tráficos simples y duales. Tráfico total ofrecido vs cursado"
echo ""
echo "------------------------------------------------------------------------------"
echo "-                            GRÁFICAS ALTERNATIVAS                           -"
echo "------------------------------------------------------------------------------"
echo ""
echo "5) ENC I - Tráfico teórico vs tráfico simulado para tráficos de primer y segundo salto"
echo "6) ENC III - Simulación sin reserva vs simulación con reserva"
echo ""
echo -n "Introduzca el número de la opción que desea: "
read VAR

if [[ $VAR -eq 1 ]]
then
    gnuplot ./gnuplot_scripts/plot_enc1.gnuplot
elif [[ $VAR -eq 2 ]]
then
   gnuplot ./gnuplot_scripts/plot_enc2.gnuplot
elif [[ $VAR -eq 3 ]]
then
    gnuplot ./gnuplot_scripts/plot_enc3.gnuplot
elif [[ $VAR -eq 4 ]]
then
    gnuplot ./gnuplot_scripts/plot_enc3_backup.gnuplot
elif [[ $VAR -eq 5 ]]
then
    gnuplot ./gnuplot_scripts/plot_enc1_theoric_vs_simulation.gnuplot
elif [[ $VAR -eq 6 ]]
then
    gnuplot ./gnuplot_scripts/plot_enc3_vs_backup.gnuplot
else
    echo "No ha seleccionado una opción disponible"
fi

