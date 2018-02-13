x = 12
if x > 10:
    print("Hello")

y = 12
if x > y:
    print("x>y")
elif x < y:
    print("x<y")
else:
    print("x=y")

for i in range(5):
    print(i)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list1 in list_of_lists:
    for x in list1:
        print(x)

print([27*x for x in range(1, 11)])
