#Merging the Tools problem related to python strings.
#Print each subsequence on a new line. There will be n/k of them. No return value is expected.

def merge_the_tools(string, k): #Defining the function.
    c = 0
    st = ' '
    for i in string:            #Checking the Condition.
        if i not in st:   
            st = st + i
        c +=1
        if c == k:
            print(st)
            c=0
            st = ' '

if __name__ == '__main__':      # Main Function
    string, k = input(), int(input())
    merge_the_tools(string, k)