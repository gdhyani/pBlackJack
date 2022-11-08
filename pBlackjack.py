import ascii_code
import random
print(ascii_code.art)
start = input("Do you want to play BlackJack? ")


def gameStart():
    print('Welcome to BlackJack!\nRules:\n1.Who ever is close to 21 WINS.\n2.You will be giving 2 cards and computer will get 1 card.\n3.You will given the choice.')
    U_cards = []
    U_total = 0
    C_cards = []
    C_total = 0
    U_cards.append(random.randint(1, 13))
    U_cards.append(random.randint(1, 13))
    C_cards.append(random.randint(1, 13))

    for card in U_cards:
        U_total += card
    print(f'\n\nYour cards are = {U_cards}    And your total = {U_total}')

    for card in C_cards:
        C_total += card
    print(f"Computer cards are = {C_cards}   And Computer total = {C_total}")

    if(input("Want to draw a card 'd' or pass the card 'p'") == 'p' ):
        C_cards.append(random.randint(1, 13));
        C_cards.append(random.randint(1, 13));
        C_total = C_total +C_cards[-1]+C_cards[-2];
        print(f'\n\nYour cards are = {U_cards}    And your total = {U_total}')
        print(f"Computer cards are = {C_cards}   And Computer total = {C_total}");
        print(f'{21-U_total} {21-C_total}');
        if(abs(21-C_total)>abs(21-U_total)):
            print("You won");
        elif (abs(21-C_total)<abs(21-U_total)):
            print('You Lose')
        else:
            print("Draw");
    else:
        exit();





def exit():
    print("Thankyou for playing BlackJack with us.")


if(start == "y"):
    gameStart()
else:
    exit()
