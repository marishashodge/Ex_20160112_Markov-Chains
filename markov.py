from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    content = open(file_path)
    content = content.read()

    return content

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    individual_words = text_string.split()

    for i in range(len(individual_words) - 2):
        if (individual_words[i], individual_words[i+1]) not in chains:
            chains[(individual_words[i]), individual_words[i+1]] = [individual_words[i+2]]

        elif (individual_words[i], individual_words[i+1]) in chains:
            chains[(individual_words[i], individual_words[i+1])].append(individual_words[i+2])

    return chains



def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""


    key0 = choice(chains.keys())
    text = key0[0] + " " + key0[1] + " " + choice(chains[key0]) 

    while text[-9:] != "Sam I am?":
        indiv_text = text.split()
        key = (indiv_text[-2], indiv_text[-1])
        text = text + " " + choice(chains[key]) 

    print text
    return text

text_string = open_and_read_file("green-eggs.txt")
chains = make_chains(text_string)
make_text(chains)

# text_string = open_and_read_file("green-eggs.txt")
# chains = make_chains(text_string)
# input_text = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_text)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
