'''
 * linestripper.py
 * description: strips extra lines in files if file exists
'''

filename = raw_input('Enter a file name to strip: ')
try:
    with open(filename, 'rb') as f:
        lines = f.readlines()
        f.close()
    print("Stripping...")
    with open(filename, 'wb') as f:
        for i in lines: 
            if len(i.strip()) > 0:
                f.write(i)
    f.close()
    print("File stripped of extra lines.")
    print("have a good day!")
except (OSError, IOError) as e: print("File does not exist.")
