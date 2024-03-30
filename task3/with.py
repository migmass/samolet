with open('file.txt', 'w') as  file:
          file.write('Hello, world!2')
          
          
with open("q.txt", "r") as f:
    content = f.read()
    
with open("scr.txt", "r") as f1, open("desc.txt", "w") as f2:
    f2.write(f1.read())
    
    