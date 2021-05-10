import random as rd
x=rd.randint(1,3)
print('1=Rock, 2=Paper, 3=Scissor')
print('Opponent have played the move')

for i in range(2):
    print('now time to play your move.......type 1,2 or 3')
    rps=int(input())
    if rps<1 or rps>3:
        print('Invalid output')
    elif x==rps:
        print('Draw')
    elif x==1 and rps==2:
        print('u win')
        break
    elif x==2 and rps==3:
        print('u win')
        break
    elif x==3 and rps==1:
        print('u win')
        break
    else:
        print('u lose, try again once more')
