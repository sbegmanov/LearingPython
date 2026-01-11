while True:
    reply = input('Enter text: ')
    if reply == 'stop': break
    print(reply.upper())

#  with := assignment expression 
while (reply := input('Enter text: ')) != 'stop':
    print(reply.upper())

# Doing a math
while True:
    reply = input('Enter text integer:')
    if reply == 'stop': break
    print(int(reply) ** 2)
print('Bye')

# Handling error
while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        print(int(reply) ** 2)
print('Bye')

# Handling Errors with try Statements
while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    try:
        num = int(reply)
    except:
        print('Bad!' * 8)
    else:
        print(num ** 2)
print('Bye')

#  If we’re sure that print won’t fail
while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    try:
        print(int(reply) ** 2)
    except:
        print('Bad!' * 8)
print('Bye')

# Supporting Floating-Point Numbers
while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    try:
        print(float(reply) ** 2)
    except:
        print('Bad!' * 8)
print('Bye')

# Nesting Code Three Levels Deep
while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        num = int(reply)
        if num < 20:
            print('low')
        else:
            print(num ** 2)
print('Bye')
