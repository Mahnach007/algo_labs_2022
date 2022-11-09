n = int(input("Enter pairs:"))
pairs = []
for _ in range(n):
    x, y = input(),  input()
    pairs.append((x, y))

u = 0
new_set = set()
new_list = []
for i in range(len(pairs) - 1):
    for j in range(i + 1, len(pairs)):
        if (int(pairs[i][1]) - int(pairs[j][0])) % 2 == 1:
            new_list.append([pairs[i][1],pairs[j][0]])
            #print(pairs[i][1], pairs[j][0])
            u += 1
        if (int(pairs[i][1]) - int(pairs[j][1])) % 2 == 1:
            new_list.append([pairs[i][1],pairs[j][1]])
            #print(pairs[i][1], pairs[j][1])
            u += 1

for i in new_list:
    a = tuple(i)
    new_set.add(a)
print("List ", len(new_list))
print("Set ", len(new_set))
