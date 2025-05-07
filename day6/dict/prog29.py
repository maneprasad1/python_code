
ip = {'S 001':['Math', 'Science'], 'S 002':['Math','English'], 
'S 3':['Math','English'], 'S3':['English']}

ip = {k.replace(" ",""):v for k,v in ip.items()}
print(ip)
