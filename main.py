import subprocess

if __name__ == '__main__':
    print("Welcome to robospeaker 1.1 created by PALLAVI")
    while True:
        x = input("Enter what do you want me to speak: ")
        if x.lower() == "q":
            command = 'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
                      '$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; ' \
                      '$speak.Speak(\'bye bye\');"'
            subprocess.run(command, shell=True)
            break
        command = f'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
                  f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; ' \
                  f'$speak.Speak(\'{x}\');"'
        subprocess.run(command, shell=True)
