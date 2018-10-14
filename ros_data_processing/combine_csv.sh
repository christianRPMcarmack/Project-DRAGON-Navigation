head -1 file1.csv > final.csv

for filename in $(ls file*.csv); do sed 1d $filename >> final.csv; done

