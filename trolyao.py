# phần Nghe.py----------------------------------------------
import speech_recognition 
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
    with speech_recognition.Microphone() as mic: #Giống mic = speech_recognition.Microphone() nhưng khi dùng with máy nói xong sẽ tắt mic
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)

    print("Robot: ...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)

    # phần hieu.py ( AI )---------------------------------------
    if you == "":
        robot_brain = " I can't hear you, try again "
    elif you == "hello": #chỉ nói từ hello mới trl hello huuthong
        robot_brain = " hello Huu Thong "
    elif you == "who love me":
        robot_brain = " it's nun nun "
    elif "name" in you: #chỉ cần câu nói có từ name AI sẽ trl name is siri
        robot_brain = "name is siri"
    elif you == " hello ": #chỉ nói từ hello mới trl hello huuthong
        robot_brain = " hello Huu Thong "
    elif you == "today":  # get current date python trên gg
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif you == "time": 
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M munites %S seconds")
    
    elif "bye" in you:
        robot_brain = "Bye Huu Thong"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain )
        robot_mouth.runAndWait()
        break
    else: 
        robot_brain = " I haven't learned this sentence yet "

    print(robot_brain)

    # Phần noi.py-----------------------------------------------
 

    # Hàm nghe lấy trên gg
    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain )
    robot_mouth.runAndWait()
