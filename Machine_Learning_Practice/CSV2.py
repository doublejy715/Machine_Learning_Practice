import csv,codecs

filename = "/Users/mac-jjy/Desktop/test.csv"
file = codecs.open(filename,"r")

reader = csv.reader(file,delimiter=",")
for cells in reader:
    print(cells[1],cells[2])
    print()