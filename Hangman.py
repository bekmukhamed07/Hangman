import random

def get_word():
    words = open("list_of_films.txt", "r")
    word = random.choice(words.readlines()).upper()
    word = word.strip()
    return word

def main():
    word = get_word()
    chooses = []
    guessed = False
    print('Can you guess the film?\n')
    print('The word contains', len(word), 'letters')
    while not guessed:
        text = 'Please enter one letter or a {}-letter word. '.format(len(word))
        choose = input(text)
        choose = choose.upper()
        if choose in chooses:
            print('You already printed "' + choose + '"')
        elif len(choose) == len(word):
            chooses.append(choose)
            if choose == word:
                guessed = True
            else:
                print('Sorry that is incorrect.')
        elif len(choose) == 1:
            chooses.append(choose)
            result = check(word, chooses, choose)
            if result == word:
                guessed = True

            else:
                print(result)

        else:
            print('Invalid entry.')

    print('Yes, the word is', word + '! You got it in', len(chooses), 'tries.')


def check(word, chooses, choose):
    choose = choose.upper()
    status = ''
    matches = 0
    for letter in word:
        if letter in chooses:
            status += letter
        else:
            status += '*'

        if letter == chooses:
            matches += 1

    if matches > 1:
        print('Yes, the word contains', matches, '"' + choose + '"' + 's')
    elif matches == 1:
        print('Yes, the word contains the letter "' + choose + '"')
    else:
        print('Sorry, the word does not contain the letter "' + choose + '"')

    return status

main()
