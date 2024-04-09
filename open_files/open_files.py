count = 0
files = []
while True:
    count += 1
    print(f'File has been opened {count} times.')
    files.append(open("somefile.txt"))
    
