'''
 * linestripper.py
 * description: strips extra lines in files if file exists
'''

filename = raw_input('Enter a file name to strip: ')
try:
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    f = open(filename, "w")
    print("Stripping...")
    for line in lines:
        if line != '\n':
            f.write(line)
    f.close()
    print("File stripped of extra lines.")
    print("have a good day!")
except (OSError, IOError) as e: print("File does not exist.")
