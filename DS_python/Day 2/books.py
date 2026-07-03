books = [8, 5, 3, 6]

for i in range(len(books)):
    for j in range(len(books)-1-i):
        if books[j] > books[j+1]:
            books[j], books[j+1] = books[j+1], books[j]

print(books)    