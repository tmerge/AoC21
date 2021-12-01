# solution of day 1 of AoC

# load measurment data from input file
with open('input.txt','r') as input_file:
    data = input_file.read().splitlines()

counter = 0
prev = data[0]

for i in data:
    print('i: ' + i + 'prev:' + prev)
    if i > prev:
        counter = counter + 1
    prev = i
    #TOODO: find bug why programm check only 1297 instead of 1298 increased measurements
print(counter)

