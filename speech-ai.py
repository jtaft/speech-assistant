# MongoDb- 
#  Datebase: Julie
#  Collection: me
#  Document: {name: "Julie"}
#
import argparse
import tempfile

import sys
#import keyboard

import memory
import speak
import listen

import sounddevice as sd
import soundfile as sf
import numpy  # Make sure NumPy is loaded before it is used in the callback
#assert numpy  # avoid "imported but unused" message (W0611)
from time import time
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet



def get_all_synonyms(synonyms):
  count = 0
  while count < 3:
    new_list = set()
    word_count = len(synonyms)
    for word in synonyms:
      for ss in wordnet.synsets(word):
        for h in ss.hypernyms():
          new_list.add(h.lemmas()[0].name())
    new_list = new_list.union(synonyms)
    if len(new_list) <= len(synonyms):
      newstuff = False
      return new_list
    synonyms = new_list.copy()
    count += 1
  return new_list


syns = wordnet.synsets("yes")
print(syns[0].definition())
##print(syns[0].lemma_names())
#print(get_all_synonyms(["yes"]))
#print(get_all_synonyms(["yea"]))
##julie = get_database()
##for item in julie.find({}):
##  print(item)
#print(memory.remember("name"))


def match_command(commandslist, response):
  for key in commandslist:
    for matcher in commandslist[key]:
      if matcher in response.lower():
        return key


wakeup_commandslist = {
        "greeting": ["hello", "hey"],
        "available": ["you there"]
}
def get_response(command):
  match command:
    case "greeting":
      return "Hello Jay, what can I do for you?"
    case "available":
      return "I'm here, what can I do for you?"
    case _:
      return "Are you talking to me?"

#heard = listen.listen_for_name()[0]
#command = match_command(wakeup_commandslist, heard)
#
#print(command)
#speak.say(get_response(command))

#heard = listen.list
