import os
import sys
import twitter
from random import choice
# from markov_twitter import tweet


def open_and_read_file(file_path1, file_path2):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    content1 = open(file_path1)
    content2 = open(file_path2)

    full_content = content1.read() + " " + content2.read()

    return full_content

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

    # Check for key with capitalized first word
    first_word = "test"
    while first_word != first_word.capitalize():
        key = choice(chains.keys())
        first_word = key[0]

    # Initializing output text with 1st key
    text = key[0]
    if nth_gram > 1:
        for n in range(nth_gram)[1:]:
            text = text + " " + key[n]

    # Add random word after first key
    text += " " + choice(chains[key]) 

    # Set arbitrary stop point with last three words of text file
    # indiv_words = text_string.split()
    # stop_adding = indiv_words[-3] + " " + indiv_words[-2] + " " + indiv_words[-1]
    # stop_count = len(stop_adding)

    # Add words to output text until stop point reached

    # if len(text) < 140:
    while text[-1] not in ["?", "!", "."]: # alternative option: text[-stop_count:] != stop_adding:
        indiv_text = text.split()
        next_key = (indiv_text[-nth_gram],)
        if nth_gram > 1: 
            for n in range(nth_gram)[1:]:
                next_key = next_key + (indiv_text[(-nth_gram)+n],)
        text = text + " " + choice(chains[next_key]) 

    # else: 
    return text


def tweet(chains):
    # Use Python os.environ to get at environmental variables
    # Note: you must run `source secrets.sh` before running this file
    # to make sure these environmental variables are set.
    
    api = twitter.Api(
        consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    # This will print info about credentials to make sure they're correct
    # print api.VerifyCredentials()

    # Send a tweet
    status = api.PostUpdate(chains)
    print status.text


filename1 = sys.argv[1]
filename2 = sys.argv[2]
text_string = open_and_read_file(filename1, filename2)
chains = make_chains(text_string, 2)
text = make_text(chains, text_string, 2)
# print text
tweet(text)

# Below code provided by Hackbright:
# input_text = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_text)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
