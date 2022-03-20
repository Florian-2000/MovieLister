# Description

This little tool reads a given Google Sheet table with a specific format for a movie list and gives you a randomized list with the wished amount of entries.
The format will need 
1. the title of the movie
2. the genre of the movie
3. the length of the movie (in minutes) and
4. a checkbox (e.g. if the movie was already watched)

There are some possibilities to edit the list before the final output:
- Add a specific entry from the Google Sheet table.
- Delete an already added entry from the final ouput
- Enter a maximum movie length
- Enter a minimum movie length

When you see the final output it can be copied to your clipboard automatically.

# Preconditions
## Google Service Mail
- You need to create a project with any project name on the [Google Cloud Platform](https://console.developers.google.com).
- Go to the dashboard of the new project and enable Google Sheet API.
- Now create a service account with "Viewer" permission.
- Create a key for this service account. 
- Fill the key.json in the folder "resources" in this project with the content of your created key.
- Share your Google Sheet which you want to use later with this mail-address.

## Google Sheet Specifications

- You need four connected columns
- In Read.py
  - In line 14: Enter the Google Sheet ID between the quotation marks. You find the ID in the URL: https://docs.google.com/spreadsheets/d/[ID]/edit
  - in line 17: Enter the range the program shall read in this format without the brackets between the quotation marks: 
  [table_name]![first_column][first_line]:[last_column][last_line]
    - The first line equals the first entry (movie)
    - You do not need to enter [last_line]. This way, the program will read all entries and does not need to be updated
  - In line 20: Enter the title column (if it is the first column that shall be read, enter 0 and so on)
  - In line 21: Enter the genre column (if it is the first column that shall be read, enter 0 and so on)
  - In line 22: Enter the length column (if it is the first column that shall be read, enter 0 and so on)
  - In line 23: Enter the checkbox column (if it is the first column that shall be read, enter 0 and so on)

# How to use
You can either use python manually via the command line, use an IDE or create a *.exe file.
Make sure there is always a correct version of key.json, otherwise it will not work.
