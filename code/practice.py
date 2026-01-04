while True:
    reply = input('Enter text: ')
    if reply == 'stop': break
    print(reply.upper())

#  with := assignment expression 
while (reply := input('Enter text: ')) != 'stop':
    print(reply.upper())
