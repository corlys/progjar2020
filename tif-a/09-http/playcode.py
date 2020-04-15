strin = 'GET/index.html HTTP/1.1'

strin2 = 'Content-Length: 11'

splits = strin.split('/')
splits2 = strin2.split('Content-Length: ')

print(splits)
print(splits2)
