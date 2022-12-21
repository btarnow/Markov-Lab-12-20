"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # open file and read to one long string with .read()
    contents = open(file_path).read()

    # return string
    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # split the contents of the file by whitespace
    words = text_string.split()

    # loop through contents (range()+1))
    for i in range(len(words)-2):

        # add tuples as keys in dictionary, using get
        word_pair = (words[i], words[i+1])
        chains[word_pair] = chains.get(word_pair, [])

        # add following word in list at key
        chains[word_pair] += [words[i+2]]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # create link using choice 
    link = choice(list(chains.keys()))
    
    # to check that we're starting with an upper case word
    while link[0][0] != link[0][0].upper() or link[0][0].isalpha() == False:
        link = choice(list(chains.keys()))

    # link[0][0].isalpha()

    # add link to list of words
    words.append(link[0])
    words.append(link[1])

    # start a while True loop
    while True:
        try: 
            # select a random value from list in dict at key link
            next_word = choice(chains[link])

            # append to words
            words.append(next_word)

            # update link for next iteration
            link = tuple((link[1], next_word))

        # Except KeyError --> break 
        except KeyError: 
            break

    return ' '.join(words)

input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
