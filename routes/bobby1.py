
# Test input
input1 = {
    "time": [3, 6, 9],
    "prerequisites": [(1, 3), (2, 3)]
}

input2 = {
    "time": [3, 6, 9],
    "prerequisites" : []
}

input3 = {
    'time': [1, 2, 3, 4, 5],
'prerequisites': [(1,2),(3,4),(2,5),(4,5)]
}

print(bobby1(input1['time'], input1['prerequisites']))
print(bobby1(input2['time'], input2['prerequisites']))
print(bobby1(input3['time'], input3['prerequisites']))