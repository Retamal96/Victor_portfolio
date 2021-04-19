
count =0
with open('Tweet.txt') as f:
    for letter in f:
        count += 1
    print('Line count', count)

f2 = open('Tweet.txt')
f2 =  f2.read()
print(len(f2 ))

for line in f2:
    if '1' not in line:
        continue
    print(line)

for line in f2:
    line = line.strip()
    if line.startswith('I'):
        print(line)


fname = input('Enter the name of the file: ')
search = input('What do you want to search for?\n')
try:
    fhand = open(fname)
except:
    print('File not opened: ', fname)
    quit()


count = 0
for line in fhand:
    if line.startswith("search"):
        count +=1
print(f'The total count for  lines starting with {search} was {count}')
