print("\n Players enter the choice :- \n1) rock\n (2) scissor\n (3) paper")


a="rock"
b="scissor"
c="paper"

p_1=input("player_1 enter the choice")
p_2=input("player_2 enter the choice")

if p_1==a and p_2==b:
    print("rock beat scissor")
    print("congrates. player_1")
    
elif p_1==a and p_2==c:
     print("paper beat rock")
     print("congrates. player_2")

elif p_1==a and p_2==a:
       print("match tie")
    

elif p_1==b and p_2==a:
     print("rock beat scissor")
     print("congrates. player_2")
    
elif p_1==b and p_2==c:
     print(" scissor beat paper")
     print("congrates. player_1")

elif p_1==b and p_2==b:
       print("match tie")
       
elif p_1==c and p_2==a:
     print("paper beat rock")
     print("congrates. player_1")

elif p_1==c and p_2==b:
     print(" scissor beat paper")
     print("congrates. player_2")

elif p_1==c and p_2==c:
    print("match tie")

else:
    print("not apropriate choice")
    
