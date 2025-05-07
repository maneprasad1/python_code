
ip =[{'key':{'subkey':1}}, {'key':{'subkey':10}}, {'key':{'subkey':5}}]

i = sorted(ip,key = lambda x : x['key']['subkey'], reverse = True)
print(i)
