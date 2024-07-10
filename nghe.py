import speech_recognition 

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic: #Giống mic = speech_recognition.Microphone() nhưng khi dùng with máy nói xong sẽ tắt mic
    print("Robot: I'm listening")
    audio = robot_ear.listen(mic)

try:
    you = robot_ear.recognize_google(audio)
except:
    you = ""
print("You: " + you)