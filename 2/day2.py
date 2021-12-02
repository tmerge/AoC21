# solution of day two of AoC

# get data from input file
with open('input.txt', 'r') as input_file:
    data = input_file.read().splitlines()

# vars of depth and forward movement
forward = 0
depth = 0

# split data to get value and action seperated
for i in data:
    t = i.split(" ")
    # check for action that will be run in next step
    if (t[0] == 'forward'):
        print(t)
        forward = forward + int(t[1])
    if (t[0] == 'down'):
        print(t)
        depth = depth + int(t[1])
    if (t[0] == 'up'):
        depth = depth - int(t[1])

# print and calc result
print(forward * depth)

