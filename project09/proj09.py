##################################################################
#  CSE 231 Project 9
#  Asks the user for a stopwords and songdata file
#
#       Finds the singer, average word count of the singer, vocabulary size, and number of songs
#       Displays the above data in a table
#       Plots the data if the user wants to
#       Asks the user for words to search in the songs
#       Displays a table of singer and song
####################################################################

import csv
import string
import pylab

import operator


# Opens the file
def open_file(message):
    # The message is the instruction to open stopwords or songdata file
    message = input(message)
    # File opens and stores the file in itself
    file = open(message,'r')
    # File is returned
    return file


# Reads the stopwords file and returns a set of the words
def read_stopwords(fp):
    # Initializes a set for the words to be stored
    stopwords_set = set()

    # Reads the file, strips the whitespaces, and removes newlines
    file = fp.read().strip().split('\n')
    # Loops through the list and adds them to the stopwords_set
    for word in file:
        stopwords_set.add(word.lower())

    # Returns stopwords_set
    return stopwords_set


# Validates the word so it can decided whether to add it the dict
def validate_word(word, stopwords):
    # If the given word is in the stopword set or it has any digit or punctuation,
    # the function returns False. Otherwise, it returns True
    if (word.isalpha() == False) or (word in stopwords):
        return False
    else:
        return True


# Creates a set of words after it is processed
def process_lyrics(lyrics, stopwords):
    # Initializes a set()
    w_set = set()
    # Splits the lyrics
    lyrics = lyrics.split()
    # For every word in lyrics, it does the following
    for a in lyrics:
        # The word is made lowercase, strips it of whitespaces and punctuation
        a = a.lower().strip().strip(string.punctuation)
        # Validates the word with validate_word function
        validate = validate_word(a,stopwords)
        # If the validate_word returns True, it is added to word set
        if validate==True:
            w_set.add(a)

    # Returns w_set
    return w_set


# Returns a dictionary of the words in the file
def read_data(fp, stopwords):
    # Initializes an empty dictionary
    dict = {}
    # Reads the file
    reader = csv.reader(fp)
    # Skips the header
    next(reader)
    # For every row in the file, it does the following
    for row in reader:  # row is a list, i.e. you do not need split()
        # Singer is in the column 1
        singer = row[0]
        # Song is the name of the song in column 2
        song = row[1]
        # Lyrics is the column 3
        lyrics = row[2]

        # Words is set of words after they are validated and processed
        words = process_lyrics(lyrics , stopwords)
        # Creates a dictionary of the singer, song, and words
        dict = update_dictionary(dict,singer,song,words)

    # Returns dict
    return dict


# Update_dictionary returns a dict with the singer, song, and words
def update_dictionary(data_dict, singer, song, words):
        # Singer is the key and the value is a dict with {song:words} of data_dict
        if singer not in data_dict:
            data_dict[singer] = {song:words}
        # If singer already exists, words is added at [singer][song]
        else:
            data_dict[singer][song] = words
        # Returns data_dict
        return data_dict


# Calculates the average word count
def calculate_average_word_count(data_dict):
    # Initializes an empty dict
    dict={}
    # For singer (key) and value in data_dict, it does the following
    for singer,value in data_dict.items():
        # Keeps counts of songs from a singer
        song_count = 0
        # Keeps count of the word
        word_count = 0
        # For song(key) and words in the data_dict
        for song,words in value.items():
            # Song_count is incremented by one
            song_count+=1
            # For every word used a singer, word_count is incremented by one
            for word in words:
                word_count+=1
        # Singer and average words used is added to the dict
        dict[singer] = (word_count/song_count)
    # Dict is returned
    return dict


# Finds the unique words in the all the songs from a singer
def find_singers_vocab(data_dict):
    # Initializes an empty dict
    dict = {}
    # For singer (key) and value in data_dict, it does the following
    for singer, value in data_dict.items():
        # Initializes a set
        w_set = set()
        # For song(key) and words in the data_dict
        for song, words in value.items():
            # All words from a singer are added to the set to find the distinct ones
            for word in words:
                w_set.add(word)
        # The singer and the w_set is added to the dict
        dict[singer] = w_set
    # Dict is returned
    return dict


# Displays the singers in a table
def display_singers(combined_list):
    print("\n{:^80s}".format("Singers by Average Word Count (TOP - 10)"))
    print("{:<20s}{:>20s}{:>20s}{:>20s}".format("Singer","Average Word Count", "Vocabulary Size", "Number of Songs"))
    print('-' * 80)
    for lst in combined_list:
        print("{:<20s}{:>20.2f}{:>20.0f}{:>20.0f}".format(lst[0], lst[1], lst[2], lst[3]))


