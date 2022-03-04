n = int(input())
list_s = []
i = 0
while i < n :
    x = input()
    list_s.append(x)
    i += 1
for word in list_s:
    if len(word) > 10 :
        print(word[0]+str((len(word)-2))+word[-1])
    else:
        print(word)
