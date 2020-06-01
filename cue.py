import os
import sys

if len(sys.argv) < 2:
    loc = input("Folder dir: ")
else:
    loc = sys.argv[1]
    
os.chdir(os.path.abspath(loc))

music = [x for x in os.listdir(loc) if not os.path.isdir(x) and os.path.isfile(x)]

with open("{0}.cue".format(loc[loc.rfind('\\') + 1:]), "w") as f:
    for i in range(len(music)):
        song = music[i]
        end = song[song.rfind(".") + 1:]

        barred = ["txt", "py", "gif", "png", "jpg", "jpeg", "zip", "torrent"]

        if end in barred:
            continue

        translation = {
            "flac":"WAVE",
            "mp3":"MP3",
            "wav":"WAVE"
        }

        end = translation.get(end, "WAVE")
        
        f.write(f"FILE \"{song}\" {end}\n  TRACK {'0' * max(0, 2 - len(str(i + 1))) + str(i + 1)} AUDIO\n    INDEX 01 00:00:00\n")