def vocab_average_plot(num_songs, vocab_counts):
    """
    Plot vocab. size vs number of songs graph
    num_songs: number of songs belong to singers (list)
    vocab_counts: vocabulary size of singers (list)

    """
    pylab.scatter(num_songs, vocab_counts)
    pylab.ylabel('Vocabulary Size')
    pylab.xlabel('Number of Songs')
    pylab.title('Vocabulary Size vs Number of Songs')
    pylab.show()


# Search songs for words that contain all user inputted words
def search_songs(data_dict, words):
    # Initializes a list so the singer and the song can be added
    lst = []
    # For singer (key) and value in data_dict, it does the following
    for singer, value in data_dict.items():
        # For song(key) and words in the data_dict
        for song, lyrics in value.items():
            # Check checks if all words in words exists in lyrics
            check = all(word in lyrics for word in words)
            # If true, singer and song are appended to the lst
            if check:
                lst.append((singer, song))

    # Lst with all the singers and song is returned
    return lst


def main():

    # Calls open_file and stores the returned stopwords file in stopwords_file
    stopwords_file = open_file('Enter a filename for the stopwords: ')
    # Calls open_file and stores the returned songdata file in songdata_file
    songdata_file = open_file('Enter a filename for the song data: ')
    # Calls read_stopwords function and stores returned set of stopwords in stopwords
    stopwords = read_stopwords(stopwords_file)

    # The dictionary from read_data is stored in data_dict
    data_dict = read_data(songdata_file,stopwords)
    # The average_word_count stores the return from calculate_word_count function
    avg_word_count = calculate_average_word_count(data_dict)
    # Vocab stores the dict that is returned from find_singers_vocab function
    vocab = find_singers_vocab(data_dict)
    # Average word count sorts the list in descending order by average word count
    avg_word_count = sorted(avg_word_count.items(), key=operator.itemgetter(1), reverse=True)
    # Initializes combined_list to be used to do display_singers
    combined_list=[]

    # For tup in average_word_count, the following is done
    for tup in avg_word_count:
        # Only appends the top 10
        if avg_word_count.index(tup) <=9:
            # Finds the [song: words] in data_dict
            songs_dict = data_dict[tup[0]]
            # Initializes song_count and word_count
            song_count = 0
            word_count = 0
            # For words in vocab, the word count is incremented by 1
            for g in vocab[tup[0]]:
                word_count+=1
            # Song count is incremented by 1 for every song of the artist
            for y,z in songs_dict.items():
                song_count+=1

            # Singer, average word count, vocab size, and song count is appended to the list
            combined_list.append([tup[0],tup[1],word_count,song_count])

    # Displays singer, avg word count, vocab size, and number of songs in a table
    display_singers(combined_list)

    # Plots the number of songs and vocab size, if the user says yes
    if input('Do you want to plot (yes/no)?: ').lower() == "yes":
        vocab_average_plot(song_count,word_count)
        pass

    # Asks the user for words to search for in the songs
    print("\nSearch Lyrics by Words")

    while True:
        # Asks for words to be searched in the songs
        search_words_input = input("\nInput a set of words (space separated), press enter to exit: ").split()
        # The search_words are inputted it runs
        if search_words_input:
            # Initializes a set for search words
            search_words_set = set()
            # For words in search words input, it is added to the search_words_set
            for search_word in search_words_input:
                search_words_set.add(search_word)
            # Search songs for the words in the songs
            search_song_lst = search_songs(data_dict,search_words_set)
            # Sorts the list by alphabetical order
            # search_song_lst.sort(key=operator.itemgetter(1))
            # Search song count initializes the song count for search
            search_song_count = 0
            # For every tup in seach song lst, the search song count is incremented by 1
            for search_tup in search_song_lst:
                search_song_count +=1

            # Prints the number of songs and header
            print("There are {} songs containing the given words!".format(search_song_count))
            print("{:<20s} {:<s}".format("Singer", "Song"))
            # For search_tup in search_song_lst displays singer and name of song
            for search_tup in search_song_lst:
                print("{:<20s} {:<s}".format(search_tup[0], search_tup[1]))
        # Else returns False and ends the loop
        else:
            return False


if __name__ == '__main__':
    main()