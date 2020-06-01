import os
import sys

if len(sys.argv) < 2:
    loc = input("Folder dir: ")
else:
    loc = sys.argv[1]
    
os.chdir(os.path.abspath(loc))

music = os.listdir(loc)

with open("{0}.cue".format(loc[loc.rfind('\\') + 1:]), "w") as f:
    for i in range(len(music)):
        song = music[i]
        end = song[song.rfind(".") + 1:]

        translation = {
            "flac":"WAVE",
            "mp3":"MP3",
            "wav":"WAVE"
        }

        end = translation.get(end, "WAVE")
        
        f.write(f"FILE \"{song}\" {end}\n  TRACK {'0' * max(0, 2 - len(str(i + 1))) + str(i + 1)} AUDIO\n    INDEX 01 00:00:00\n")