s=[]
def push(ele):
    s.append(ele)

def pop():
    print("The poped element is ",s[-1])
    del s[-1]

def peek():
    print("The top element is ",s[-1])


def isEmpty():
    if len(s)==0:
        print("stack is empty")

def size():
    print("Current size of the stack is ",len(s))


c=True

while(c) :
    print("1.push \n2.pop \n3.peek \n4.isEmpty \n5.size \n6.exit")
    a=int(input("Enter the choice from given option: "))
    if a==1:
        d=int(input("Enter an element to push in the stack: "))
        push(d)
    elif a==2:
        pop()
    elif a==3:
        peek()
    elif a==4:
        isEmpty()
    elif a==5:
        size()
    elif a==6:                 
        c=False