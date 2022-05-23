#User function Template for python3

def reverseWord(s):
    ln = len(s) - 1
    arr = list(s)
    
    i = 0
    while i <= ln - i:
        arr[i], arr[ln - i] = arr[ln - i], arr[i]
        i += 1
    
    string = ''
    return (string.join(arr))
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends