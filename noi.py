import pyttsx3

robot_brain = "I can't hear you, try again"

# Hàm nghe lấy trên gg
robot_mouth = pyttsx3.init()
robot_mouth.say( robot_brain )
robot_mouth.runAndWait()