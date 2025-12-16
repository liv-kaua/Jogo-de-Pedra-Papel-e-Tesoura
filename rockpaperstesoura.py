import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if player_choose == 0:
    print(rock)
elif player_choose == 1:
    print(paper)
elif player_choose == 2:
    print(scissors)
else:
    print("You typed an invalid number, you lose!")

print("Computer chose:")

computer_choose = random.randint(0,2)
if computer_choose == 0:
    print(rock)
elif computer_choose == 1:
    print(paper)
else:
    print(scissors)


if player_choose == 0 and computer_choose == 2:
    print("You win")
elif player_choose == 1 and computer_choose == 0:
    print("You win")
elif player_choose == 2 and computer_choose == 1:
    print("You win")
elif player_choose == computer_choose:
    print("It's a draw!")
else:
    print("You lose!")


# pedra quebra a tesoura (pedra vence tesoura)
#
# papel envolve a pedra (papel vence pedra)
#
# tesoura corta o papel (tesoura vence papel)