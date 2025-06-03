questions =[
    ["which datatype is use for storing alphabets !","int","char","float","array",2],
    ["which datastructure is like tree !","queue","linkedlist","tree","stack",3],
    ["which !","int","char","float","array",2],
    ["which datatype is use for storing alphabets !","int","char","float","array",2],
    ["which datatype is use for storing alphabets !","int","char","float","array",2]
]
level=[1000,10000,160000,320000,2500000]
money=0

i=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"The Question for {level[i]} rs apki screen pr ye raha !!!:")
    print(f"{question[0]}")
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")
    ans=int(input("enter option from 1-4 :"))
    if ans==question[-1]:
        print("congratulations you are right !")
        money=level[i]
        print(f"your currnt amount is {money}")
    else:
        print("wronge answer !") 
        if i==0:
            money=0
            print(f"now your winning amount is {money} due to loss")
            break
        elif i<=2 and i>=1:
            money=10000
            print(f"now your winning amount is {money} due to loss")
            break
        elif i>=3:
            money=320000  
            print(f"now your winning amount is {money} due to loss")      
            break
        

































