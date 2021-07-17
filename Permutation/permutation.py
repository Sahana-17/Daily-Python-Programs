#Python code to output all the permutaitons for a given string
#Eg. ABC : ABC, ACB, BCA, BAC, CAB, CBA

def generatePermutation(string,start,end):  
    current = 0
    if(start == end-1):  
        print(string) 
    else:   
        for current in range(start,end):  
   
            x = list(string)  
            temp = x[start]  
            x[start] = x[current] 
            x[current] = temp
  
     
  
            generatePermutation("".join(x),start+1,end)  
             
            temp = x[start] 
            x[start] = x[current]
            x[current] = temp
  
str = "aeiou"  
n = len(str)
print("All the permutations of the string are: ") 
generatePermutation(str,0,n)
