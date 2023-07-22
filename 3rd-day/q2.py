#Find the Runner-Up Score!
##Given the participants' score sheet for your University Sports Day,
##you are required to find the runner-up score. You are given  scores.
##Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input("Now many Number you want to enter:"))
    arr = list(map(int, input("Enter Number:").split()))
    arr.sort()
    print(arr[arr.index(max(arr))-1])
    
