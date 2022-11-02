import whisper

model = whisper.load_model("small")

audio = "Herbert Marcuse and the Frankfurt School (1977)-vm3euZS5nLo.m4a"
transcribe = model.transcribe(audio)


file = open('Herbert Marcuse and the Frankfurt School (1977)-vm3euZS5nLo.txt', 'w')
file.write(transcribe["text"])




#   OUTPUT TO CONSOLE   #
#translate = model.transcribe(audio, task="translate")

#print(transcribe["text"])

#print("TRANSLATED AUDIO")
#print(translate["text"])
#########################