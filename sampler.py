import music21
# 加载midi文件
midi_path = 'test.mid'
midi_data = music21.converter.parse(midi_path)
bq = midi_data.getTimeSignatures()[0].beatDuration.quarterLength
midi_data.parts[1].flat
for c in midi_data.parts[1].flat:
    c.show("text")
