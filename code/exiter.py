import sys

def bye():
    sys.exit(62)            # Crucial error: abort now!
try:
    bye()
except:
    print('Got it')         # Oops--we ignored the exit
    print('Continuing...')

# Normally, sys.exit(62) terminates the program. But the empty except catches SystemExit, so the program continues.