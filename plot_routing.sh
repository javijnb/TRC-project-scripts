#!/bin/bash

if [[ $1 -eq 1 ]]
then
    gnuplot ./gnuplot_scripts/plot_enc1.gnuplot
elif [[ $1 -eq 2 ]]
then 
    gnuplot ./gnuplot_scripts/plot_enc2.gnuplot
else
    echo "Encaminamiento elegido no válido"
fi