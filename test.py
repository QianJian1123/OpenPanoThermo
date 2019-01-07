import os,sys
print(sys.argv[1])
files = os.listdir(sys.argv[1])
command='./image-stitching ' 
for num,file in enumerate(files):
    print(num,file)
    command+=' {}/{}'.format(sys.argv[1],file)
#print(command)
os.system(command)












