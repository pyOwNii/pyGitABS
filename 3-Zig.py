import time, sys

indent = 0 #nr of spaces to indent
indentIncreasing = True #Whether the indentation is increase or not.

try:
    while True: #main loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) #Pause for 1/10th of a second

        if indentIncreasing is True:
            #Increase number of spaces:
            indent = indent + 1
            if indent == 20: #change direction
                indentIncreasing = False

        else:
            #decrease number of spaces
            indent = indent - 1
            if indent == 0:     #change direction
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()

