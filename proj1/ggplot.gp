#Styles for grid and border
set style line 100 lc rgb "white" lw 3 #white major grid line
set style line 101 lc rgb "white" lw 1 #white minor grid line
set style line 200 lc rgbcolor "#333333" lw 1 # gray line for tics

# Draw gray graph background
set object 1 rect from graph 0, graph 0 to graph 1, graph 1 
set object 1 behind fc rgbcolor "#d8d8d8" fillstyle solid 1.0 noborder

set border 0 ls 200   # get rid of all border lines
set tics nomirror out # make tics point out
set mxtics 2          # two divisions for minor x tics
set mytics 2          # two divisions for minor y tics

#Set up grid with minor tics and the right line styles
set grid mxtics mytics xtics ytics ls 100, ls 101

#Set the key outside
set key rmargin center Left reverse


