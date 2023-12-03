from random import shuffle
list1 = [' ','0',' ']
def shufflelist(shuff_list) :
    shuffle(shuff_list)
    return shuff_list
def play_game():
    guess =''
    guess = input("Pick the correct index from 0 , 1 or 2")
    return int (guess)
def check(shuff_list,guess):
    if(shuff_list[guess] == '0'):
        print("You Won")
    else:
        print("try again!!!")
        print(shuff_list)

shuff_list=shufflelist(list1)
guess = play_game()
check(shuff_list,guess)