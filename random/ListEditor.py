import inflect
import random
from operator import itemgetter

import Read
from Specification import specification_handler


# Creating a new list with all unchecked entries
def get_unchecked(old_movie_list):
    # the new list
    new_movie_list = []

    # sort out unchecked entries
    try:
        for movie in old_movie_list:
            if movie[Read.CHECKBOX_CELL] == 'FALSE':
                new_movie_list.append(movie)
    except IndexError:
        print('There is no unchecked entry!')
        quit()

    for movie in new_movie_list:
        movie.remove('FALSE')

    return new_movie_list


# asking for the amount of entries the user wants to get
def asking_entry_amount(entries_amount):

    # actual question for user input
    while True:
        try:
            # amount as a string
            amount_string = input('\nSo how many movies do you want in your list? (Write a number like \"4\")\n')
            # amount as an int
            amount_int = int(amount_string)

            # test if positive
            if amount_int < 0:
                print('Seriously why would you want this?')
            # test if user input is higher then actual entries in sheet
            elif amount_int > entries_amount:
                print('You do not have this much entries in your sheet')
            else:
                break

        # if input was a negative number or words
        except ValueError:
            print('Wait. That\'s illegal. Try a real whole positive number.')

    # Output
    if amount_int == 1:
        print('You wished for only one movie!')
    elif amount_int == 0:
        print('Okay bye')
        quit()
    else:
        print('You wished for ' + inflect.engine().number_to_words(amount_int) + ' movies in your list.')

    return amount_int


# create a random list with the wished amount of entries
def randomize_list(movie_list):
    # all unchecked movies
    movie_list = get_unchecked(movie_list)

    # get the wished amount
    amount = asking_entry_amount(len(movie_list))

    # specific wishes                                       # add help list for specific entries
    end_list = []
    movie_list, end_list = specification_handler(movie_list, end_list, amount)

    # creation of random list
    list_to_user = end_list

    for x in range(amount - len(end_list)):
        # get element of list
        rand = random.choice(movie_list)
        # get index of element in list
        index = movie_list.index(rand)

        # test if entry is already in final list and if yes the next entry ist taken
        while list_to_user.__contains__(movie_list[index]):
            index = (index + 1) % len(movie_list)
        list_to_user.append(movie_list[index])

    return list_to_user


# sort movies by genre
def sort_by_genre(movie_list):
    movie_list = sorted(movie_list, key=itemgetter(Read.GENRE_CELL))

    return movie_list


# nice output of list
def output_list(movie_list):
    list_as_string = ''
    for counter in range(0, len(movie_list)):
        list_as_string += (str(counter+1) + ". " + movie_list[counter][Read.TITLE_CELL] + "\n     " +
                           movie_list[counter][Read.GENRE_CELL] + "\n     " + movie_list[counter][Read.LENGTH_CELL] +
                           "min\n")

    return list_as_string
