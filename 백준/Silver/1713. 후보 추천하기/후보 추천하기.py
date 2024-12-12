N = int(input())
counts = int(input())
recomendations = list(map(int, input().split()))

photos = []
for i in range(counts):
    student_num = recomendations[i]
    
    for idx in range(len(photos)):
        if photos[idx][2] == student_num:
            photos[idx][0] += 1     
            break
    else:
        if len(photos) < N:
            photos.append([1, i, student_num])
        else:
            photos.sort(key=lambda x: (x[0], x[1]))
            photos[0] = [1, i, student_num]

photos.sort(key=lambda x:x[2])
print(*[photo[2] for photo in photos])