# Aaaa aaaaB
result = 0
t = input('')
l = []
word = t[0]
for i in range(1,len(t)):
    if t[i].isupper():
        l.append(word)
        word = t[i]
    else:
        word += t[i]
if word:
    l.append(word)

#print(l)

for i in range(len(l)-1):
    if len(l[i]) % 4 != 0:
        result += (4 - (len(l[i]) % 4))
        #print(f'kk ${result}')

print(result)