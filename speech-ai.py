# MongoDb- 
#  Datebase: Julie
#  Collection: me
#  Document: {name: "Julie"}
#
import argparse
import tempfile

import sys
import keyboard

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


#filename = "recording.wav"
#samplerate = 16000
#channels = 1
#audio_queue = queue.Queue()
#response = [""]


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


#syns = wordnet.synsets("yes")
#print(syns[0].definition())
##print(syns[0].lemma_names())
#print(get_all_synonyms(["yes"]))
#print(get_all_synonyms(["yea"]))
##julie = get_database()
##for item in julie.find({}):
##  print(item)
#print(memory.remember("name"))


#def transcribe(setresponse):
#  model = whisper.load_model("tiny.en")
#  result = model.transcribe(filename, language="english")
#  print(result["text"])
#  setresponse(result["text"])
#
#
#def callback(indata, frames, time, status):
#  """This is called (from a separate thread) for each audio block."""
#  if status:
#    print(status, file=sys.stderr)
#  audio_queue.put(indata.copy())

#def record_voice():
#  print("Press 'q' to quit: ")
#  try:
#    # Make sure the file is opened before recording anything:
#    with sf.SoundFile(filename, mode='w+', samplerate=samplerate, channels=channels) as file:
#      with sd.InputStream(samplerate=samplerate, channels=channels, callback=callback):
#        while True:
#          if keyboard.is_pressed("q"):
#            print("stopping recording")
#            break
#          file.write(audio_queue.get())
#  except Exception as e:
#    exit(type(e).__name__ + ': ' + str(e))

#def set_response(res):
#    response[0] = res
#
#def listen_for_name():
#  starttime = time()
#  innertime = time()
#  try:
#    # Make sure the file is opened before recording anything:
#    file = sf.SoundFile(filename, mode='w', samplerate=samplerate, channels=channels)
#    with sd.InputStream(samplerate=samplerate, channels=channels, callback=callback):
#     #while time()-starttime < 2:
#     while "julie" not in response[0].lower():
#       file.write(audio_queue.get())
#       if time()-innertime >= 2:
#         innertime = time()
#         t = threading.Thread(target=transcribe, args=(set_response, ))
#         t.start()
#         print(response[0])
#       if time()-starttime > 30:
#         starttime = time()
#         file.close()
#         file = sf.SoundFile(filename, mode='w', samplerate=samplerate, channels=channels)
#         print("new file")
#     speak.say("Hello Jay, I am here")
#     print(f"{time()-starttime}s")
#  except Exception as e:
#    exit(type(e).__name__ + ': ' + str(e))

#response = ""
#while "exit" not in response.lower():
#listen_for_name()
  #response = transcribe()
  #print(response)
  #record_voice()
#transcribe()
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

heard = listen.listen_for_name()[0]
command = match_command(wakeup_commandslist, heard)

print(command)
speak.say(get_response(command))

#heard = listen.list
