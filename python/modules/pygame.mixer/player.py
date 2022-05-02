from pygame import mixer

"""define a function"""
def play(file):
    mixer.init() #to initialize pygame (Must)
    mixer.music.load(file) #to load file from path
    # mixer.music.play() #it will play by loop
    # mixer.music.play(loops=0) #to disable loop playing
    while True:
        usr_input  = input("Enter your commands: ")
        if usr_input == "play":
            mixer.music.play(loops=0)
        elif usr_input == "stop":
            mixer.music.stop()
            break
        elif usr_input == "pause":
            mixer.music.pause()
        elif usr_input == "unpause":
            mixer.music.unpause()

if __name__=="__main__":
    path = "/home/thor/Music/nightmare-90160.mp3"
    play(path)