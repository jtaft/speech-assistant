import sounddevice as sd
import soundfile as sf

from time import time

import whisper
import threading
import queue
#import numpy  # Make sure NumPy is loaded before it is used in the callback

filename = "recording.wav"
samplerate = 16000
channels = 1
audio_queue = queue.Queue()
response = [""]

def set_response(res):
    response[0] = res

def transcribe(setresponse):
  model = whisper.load_model("tiny.en")
  result = model.transcribe(filename, language="english")
  print(result["text"])
  setresponse(result["text"])



def callback(indata, frames, time, status):
  """This is called (from a separate thread) for each audio block."""
  if status:
    print(status, file=sys.stderr)
  audio_queue.put(indata.copy())

def listen(condition):
  """ condition is a function that takes a response and returns a bool"""
  starttime = time()
  innertime = time()
  try:
    file = sf.SoundFile(filename, mode='w', samplerate=samplerate, channels=channels)
    with sd.InputStream(samplerate=samplerate, channels=channels, callback=callback):
     while(not condition(response[0])):
       file.write(audio_queue.get())
       if time()-innertime >= 2:
         innertime = time()
         t = threading.Thread(target=transcribe, args=(set_response, ))
         t.start()
         print(response[0])
       if time()-starttime > 30:
         starttime = time()
         file.close()
         file = sf.SoundFile(filename, mode='w', samplerate=samplerate, channels=channels)
         print("new file")
     print(f"{time()-starttime}s")
     return response
  except Exception as e:
    exit(type(e).__name__ + ': ' + str(e))

def is_my_name(response):
  if "julie" in response.lower():
    return True
  return False

def listen_for_name():
  return listen(is_my_name)

def listen
