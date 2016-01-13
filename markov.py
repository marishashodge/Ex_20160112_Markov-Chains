from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    content = open(file_path)
    content = content.read()

    return content

def make_chains(text_string,nth_gram):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    indiv_words = text_string.split()

    for i in range(len(indiv_words) - nth_gram):
        nth_tuple = (indiv_words[i],)

        if nth_gram > 1:
            for n in range(nth_gram)[1:]:
                nth_tuple = nth_tuple + (indiv_words[i+n],)

        if nth_tuple not in chains:
            chains[nth_tuple] = [indiv_words[i+nth_gram]]

        elif nth_tuple in chains:
            chains[nth_tuple].append(indiv_words[i+nth_gram])

    # print chains
    return chains


def make_text(chains, text_string, nth_gram):
    """Takes dictionary of markov chains; returns random text."""

    key = choice(chains.keys())
    text = key[0]
    if nth_gram > 1:
        for n in range(nth_gram)[1:]:
            text = text + " " + key[n]

    text += " " + choice(chains[key]) 

    indiv_words = text_string.split()
    stop_adding = indiv_words[-3] + " " + indiv_words[-2] + " " + indiv_words[-1]
    stop_count = len(stop_adding)

    while text[-stop_count:] != stop_adding:
        indiv_text = text.split()
        next_key = (indiv_text[-nth_gram],)
        if nth_gram > 1: 
            for n in range(nth_gram)[1:]:
                next_key = next_key + (indiv_text[(-nth_gram)+n],)
        text = text + " " + choice(chains[next_key]) 

    print text
    return text

import sys 

filename = sys.argv[1]
text_string = open_and_read_file(filename)
chains = make_chains(text_string, 3)
make_text(chains, text_string, 3)

# Below code provided by Hackbright
# input_text = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_text)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
