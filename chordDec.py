import math
import midiExport


class chordDec(midiExport.eventLogger):
    def __init__(self, numTrack: int = 4) -> None:
        super().__init__(numTrack)

        self.chord_name_major = {'I', '0', 'II', '0',
                                 'III', 'IV', '0', 'V', '0', 'VI', '0', 'VII'}
        self.chord_name_minor = {'III', '0', 'IV', '0',
                                 'V', 'VI', '0', 'VII', '0', 'I', '0', 'II'}

        self.isMajor = True

        self.averDelta = 0

        self.isTerminalChord = False

    # 获取历史记录名称
    def getChordHistoryName(self, pos: int) -> str:
        c = self.getChordHistory(pos)
        if c < 0:
            return "0"
        if self.isMajor:
            return self.chord_name_major[c % 12]
        else:
            return self.chord_name_minor[c % 12]

    # 检查终止和弦
    def checkTerminalChord(self):
        c0 = self.getChordHistoryName(1)
        c1 = self.getChordHistoryName(2)
        c2 = self.getChordHistoryName(3)
        c3 = self.getChordHistoryName(4)
        # 第一类：正格终止(Perfect Cadence) 即V->I的和弦进行
        if c0 == 'I' and c1 == 'V' and (c2 == 'II' or c2 == 'IV' or c2 == 'VI'):
            return True
        # 第二类：变格终止(Plagal Cadence) 即IV->I的和弦进行
        if (c1 == 'IV' or c1 == 'II' or c1 == 'VI') and c0 == 'I':
            return True
        # 第三类：阻碍终止(Interrputed Cadencce) V7->I 被 V7->VI代替
        if (c3 == 'V' and c2 == 'I') and (c1 == 'V' and c0 == 'VI'):
            return True
        # 第四类：半终止(Semi Cadence) 任意和弦到V或VII（配合斜率）
        if c0 == 'V' or c0 == 'VII':
            return True
        return False

    # 按id弹奏并使用随机力度信息
    def playIndexRV(self,
                    id: int,
                    level: int,  # 音量，为0说明停止演奏
                    track: int,  # 轨道
                    delta: int = 0
                    ) -> None:
        if delta > 0:
            delta = 0

        vel = math.floor(16 * (math.random() + level - 1))
        if level <= 0 or vel <= 0:
            vel = 0
        elif vel >= 127:
            vel = 127
        self.playIndex(id, vel, track, delta)

    def onFrameBegin(self):
        self.isTerminalChord = self.checkTerminalChord()
