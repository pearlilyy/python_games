import random

# ---------- Task One ----------
# Guess the Number by User Input:
#     - Create a game where you have to guess a random number
#         within a certain range of integers.
#     - The game will always tell you whether your guess was too high or too low.
#     - Report to the User how many tries they have left and stop the game
#         when they have guessed the number or have no tries left.
#     - import the 'random' library to randomly pick a number
# '''


def guess_random_number(tries, start, stop):
    if str(tries).isalnum() != True or str(start).isalnum() != True or str(stop).isalnum() != True:
        print("You can only enter integers!")
        return False
    guess_list = []
    target = random.randint(start, stop)
    while tries != 0:
        print(f'Number of tries left: {tries}')

        guess = int(input(f"Guess a number between {start} and {stop}: "))
        if guess in guess_list:
            print("You can't enter the same number you used before.")
            continue
        else:
            guess_list.append(guess)

        if guess == target:
            print("You guessed the correct number!")
            break
        elif guess < target:
            print("Guess higher!")
            tries -= 1
        else:
            print("Guess lower!")
            tries -= 1
    if tries == 0:
        print(f"You have failed to guess number: {target}")
        return target

# guess_random_number(5, 0, 10)
# '''

# ---------- Task Two  ----------
# Guess the Number Computer Linear Search:
#     - Create a game where a program does the search for you.
#     - The search algorithm must run in O(n) - Linear Time
# '''


def guess_random_num_linear(tries, start, stop):
    target = random.randint(start, stop)
    print(f'The number for the program to guess is: {target}')

    for x in range(start, stop):
        print(f'Number of tries left: {tries}')
        print(f"The program is guessing... {x}")
        if x == target:
            print('The program has guessed the correct number!')
            return target
        else:
            tries -= 1
            if tries == 0:
                print("The program has failed to guess number.")
                return target

# guess_random_num_linear(5, 0, 10)
# '''

# ---------- Task Three ----------
# Guess the Number Computer Linear Search:
#     - Create a game where a program does the search for you.
#     - The search algorithm must run in O(log(n)) - Logarithmic Time
# '''


def guess_random_num_binary(tries, start, stop):
    # bonus task 1.
    if str(tries).isalnum() != True or str(start).isalnum() != True or str(stop).isalnum() != True:
        print("You can only enter integers!")
        return False

    target = random.randint(start, stop)
    print(f'Random number to find: {target}')
    while tries != 0 and start <= stop:
        pivot = (start + stop) // 2
        # print(pivot)
        if pivot == target:
            print(f'Found it! {pivot}')
            return pivot
        elif pivot < target:
            start = pivot + 1
            print('Guessing higher!')
            tries -= 1
            continue
        elif pivot > target:
            stop = pivot - 1
            print('Guessing lower!')
            tries -= 1
            continue
        else:
            continue
    print("The program has failed to guess number.")
    return target

# guess_random_num_binary(5, 0, 100)


# bonus task 2.
cus_tries = int(input("Enter how many tries you want to have: "))
cus_start = int(input("Enter the minimum range you want to set: "))
cus_stop = int(input("Enter the maximum range you want to set: "))

# bonus task 3.
print("Which one do you want to choose to guess a random number? ")
chosen_search = input(
    "1)user input,  2)linear search,  3)binary search  :").lower()
if chosen_search == "1" or chosen_search == "user input":
    guess_random_number(cus_tries, cus_start, cus_stop)
elif chosen_search == "2" or chosen_search == "linear search":
    guess_random_num_linear(cus_tries, cus_start, cus_stop)
elif chosen_search == "3" or chosen_search == "binary search":
    guess_random_num_binary(cus_tries, cus_start, cus_stop)
else:
    print("Enter 1, 2 or 3!")
# '''

''' Task 1.'''
# guess_random_num(5, 0, 10)

''' Task 2.'''
# guess_random_num_linear(5, 0, 10)

''' Task 3.'''
#guess_random_num_binary(5, 0, 100)
