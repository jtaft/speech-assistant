import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
index = 0
voicedict = dict()
for voice in voices:
  print(index)
  voicedict[index] = voice.id
  engine.setProperty('voice', voice.id)  # changes the voice
  engine.say('The quick brown fox jumped over the lazy dog.')
  engine.runAndWait()
  index+=1

selection = input("Select a voice:")

print(voicedict[int(selection)])
engine.setProperty('voice', voicedict[int(selection)])  # changes the voice
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
