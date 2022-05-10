import sys, time
indent = 0
indent_Increasing = True

try:
    while True: #Main Program loop
        print(" " * indent, end="")
        print("********")
        time.sleep(0.1)

        if indent_Increasing:
            #increase the number of spaces:
            indent += 1
            if indent == 20:
                indent_Increasing = False

        else:
            indent -= 1
            if indent == 0:
                indent_Increasing = True

except KeyboardInterrupt:
    sys.exit()

