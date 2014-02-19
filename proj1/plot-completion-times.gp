#set term postscript eps color enhanced size 5,2.5 16 solid
set term png size 600,400 #fsize 11 linewidth 1

set key autotitle columnheader
load 'ggplot.gp'
load 'brewer-set1.gp'

set border 3
set tics nomirror

set xlabel 'Time Since First HIT (hours)'
set ylabel 'Completed HITs'

set output 'completion_times.png'
set grid

unset key

plot 'comp_times.dat' using 1:0 with l ls 1 lw 4

