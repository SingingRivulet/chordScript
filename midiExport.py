import dispatch
import mido


class eventLogger(dispatch.dispatcher):
    def __init__(self, numTrack: int = 4) -> None:
        super().__init__()

        self.tracks = []
        self.ins = []
        self.notes = []
        self.statusMapper = dict()

        for i in range(numTrack):
            self.tracks.append([])
            self.ins.append(0)

    # 演奏用的函数
    def playNote(self,
                 tone: int,  # 音高
                 vel: int,  # 音量，为0说明停止演奏
                 track: int  # 轨道
                 ) -> None:

        if tone >= 127 or tone <= 0:
            return

        try:
            t = self.tracks[track]
            t.append((self.fragId, tone, vel))
            #print("play:", self.fragId/(384/6), tone, vel)
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
    def linkEvents(self, tpq=384):
        index = 1

        mf = mido.MidiFile(type=1, ticks_per_beat=tpq)
        k = tpq/16

        # 0号轨（留给旋律）
        track0 = mido.MidiTrack()
        mf.tracks.append(track0)

        for trackId in range(len(self.tracks)):

            t = self.tracks[trackId]

            # 创建轨道
            mt = mido.MidiTrack()
            index += 1

            # 设置乐器
            mp = mido.Message('program_change', program=self.ins[trackId],
                              time=0, channel=trackId+1)
            mt.append(mp)

            for i in range(len(t)):
                if i == 0:
                    # 第一个音符
                    if t[i][2] > 0:
                        delta = t[i][0]
                        mnote = mido.Message('note_on',
                                             note=t[i][1],
                                             velocity=0,
                                             time=int(delta*k))
                        mt.append(mnote)
                else:
                    # 后续音符需要间隔
                    delta = t[i][0]-t[i-1][0]
                    delta = int(delta*k)

                    if t[i][2] > 0:
                        mnote = mido.Message('note_on',
                                             note=t[i][1],
                                             velocity=t[i][2],
                                             time=delta,
                                             channel=trackId+1)
                        mt.append(mnote)
                    else:

                        mnote = mido.Message('note_off',
                                             note=t[i][1],
                                             velocity=t[i][2],
                                             time=delta,
                                             channel=trackId+1)
                        mt.append(mnote)

            mf.tracks.append(mt)
        return mf
