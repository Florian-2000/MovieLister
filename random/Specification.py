import inflect

# from here it's possible to see all specific questions
import Read


def specification_handler(movie_list, end_list, amount):
    print('Now you can add specific wishes. What do you want to do?')
    while True:
        wish = input(
            '\"1\" = add specific entry to final list\n'
            '\"2\" = delete specific entry from final list\n'
            '\"3\" = enter maximum length\n'
            '\"4\" = enter minimum length\n'
            '\"5\" = enter wished genres\n'
            '\"6\" = update wished amount\n'
            'Everything else = Nothing\n')
        if '1' == wish:
            movie_list, end_list = add_specific_entry(movie_list, end_list, amount)
        elif '2' == wish:
            end_list = delete_specific_entry(end_list)
        elif '3' == wish:
            movie_list = create_list_with_maximum_length(movie_list, end_list, amount)
        elif '4' == wish:
            movie_list = create_list_with_minimum_length(movie_list, end_list, amount)
        elif '5' == wish:
            movie_list = get_wished_genre(movie_list, amount)
        elif '6' == wish:
            amount = update_amount(amount, movie_list, end_list)
        else:
            break

    return movie_list, end_list


# 1. add an entry the user wants to see in the final list
def add_specific_entry(movie_list, end_list, amount):
    is_full = test_difference(len(end_list), amount)  # maybe error here with dimension

    # Do nothing if list is full
    if not is_full:
        return movie_list, end_list
    wished_entry = input('What do you want to add from your google sheet? Just give me the title.\n')

    # test if movie is already in final list
    for counter in range(0, len(end_list)):
        if end_list[counter][Read.TITLE_CELL] == wished_entry.lower():
            print('This movie is already in your list.\n')
            return movie_list, end_list
        counter += 1

    # go through entire list with unchecked elements and look if wished_entry is an element
    for counter in range(0, len(movie_list)):
        if movie_list[counter][Read.TITLE_CELL] == wished_entry.lower() and movie_list[counter] not in end_list:
            end_list.append(movie_list[counter])
            print('Movie was added to your list.\n')
            return movie_list, end_list

    print('Sorry, but this movie is not in your unchecked watchlist.\n')

    return movie_list, end_list


# 2. delete entry from final list
def delete_specific_entry(end_list):
    # if there is no added entry
    if len(end_list) == 0:
        print('There is nothing to delete.\n')
        return end_list

    # user need to know which elements are in current list
    print('Your current final list:')
    print(output_list(end_list))

    wished_entry = input('What do you want to delete from your final list? Just give me the title.\n')

    # actual deletion of element

    in_list = False
    for counter in range(0, len(end_list)):
        if end_list[counter][Read.TITLE_CELL] == wished_entry:
            end_list.remove(end_list[counter])
            print('Movie was deleted from your list.\n')
            in_list = True

    if not in_list:
        print('Sorry, but this is not in your current final list.\n')

    return end_list


# 3. create list with maximum length
def create_list_with_maximum_length(movie_list, end_list, amount):
    max_length = input('What is the maximum length in minutes?\n(Hint: If you still want to add a movie which is longer'
                       ' than your wished maximal length then you maybe won\'t be able to do this after this.\nPerhaps '
                       'just type something very high and come back later.)\n')

    max_length = bring_back_correct_number(max_length)
    if max_length == -1:
        print('Try again. Your input was not a real whole positive number.\n')
        return movie_list

    max_length_list = []

    # go through movie list and copy elements below maximum length
    counter = 0

    for movie in movie_list:
        if int(movie[Read.LENGTH_CELL]) <= max_length:
            max_length_list.append(movie)
            counter += 1

    # test if enough movies can be selected to fill the wished amount of movies
    if counter < amount - len(end_list):
        print('This is too low. It is not possible to get the wished amount of movies.\n')
        return movie_list

    print('Updated maximum length')
    return max_length_list


# 4. create list with minimum length
def create_list_with_minimum_length(movie_list, end_list, amount):
    min_length = input('What is the minimum length in minutes?\n(Hint: If you still want to add a movie which is '
                       'shorter than your wished minimal length then you maybe won\'t be able to do this after this. '
                       '\nPerhaps just type something very low (greater than 1) and come back later.)\n')

    min_length = bring_back_correct_number(min_length)
    if min_length == -1:
        print('Try again. Your input was not a real whole positive number.\n')
        return movie_list

    min_length_list = []

    # go through movie list and copy elements below maximum length
    counter = 0
    for movie in movie_list:
        if int(movie[Read.LENGTH_CELL]) >= min_length:
            min_length_list.append(movie)
            counter += 1

    # test if enough movies can be selected to fill the wished amount of movies
    if counter < amount - len(end_list):
        print('This is too high. It is not possible to get the wished amount of movies.\n')
        return movie_list

    print('Updated minimum length')
    return min_length_list


# 5. create a list with only wanted genres
def get_wished_genre(movie_list, amount):
    # list with all wished genre
    genre_list = []

    while True:
        wished_genre = input('Which genre do you want to see in your final list?\n')
        genre_exists = False
        for movie in movie_list:
            if wished_genre in movie[Read.GENRE_CELL]:
                genre_list.append(movie)
                genre_exists = True
        if not genre_exists:
            print('This genre does not exist in the list.')

        is_enough = input('Add another genre? \"1\" = Yes, Everything else = No\n')
        if is_enough != '1':
            break

    if len(genre_list) < amount:
        print('Sorry, but there are not enough movies compared to your wished amount of entries.\n')
        return movie_list

    print('The list was updated.\n')
    return genre_list


# 6. update amount of entries for list
def update_amount(amount, movie_list, end_list):

    print('Currently you want ' + str(amount) + ' movies in your final list.')
    print('The maximum amount you can enter is ' + str(len(movie_list)))

    if len(end_list) == 0:
        print('The minimum amount you can enter is ' + str(1))
    else:
        print('The minimum amount you can enter is ' + str(len(end_list)))

    new_amount = input('')
    new_amount = bring_back_correct_number(new_amount)
    # if new amount is not a useful number
    if new_amount == -1:
        print('Try again. Your input was not a real whole positive number.\n')
        return amount

    # if new amount is too high to get wished amount of entries
    if len(movie_list) < new_amount:
        print('This amount is too high.\n')
        return amount

    # if new amount is too low because of already entered movies
    if len(end_list) > new_amount:
        print('This amount is too low.\n')
        return amount

    print('Your new amount is ' + str(new_amount) + '\n')
    return new_amount


# testing to make sure final list is not longer than wished
def test_difference(param, amount):
    if amount - param == 0:
        movie_string = 'movie'
        if amount > 1:
            movie_string += 's'
        print(
            'Sorry, but you already have ' + inflect.engine().number_to_words(amount)
            + ' ' + movie_string + ' in your list. You should consider deleting an entry')
        return False
    elif amount - param == 1:
        print('Only one more movie allowed!')
        return True
    else:
        return True


# nice output of list
def output_list(movie_list):
    list_as_string = ''
    for counter in range(0, len(movie_list)):
        list_as_string += (
                str(counter + 1) + ". " + movie_list[counter][0] + "\n     " + movie_list[counter][1] + "\n     " +
                movie_list[counter][2] + "min\n")

    return list_as_string


def bring_back_correct_number(input_string):
    try:
        # amount as an int
        amount_int = int(input_string)
        if amount_int > 0:
            return amount_int

        return -1

    # if input was a negative number or words
    except ValueError:
        return -1
