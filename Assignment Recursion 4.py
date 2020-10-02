#Q4.Implement recursion using a stack ADT.

# Python program to sort a stack using recursion
def sortedInsert(s,element): #function to insert element in the sorted way
    if len(s)==0 or element>s[-1]:
        s.append(element) 
        return
    else: 
        temp = s.pop() 
        sortedInsert(s, element) 
        s.append(temp) 
 
def sortStack(s): #function to sort stack
    if len(s) != 0: 
        temp = s.pop()
        sortStack(s)
        sortedInsert(s,temp) 
  
def StackAsc(s): #function for ascending order sorting
    for i in s: 
            print(i , end=" ") 
    print()

def StackDesc(s): #function for descending order sorting
    for i in s[::-1]:
        print(i,end=" ")
    print()


stack1=[]
print("Enter the size of an Stack")
size=int(input())

print("Enter the elements in the Stack")
for i in range(0,size):
    stack1.append(int(input()))

print("Stack elements before Soring")
StackAsc(stack1)

sortStack(stack1)

print("Stack elements after Sorting in Ascending order")
StackAsc(stack1)

print("Stack elements after Sorting in Descending order")
StackDesc(stack1)
