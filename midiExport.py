import music21.midi
import dispatch


class eventLogger(dispatch.dispatcher):
    def __init__(self, numTrack: int = 4) -> None:
        super().__init__()

        self.tracks = []
        self.ins = []

        for i in range(numTrack):
            self.tracks.append([])
            self.ins.append(0)

    # 演奏用的函数
    def playNote(self,
                 tone: int,  # 音高
                 vel: int,  # 音量，为0说明停止演奏
                 track: int  # 轨道
                 ) -> None:

        try:
            t = self.tracks[track]
            t.append((self.fragId, tone, vel))
        except Exception as err:
            print(err)

    # 设置通道的乐器
    def setIns(self,
               track: int,  # 通道
               ins: int  # 乐器id
               ) -> None:
        try:
            self.ins[track] = ins
        except Exception as err:
            print(err)

    # 把事件连接成音符
    def linkEvents(self):
        index = 1

        mf = music21.midi.MidiFile()
        mf.ticksPerQuarterNote = 384

        # 0号轨（留给旋律）
        track0 = music21.midi.MidiTrack(0)
        mf.tracks.append(track0)

        # 0轨的终止符
        me = music21.midi.MidiEvent(track0)
        me.type = "END_OF_TRACK"
        me.channel = 0
        me.data = ''
        track0.events.append(me)

        for trackId in range(len(self.tracks)):

            t = self.tracks[trackId]

            # 创建轨道
            mt = music21.midi.MidiTrack(index)
            index += 1

            # 设置乐器
            mp = music21.midi.MidiEvent(
                type='PROGRAM_CHANGE', time=0, channel=trackId+1)
            mp.data = self.ins[trackId]

            for i in range(len(t)):
                if i == 0:
                    # 第一个音符
                    if t[i][2] > 0:
                        delta = t[i][0]
                        dt = music21.midi.DeltaTime(mt)
                        dt.time = delta*6
                        mt.events.append(dt)
                else:
                    # 后续音符需要间隔
                    delta = t[i][0]-t[i-1][0]
                    dt = music21.midi.DeltaTime(mt)
                    dt.time = delta*6
                    mt.events.append(dt)

                me = music21.midi.MidiEvent(mt)
                if t[i][2] > 0:
                    me.type = "NOTE_ON"
                else:
                    me.type = "NOTE_OFF"
                me.channel = trackId+1
                me.time = None  # t[i][0] * 6
                me.pitch = t[i][1]
                me.velocity = t[i][2]
                mt.events.append(me)

            # 终止标识
            me = music21.midi.MidiEvent(mt)
            me.type = "END_OF_TRACK"
            me.channel = trackId+1
            me.data = ''  # must set data to empty string
            mt.events.append(me)

            mf.tracks.append(mt)
        return mf
