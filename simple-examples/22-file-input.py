def read_txt(line):
    print line
    
with open('./file-sample.txt') as f:
    for line in f :
        read_txt(line)
        
        