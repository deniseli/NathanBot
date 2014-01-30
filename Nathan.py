# This is a python script to simulate a conversation with Nathan Handler.  It
# does not pass the Turing test, but then, neither does the real Nathan, so that
# limitation exists purely for the sake of realism, and definitely has nothing
# to do with my ability to make a bot that can pass the Turing test.
#
# Denise Li
# January 2014
#
# Nathan.py

import nltk
import random
import sys
import time
import urllib2
from lists import *


def split_text(text):
    global happiness
    words = nltk.word_tokenize(text)
    if any(s in text for s in key_words_and_phrases["exit"]):
        happiness = 0
        nathan_says("Oh, come on!")
        sys.exit()
    if any(s in words for s in key_words_and_phrases["greetings"]):
        respond_to_greeting()
    if any(s in words for s in key_words_and_phrases["debian"]):
        talk_about_debian()
        return True
    if any(s in words for s in key_words_and_phrases["open source"]):
        talk_about_open_source()
        return True
    if any(s in words for s in key_words_and_phrases["paul"]):
        talk_about_paul()
        return True
    return False

def nathan_says(text):
    sys.stdout.write("NathanBot: ")
    sys.stdout.flush()
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        if l is ' ': time.sleep(0.15)
        else: time.sleep(random.uniform(0.05, 0.1))
    print
    # Multiple hehehes possible, but unless Nathan is too happy,
    # chained hehehes should stop quickly.
    if random.randint(1, happiness + 30) < happiness: hehehe()

def handle_happiness(text):
    global happiness
    if "nathan" in text:
      happiness += 2
    elif any(s in text for list in key_words_and_phrases.values() for s in list for s in list):
      happiness += 1
    else:
      happiness -= 1
    if happiness <= 0: go_to_meeting()

def respond_to_greeting():
    sayings = ["Hi.", "Hello.", "Hi!"]
    nathan_says(random.choice(sayings))

def talk_about_open_source():
    nathan_is_a_pretty_big_deal("open source")

def talk_about_debian():
    nathan_is_a_pretty_big_deal("debian")

def nathan_is_a_pretty_big_deal(community):
    sayings = ["I'm a pretty big deal in the " + community + " community.",
               "Have you heard about my involvement with " + community + "?"]
    nathan_says(random.choice(sayings))

def talk_about_paul():
    sayings = ["Did you meet Paul Tagliamonte at R|P? He's @paultag on GitHub."]
    nathan_says(random.choice(sayings))

def talk_about_country_music():
    # Could do something interesting with this with a web app.  Perhaps autoplay
    # a song at the top of the country music charts?
    song_and_artist = random.choice(country_tunes)
    nathan_says("Let's listen to country music!")
    nathan_says("What do you say to listening to a bit of \"" + song_and_artist[0] + "\"?")
    nathan_says(song_and_artist[1] + " is great.")

def talk_about_my_spirit_animal():
    if random.randint(0, 1) is 0:
        animal_phrase = "The " + random.choice(critical_animals) + \
                        " is my spirit animal. It's going to die out soon..."
    else:
        animal_phrase = "The " + random.choice(extinct_animals) + \
                        " is my spirit animal. It's extinct."
    nathan_says(animal_phrase)

def go_to_meeting():
    # Over the summer of 2013 while interning at Facebook, our beloved Nathan
    # went to every single meeting in the hope of getting another free t-shirt.
    # This is an artist's rendition of that phenomenon.
    sayings = ["Sorry, I have to go to a meeting.  ttyl"]
    nathan_says(random.choice(sayings))
    sys.exit()

def hehehe():
    nathan_says("he" * ((happiness/3) + 1) + "h")

def default_nathan():
    random.choice([
        talk_about_open_source,
        talk_about_debian,
        talk_about_paul,
        talk_about_country_music,
        talk_about_my_spirit_animal,
        go_to_meeting
    ])()

happiness = 10
input = ""
nathan_says("Oh, hi!")
# "Oh, hi!" is temporary.  I actually want the user to input a background music
# choice upon starting NathanBot, but as soon as it loads, NathanBot replaces
# said choice with country music.
while True:
    input = raw_input("> ").lower()
    handle_happiness(input)
    if not split_text(input): default_nathan()
