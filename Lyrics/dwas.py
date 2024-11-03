import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("I",0.1),
        ("I just woke up from a dream", 0.1),
        ("Where you and I had to say goodbye", 0.09),
        ("And I don't know what it all means", 0.07),
        ("But since I survived I realized", 0.1),
        ("Wherever you go that's where I'll follow", 0.08),
        ("Nobody's promised tomorrow", 0.1),
        ("So I'ma love you every night like", 0.04),
        ("It's the last night", 0.05),
        ("Like it's the last night", 0.06),
        ("If the world was ending", 0.1),
        ("I'd wanna be next to you", 0.1),
        ("If the party was over", 0.1),
        ("And our time on Earth was through", 0.07),
        ("I'd wanna hold you just for a while", 0.1),
        ("And die with a smile", 0.17),
        ("If the world was ending", 0.1),
        ("I'd wanna be next to you", 0.1),
        ("Code lyrics by Duong :3", 0.1)
    ]

    delays = [1.9, 1.0, 1.6, 1.1, 1.5, 1.2, 1.5, 0.7, 0.8, 0.9, 0.1, 3.3, 0.4, 3.4, 1.0, 0.5, 0.4, 0.4, 5.0]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()