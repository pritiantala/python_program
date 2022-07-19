def quiz():
    guess=[]
    correct_ans=0
    que_num=1

    for key in question:
        print("---------------------------")
        print(key)
        for i in options[que_num-1]:
            print(i)
        ans=input("Enter(A,B,C, or D):")
        ans=ans.upper()
        guess.append(ans)

        correct_ans+=check_answer(question.get(key),ans)
        que_num+=1
    display_score(correct_ans,guess)
    
#-------------------------------------
def check_answer(answer,ans):
    if answer==ans:
        print("CORRECT ANS!")
        return +50
    else:
        print("WRONG ANS!")
        return -20
#------------------------------------------
def display_score(correct_ans,guess):
    print("--------------------------")
    print("RESULTS")
    print("----------------------------")

    print("Answers:",end=" ")
    for i in question:
        print(question.get(i),end=" ")
    print()
    print("YOUR ANS IS:",end=" ")
    for i in guess:
        print(i,end=" ")
    print()  
    
    print("Your score is:"+str(correct_ans))
   
    


#-------------------------------------------
def play_again():
    choice=input("Do you want to continue?press 'y' for yes ans 'n' for no: SS")
    if choice=='n' or choice=='no':
        return False
    else:
        return True
#------------------------------------------
question={
    "What is never borrowed, but often returned?:":"D",
    "Joe’s father had three sons. Two were named Snap and Crackle. What was the third son's name?:":"B",
    "What is something that you are forever leaving behind, but still always have?:":"B",
    "What is at the end of every rainbow?:":"C",
    "Which month has 28 days?:":"D",
    "The more you take, the more you leave behind. What are they?:":"D",
    "I start off dry but emerge wet. I go in light but emerge heavy. What am I?:":"A",
    "I have a head, but I don’t have a body. I have leaves, but no branches. What am I?:":"C",
    "I will crack if you drop me. If you smile at me, I’ll smile back. What am I?:":"B",
    "I start with M and end with X and have an infinite number of letters. What am I?:":"C",

}
options=[["A.Gifts","B.A Dog","C.A Check","D.Thans"],
         ["A.Snap","B.Joe","C.Rap","D.You"],
         ["A.Smell","B.Fingerprints","C.Memory","D.Wits"],
         ["A.A pot of gold","B.Blue","C.A letter W","D.A strom"],
         ["A.January","B.February","C.June","D.All of them"],
         ["A.Memory","B.Money","C.Candle","D.Footsteps"],
         ["A.Tea bag","B.Rice","C.Water","D.Swimmer"],
         ["A.Bonsai","B.Book","C.Lettuce","D.Oak tree"],
         ["A.An egg","B.Mirror","C.Nuts","D.A vase"],
         ["A.Mix","B.Minx","C.Mailbox","D.Marx"]
]

while play_again():
    quiz()
print("THANKS")