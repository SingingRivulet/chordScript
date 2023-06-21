import music21
import numpy


def getChordArr(c):
    res = []
    if type(c) == music21.chord.Chord:
        for n in c:
            res.append(n.pitch.midi)
    elif type(c) == music21.note.Note:
        res.append(c.pitch.midi)
    return res


def sampleMidi(midi_path, track_melody=0, track_chord=1):
    # 加载midi文件
    midi_data = music21.converter.parse(midi_path)
    print("len(midi_data.parts) =", len(midi_data.parts))
    midilen = 0

    # print("melody:")
    # for c in midi_data.parts[track_melody].flat:
    #    c.show("text")

    # print("\nchord:")
    for c in midi_data.parts[track_chord].flat:
        # c.show("text")
        #print(c.offset, c.duration.quarterLength, getChordArr(c))
        midilen = int(c.offset+c.duration.quarterLength)

    # print(midilen)

    chordArray = []
    melodyArray = []

    for i in range(midilen):
        chordArray.append([])

    for i in range(midilen*4):
        melodyArray.append(0)

    for c in midi_data.parts[track_chord].flat:
        begin = int(c.offset)
        dur = int(c.duration.quarterLength)
        for i in range(dur):
            chordArray[i+begin] = getChordArr(c)

    for n in midi_data.parts[track_melody].flat:
        if type(n) == music21.note.Note:
            begin = int(n.offset*4)
            dur = int(n.duration.quarterLength*4)
            for i in range(dur):
                melodyArray[i+begin] = n.pitch.midi

    # print(melodyArray)
    kk = music21.analysis.discrete.KrumhanslKessler()
    return melodyArray, chordArray, kk.getSolution(midi_data)
