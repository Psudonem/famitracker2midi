import os
from mido import Message, MidiFile, MidiTrack

n=[
        [19,"G-0"],
        [21,"A-0"],
        [22,"A#0"],
        [23,"B-0"],
        [24,"C-1"],
        [25,"C#1"],
        [26,"D-1"],
        [27,"D#1"],
        [28,'E-1'],
        [29,'F-1'],
        [30,'F#1'],
        [31,'G-1'],
        [32,'G#1'],
        [33,"A-1"],
        [34,"A#1"],
        [35,"B-1"],
        [36,"C-2"],
        [37,"C#2"],
        [38,"D-2"],
        [39,"D#2"],
        [40,"E-2"],
        [41,"F-2"],
        [42,"F#2"],
        [43,"G-2"],
        [44,"G#2"],
        [45,"A-2"],
        [46,"A#2"],
        [47,"B-2"],
        [48,"C-3"],
        [49,"C#3"],
        [50,"D-3"],
        [51,"D#3"],
        [52,"E-3"],
        [53,"F-3"],
        [54,"F#3"],
        [55,"G-3"],
        [56,"G#3"],
        [57,"A-3"],
        [58,"A#3"],
        [59,"B-3"],
        [60,"C-4"],
        [61,"C#4"],
        [62,"D-4"],
        [63,"D#4"],
        [64,"E-4"],
        [65,"F-4"],
        [66,"F#4"],
        [67,"G-4"],
        [68,"G#4"],
        [69,"A-4"],
        [70,"A#4"],
        [71,"B-4"],
        [72,"C-5"],
        [73,"C#5"],
        [74,"D-5"],
        [75,"D#5"],
        [76,"E-5"],
        [77,"F-5"],
        [78,"F#5"],
        [79,"G-5"],
        [80,"G#5"],
        [81,"A-5"],
        [82,"A#5"],
        [83,"B-5"],
        [84,"C-6"],
        [85,"C#6"],
        [86,"D-6"],
        [87,"D#6"],
        [88,"E-6"],
        [89,"F-6"],
        [90,"F#6"],
        [91,"G-6"],
        [92,"G#6"],
        [93,"A-6"],
        [94,"A#6"],
        [95,"B-6"],
        [96,'C-7']]


def getNoteNumfromString(note):
    for i in range(0,len(n)):
        if(note in n[i][1]):
            return n[i][0]
    return None

f = open("cha cha.txt", "r")

file = f.read()
f.close()

f= file.split("\n")



trax=[]



mid = MidiFile(type=1)


start=f.index('PATTERN 00')



for i in range(0,3):
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(Message('program_change', program=1, time=0))
    
    for z in range(start, len(f)):
        if('ROW ' in f[z]):
            line=f[z].split(' : ')
            c0note= line[i+1][:3]
            if(c0note!="..." and c0note!="---" and c0note!="==="):
                print(getNoteNumfromString(c0note),c0note)
                track.append(Message('note_on', note=getNoteNumfromString(c0note), velocity=90, time=0))
                track.append(Message('note_off', note=getNoteNumfromString(c0note), velocity=0, time=96))
            else:
                
                track.append(Message('note_on', note=44, velocity=0, time=96))
                #print(c0note)






mid.save('cha cha.mid')
