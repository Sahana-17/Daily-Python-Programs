#Compare names in two files without using "comm" or any in-built function

file1 = open("/users/sahana/Daily-Python-Programs/namelist.txt", "r")
file2 = open("/users/sahana/Daily-Python-Programs/infernal_name.txt", "r")


for line1 in file1:

    for line2 in file2:

        if line1 == line2 :
            print(line1)
        else:
            print("")
        break

file1.close()
file2.close()
