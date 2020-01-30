
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()
# yell=shout

def person_does(name, func):
    return name + " says " + func("HoW hAs yoUr dAy bEEn?")

message = person_does("Eric", shout)
print(message)
message = person_does("Eric", whisper)
print(message)