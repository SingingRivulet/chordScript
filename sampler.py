import music21

# 读取MIDI文件
midi = music21.converter.parse('path/to/midi/file')

# 遍历乐谱中的每个小节
for measure in midi.getElementsByClass(music21.stream.Measure):

    # 设置采样间隔（1拍）
    sampling_interval = measure.timeSignature.beatDuration.quarterLength

    # 遍历小节中的所有音符和休止符
    for element in measure.notesAndRests:

        # 如果当前元素是音符，则获取其持续时间
        if isinstance(element, music21.note.Note):
            duration = element.duration.quarterLength

        # 如果当前元素是休止符，则将持续时间设置为0
        else:
            duration = 0

        # 获取当前元素在小节中的位置
        position = element.offset % sampling_interval

        # 如果当前元素跨越小节边界，则将其截断以保持在当前小节中
        if position + duration > sampling_interval:
            duration = sampling_interval - position

        # 如果当前元素完全包含在采样窗口内，则显示它
        if position < sampling_interval and position + duration > 0:
            print(element)
