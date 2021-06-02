# importing the module
import subprocess
from datetime import datetime
import json
import array
import binascii
import os 
import sh  # pip install sh #WORKS FOR MACOS

def first():
    with open(".\\sample.txt") as f:     
        content_list = f.readlines()
        print(content_list)

def second():
    date_format = "%d/%m/%Y"
    date1 = input("Enter the first Date in format (DD/MM/YYYY): ")
    date2 = input("Enter the second Date in format (DD/MM/YYYY): ")
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    delta = b - a
    print (delta.days,"without including the end date.")

def third():
    dict1 = {}
    n = int(input("Enter total number of items in dictionary: "))
    for i in range(n):
        print(f"\nENter the value for {i+1} item : ")
        name = input("Enter the key value: ")
        values = int(input(f"Enter the value for key {name}: ")) 
        dict1[name] = values
    print(dict1)
    print("Original String:")
    print(dict1)
    print("\nJSON data:")
    print(json.dumps(dict1, sort_keys=True, indent=4))

def forth():
    models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
    print("Original list of dictionaries :")
    print(models)
    sorted_models = sorted(models, key = lambda x: x['color'])
    print("\nSorting the List of dictionaries :")
    print(sorted_models)

def fifth():
       with open(".\\sample.txt") as f:
        data = f.read()
        data.replace(",", " ")
        print(len(data.split(" ")))

def sixth():
    x = input("Enter the elements of array: ")
    b = x.split(" ")
    c = []
    for i in b:
        c.append(int(i))
    print(c)
    a = array.array('i',c)
    print("Original array: ")
    print('A1: ', a)
    bytes_array = a.tobytes()
    print('Array of bytes: ', binascii.hexlify(bytes_array))

def eighth():
    while 1:
            x = 1    
            file = open(f'.\\logs\\{x}.log', 'a') 
            file_size = os.stat(f'.\\logs\\{x}.log').st_size 
            while file_size<2097152:
                q = input("Enter the data for log file: ")
                file.write(f"{datetime.now()} : {q}\n")
                print("Writing in the same file") 
            print("Creating new file")

def ninth():
    print("All the active IP address of your machine are: ")
    print ("----------------------")   
    
    for num in range(10,40):  
        ip = "192.168.0."+str(num)  
    
        try:  
            sh.ping(ip, "-c 1",_out="/dev/null")  
            print ("PING ",ip , "OK" ) 
        except sh.ErrorReturnCode_1:  
            print ("PING ", ip, "FAILED")


    print("ALL THE INSTALLED SOFTWARE ON THE MACHINE ARE: ")
    Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
    a = str(Data)
    # try block
    try:
        for i in range(len(a)):
            print(a.split("\\r\\r\\n")[6:][i])
    except IndexError as e:
        print("All Done")


# Driver program
if __name__ == "__main__":
    while 1:
        print("Enter X to exit ")        
        a = input("CHOOSE QUESTION NUMBER TO RUN THE SCRIPT: ")
        if(a=='1'):
            first()
        elif(a=='2'):
            second()
        elif(a=='3'):
            third()
        elif(a=='4'):
            forth()
        elif(a=='5'):
            fifth()
        elif(a=='6'):
            sixth()
        elif(a=='7'):
            pass
        elif(a=='8'):
            eighth()
        elif(a=='9'):
            ninth()
        elif(a=='X'):
            exit()
        else:
            print("Wrong Option")
