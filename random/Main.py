from Read import get_list_from_sheet
from ListEditor import output_list, randomize_list, sort_by_genre
import clipboard

if __name__ == '__main__':
    print('Welcome to the randomizer application for your google sheets!\n'
          + 'Here you can get a random selection of your movie entries from Google Sheets.')

    while True:

        # all sheet entries
        movie_list = get_list_from_sheet()

        # final list
        movie_list = sort_by_genre(randomize_list(movie_list))

        # actual list to user
        movie_list = output_list(movie_list)
        print(movie_list)

        is_fine = input('\nIs this fine for you? If yes, the list will be ' +
                        'copied to your clipboard (\"1\" = Yes, Everything else = No)\n')
        if is_fine == '1':
            clipboard.copy(movie_list)
            break
