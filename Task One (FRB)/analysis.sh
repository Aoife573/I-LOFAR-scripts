awk 'NR!=1{if ($3<8000000) print $0}' SMC021_008D1.pls | sort -gr -k4 | head -20
awk 'NR!=1{if ($1>200 && $1<500 && $3<8000000) print $0}' SMC021_008D1.pls | sort -gr -k4 | head -60| awk '{print $1,$4}'

gnuplot
set ylabel "DM (pc/cc)"
set xlabel "S/N"
plot "ch_file" u 1:2:(1.0) wi ye title "S/N vs DM"

awk 'NR!=1{if ($3<8000000) print $0}' 6.pls | sort -gr -k4 | head -1
