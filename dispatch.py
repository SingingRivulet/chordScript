import collections
import math

# 播放调度


class dispatcher:
    def __init__(self) -> None:

        self.chord_notes = []  # 和弦的每个音

        self.chord_notes_real = []  # 经过处理的chord_notes

        self.playingNote = set()  # 音符播放状态

        self.autoStopAll = True  # 小节结束时自动停止所有音符

        self.lastFragId = -1  # 上次处理的id

        self.fragId = 0

        self.baseTone = 0  # 变调

        self.bps = 4  # 拍/每小节

        # 和弦历史记录（识别终止和弦要用）
        self.chordHistoryQueue = collections.deque(maxlen=32)

    # 演奏用的函数
    # 这个函数需要重载
    def playNote(self,
                 tone: int,  # 音高
                 vel: int,  # 音量，为0说明停止演奏
                 track: int  # 轨道
                 ) -> None:
        pass

    # 设置通道的乐器
    # 这个函数需要重载
    def setIns(self,
               track: int,  # 通道
               ins: int  # 乐器id
               ) -> None:
        pass

    # 和弦脚本主函数
    # 这个函数需要重载
    def process_callback(self) -> None:
        yield

    # 每一帧开始时触发
    # 这个函数需要重载
    def onFrameBegin(self) -> None:
        pass

    # 处理主函数
    # 注意：这个函数是协程
    def process(self):
        self.fragId = 0
        self.lastFragId = -1
        secId_now = int(math.floor(self.fragId / (16. * self.bps)))
        secId_last = int(math.floor(self.lastFragId / (16. * self.bps)))
        yield self
        for ignore in self.process_callback():
            secId_now = int(math.floor(self.fragId / (16. * self.bps)))
            secId_last = int(math.floor(self.lastFragId / (16. * self.bps)))
            if self.autoStopAll and secId_now != secId_last:
                self.stopAll()
            self.lastFragId = self.fragId

            yield self

    # 停止所有音符
    def stopAll(self) -> None:
        for note in self.playingNote:
            tone = note[0]
            channel = note[1]
            self.playNote(tone, 0, channel)

    # 设置和弦
    def setChord(self, notes: list) -> None:
        self.chord_notes = notes
        self.chord_notes_real = []

        if len(notes) <= 0:
            return

        last = notes[0]-1
        for it in notes:
            n = (it - self.baseTone + 12) % 12
            while n < last:
                n += 12
            last = n
            self.chord_notes_real.append(n)

        # 设置历史记录
        if len(self.chord_notes_real) > 0:
            note = self.chord_notes_real[0]
            if len(self.chordHistoryQueue) == 0 or self.chordHistoryQueue[-1] != note:
                self.chordHistoryQueue.append(note)

    # 弹奏（音高）
    def play(self,
             tone: int,  # 音高
             vel: int,  # 音量，为0说明停止演奏
             track: int  # 轨道
             ) -> None:

        tone += self.baseTone
        notepair = (tone, track)

        if vel > 0:
            if notepair in self.playingNote:
                self.playNote(tone, 0, track)  # 先关闭再重新启动
            self.playingNote.add(notepair)
            self.playNote(tone, vel, track)
        else:
            self.playingNote.pop(notepair)
            self.playNote(tone, 0, track)

    # 按id弹奏
    def playIndex(self,
                  id: int,
                  vel: int,  # 音量，为0说明停止演奏
                  track: int,  # 轨道
                  delta: int = 0
                  ) -> None:
        if id < 0 or id >= len(self.chord_notes_real):
            return
        tone = self.chord_notes_real[id]+delta
        self.play(tone, vel, track)

    # 获取音符数量
    def playListSize(self) -> int:
        return len(self.playingNote)

    # 移动和弦列表的八度到指定范围（常函数，返回需要移动的数值）
    def shiftPlayList(self, target: int) -> int:

        if len(self.chord_notes_real) == 0:
            return 0

        tone = self.chord_notes_real[0] % 12
        while tone < target:
            tone += 12

        delta = tone - self.chord_notes_real[0]
        return delta

    # 查询历史记录
    def getChordHistory(self, pos: int) -> int:
        try:
            return self.chordHistoryQueue[-pos]
        except Exception:
            return -1

    # 跳到下一帧
    def sleepSec(self):
        yield
        self.onFrameBegin()

    # 等到指定时间
    def waitTime(self, time: int):
        while self.fragId != time:
            yield from self.sleepSec()


# 测试
#d = dispatcher()
# for s in d.process():
#    pass
