import pyttsx3


engine = pyttsx3.init()
def onStart(name):
  print(f"starting: {name}")

def onWord(name, location, length):
  print(f"word: {name}, {location}, {length}")
  engine.stop()

def onEnd(name, completed):
  print(f"end: {name}, {completed}")
  #engine.endLoop()

def say(val):
  engine.connect('started-utterance', onStart)
  engine.connect('started-word', onWord)
  engine.connect('finished-utterance', onEnd)
  engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')  # changes the voice
  engine.say(val, 'hello')
  engine.runAndWait()


#say("Hello Jay, what can I do for you?")
#
#say("I'm here, what can I do for you?")
#say("Are you talking to me?")
#
#say("Did I hear my name?")
say("Hello, my love")
