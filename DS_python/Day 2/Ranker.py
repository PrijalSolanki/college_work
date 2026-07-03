marks = [65, 90, 72, 85]

for i in range(len(marks)):
    max_index = i

    for j in range(i + 1, len(marks)):
        if marks[j] > marks[max_index]:
            max_index = j

    marks[i], marks[max_index] = marks[max_index], marks[i]

print(marks)