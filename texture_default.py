import math
import sys
import chordDec
import mido
import sampler
import numpy


class texture_default(chordDec.chordDec):

    def isRefrain(self) -> bool:
        return self.averDelta > 1

    def play_m_1(self):
        # 主歌钢琴1：最舒缓的弹奏模式，和弦中低音部分弹二分音符，高音部分弹四分音符。具体格式如下：
        self.setIns(1, 0)  # 设置一号通道为钢琴
        guitarShift = self.shiftPlayList(40)
        pianoShift = self.shiftPlayList(36)
        print("pianoShift", pianoShift)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,0,2,Piano,p5]
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,0,1,Piano,p5]
        self.playIndexRV(3, 5 - 2, 1, pianoShift)  # [3,0,1,Piano,p5]
        self.playIndexRV(4, 5 - 2, 1, pianoShift)  # [4,0,1,Piano,p5]
        self.playIndexRV(5, 5 - 2, 1, pianoShift)  # [5,0,1,Piano,p5]
        yield from self.waitTime(16)
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,1,1,Piano,p4]
        self.playIndexRV(3, 4 - 2, 1, pianoShift)  # [3,1,1,Piano,p4]
        self.playIndexRV(4, 4 - 2, 1, pianoShift)  # [4,1,1,Piano,p4]
        self.playIndexRV(5, 4 - 2, 1, pianoShift)  # [5,1,1,Piano,p4]
        yield from self.waitTime(32)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,2,2,Piano,p5]
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,2,1,Piano,p4]
        self.playIndexRV(3, 4 - 2, 1, pianoShift)  # [3,2,1,Piano,p4]
        self.playIndexRV(4, 4 - 2, 1, pianoShift)  # [4,2,1,Piano,p4]
        self.playIndexRV(5, 4 - 2, 1, pianoShift)  # [5,2,1,Piano,p4]
        yield from self.waitTime(48)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,3,1,Piano,p5]
        self.playIndexRV(3, 5 - 2, 1, pianoShift)  # [3,3,1,Piano,p5]
        self.playIndexRV(4, 5 - 2, 1, pianoShift)  # [4,3,1,Piano,p5]
        self.playIndexRV(5, 5 - 2, 1, pianoShift)  # [5,3,1,Piano,p5]

    def play_m_2(self):
        # 主歌钢琴2：模仿流行音乐中电贝司的弹法。
        # 在主歌钢琴1的基础上，每小节最后半拍加一个和弦最低音的八分音符。具体格式如下：
        self.setIns(1, 0)  # 设置一号通道为钢琴
        guitarShift = self.shiftPlayList(40)
        pianoShift = self.shiftPlayList(36)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,0,2,Piano,p5]
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,0,1,Piano,p5]
        self.playIndexRV(3, 5 - 2, 1, pianoShift)  # [3,0,1,Piano,p5]
        self.playIndexRV(4, 5 - 2, 1, pianoShift)  # [4,0,1,Piano,p5]
        self.playIndexRV(5, 5 - 2, 1, pianoShift)  # [5,0,1,Piano,p5]
        yield from self.waitTime(16)
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,1,1,Piano,p4]
        self.playIndexRV(3, 4 - 2, 1, pianoShift)  # [3,1,1,Piano,p4]
        self.playIndexRV(4, 4 - 2, 1, pianoShift)  # [4,1,1,Piano,p4]
        self.playIndexRV(5, 4 - 2, 1, pianoShift)  # [5,1,1,Piano,p4]
        yield from self.waitTime(24)
        self.playIndexRV(1, 4 - 2, 1, pianoShift)  # [1,1.5,0.5,Piano,p4]
        yield from self.waitTime(32)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,2,2,Piano,p5]
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,2,1,Piano,p4]
        self.playIndexRV(3, 4 - 2, 1, pianoShift)  # [3,2,1,Piano,p4]
        self.playIndexRV(4, 4 - 2, 1, pianoShift)  # [4,2,1,Piano,p4]
        self.playIndexRV(5, 4 - 2, 1, pianoShift)  # [5,2,1,Piano,p4]
        yield from self.waitTime(48)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,3,1,Piano,p5]
        self.playIndexRV(3, 5 - 2, 1, pianoShift)  # [3,3,1,Piano,p5]
        self.playIndexRV(4, 5 - 2, 1, pianoShift)  # [4,3,1,Piano,p5]
        self.playIndexRV(5, 5 - 2, 1, pianoShift)  # [5,3,1,Piano,p5]
        yield from self.waitTime(56)
        self.playIndexRV(1, 4 - 2, 1, pianoShift)  # [1,3.5,0.5,Piano,p4]

    def play_m_3(self):
        # 主歌钢琴3：主歌太长时，将小节中第一、二、四拍的第二个音改为后半拍开始。具体格式如下：
        self.setIns(1, 0)  # 设置一号通道为钢琴
        guitarShift = self.shiftPlayList(40)
        pianoShift = self.shiftPlayList(36)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,0,2,Piano,p5]
        self.playIndexRV(3, 5 - 2, 1, pianoShift)  # [3,0,1,Piano,p5]
        self.playIndexRV(4, 5 - 2, 1, pianoShift)  # [4,0,1,Piano,p5]
        self.playIndexRV(5, 5 - 2, 1, pianoShift)  # [5,0,1,Piano,p5]
        yield from self.waitTime(8)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,0.5,1,Piano,p5]
        yield from self.waitTime(16)
        self.playIndexRV(3, 5 - 2, 1, pianoShift)  # [3,1,1,Piano,p5]
        self.playIndexRV(4, 5 - 2, 1, pianoShift)  # [4,1,1,Piano,p5]
        self.playIndexRV(5, 5 - 2, 1, pianoShift)  # [5,1,1,Piano,p5]
        yield from self.waitTime(24)
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,1.5,0.5,Piano,p4]
        yield from self.waitTime(32)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,2,2,Piano,p5]
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,2,1.5,Piano,p4]
        self.playIndexRV(3, 4 - 2, 1, pianoShift)  # [3,2,1,Piano,p4]
        self.playIndexRV(4, 4 - 2, 1, pianoShift)  # [4,2,1,Piano,p4]
        self.playIndexRV(5, 4 - 2, 1, pianoShift)  # [5,2,1,Piano,p4]
        yield from self.waitTime(48)
        self.playIndexRV(3, 5 - 2, 1, pianoShift)  # [3,3,1,Piano,p5]
        self.playIndexRV(4, 5 - 2, 1, pianoShift)  # [4,3,1,Piano,p5]
        self.playIndexRV(5, 5 - 2, 1, pianoShift)  # [5,3,1,Piano,p5]
        yield from self.waitTime(56)
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,3.5,0.5,Piano,p4]

    def play_m_s(self):
        # 终止和弦
        # 主歌钢琴加花：
        self.setIns(1, 0)  # 设置一号通道为钢琴
        guitarShift = self.shiftPlayList(40)
        pianoShift = self.shiftPlayList(36)
        # 主歌乐句过渡处，在主歌钢琴2的基础上，
        # 最后一拍取代为以十六分音符弹当前和弦高八度的1232音。具体格式如下：

        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,0,2,Piano,p5]
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,0,1,Piano,p5]
        self.playIndexRV(3, 5 - 2, 1, pianoShift)  # [3,0,1,Piano,p5]
        self.playIndexRV(4, 5 - 2, 1, pianoShift)  # [4,0,1,Piano,p5]
        self.playIndexRV(5, 5 - 2, 1, pianoShift)  # [5,0,1,Piano,p5]

        yield from self.waitTime(16)
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,1,1,Piano,p4]
        self.playIndexRV(3, 4 - 2, 1, pianoShift)  # [3,1,1,Piano,p4]
        self.playIndexRV(4, 4 - 2, 1, pianoShift)  # [4,1,1,Piano,p4]
        self.playIndexRV(5, 4 - 2, 1, pianoShift)  # [5,1,1,Piano,p4]

        yield from self.waitTime(24)
        self.playIndexRV(1, 4 - 2, 1, pianoShift)  # [1,1.5,0.5,Piano,p4]

        yield from self.waitTime(32)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,2,2,Piano,p5]
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,2,1,Piano,p4]
        self.playIndexRV(3, 4 - 2, 1, pianoShift)  # [3,2,1,Piano,p4]
        self.playIndexRV(4, 4 - 2, 1, pianoShift)  # [4,2,1,Piano,p4]
        self.playIndexRV(5, 4 - 2, 1, pianoShift)  # [5,2,1,Piano,p4]

        yield from self.waitTime(48)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,3,1,Piano,p5]

        yield from self.waitTime(52)
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,3.25,0.75,Piano,p4]

        yield from self.waitTime(56)
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,3.5,0.5,Piano,p6]

        yield from self.waitTime(60)
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,3.75,0.25,Piano,p4]

    def play_r_1_1(self):
        # 副歌钢琴1：每小节的第一、二拍的第二个音变为后半拍开始；
        # 每小节第二拍的最后四分之一拍添加一个根音；
        # 每小节第三拍后半拍添加当前和弦第二个音；
        # 每小节第三拍的最后四分之一拍添加当前和弦所有除了根音之外的16分音符；
        # 每小节最后一拍第一个16分空掉，后三个依次弹当前和弦高八度的321音；
        # 第四小节最后一拍的三个音的顺序改成123音（Cmaj7就是CEG）。
        # 各小节具体格式如下：
        # 第一小节：
        self.setIns(1, 0)  # 设置一号通道为钢琴
        self.setIns(2, 24)  # 设置二号通道为吉他
        guitarShift = self.shiftPlayList(40)
        pianoShift = self.shiftPlayList(36)

        self.playIndexRV(1, 6 - 2, 1, pianoShift)  # [1,0,1.75,Piano,p6]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,0,1,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,0,1,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,0,1,Piano,p6]
        yield from self.waitTime(8)
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,0.5,1,Piano,p4]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,0.5,1.25,Guitar,g5]
        yield from self.waitTime(12)
        self.playIndexRV(2, 6, 2, guitarShift)  # [2,0.75,1.25,Guitar,g6]
        yield from self.waitTime(16)
        self.playIndexRV(3, 5 - 2, 1, pianoShift)  # [3,1,1,Piano,p5]
        self.playIndexRV(4, 5 - 2, 1, pianoShift)  # [4,1,1,Piano,p5]
        self.playIndexRV(5, 5 - 2, 1, pianoShift)  # [5,1,1,Piano,p5]
        yield from self.waitTime(20)
        self.playIndexRV(3, 7, 2, guitarShift)  # [3,1.25,0.75,Guitar,g7]
        yield from self.waitTime(24)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,1.5,0.5,Piano,p5]
        yield from self.waitTime(28)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,1.75,0.25,Piano,p5]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,1.75,0.25,Guitar,g5]
        yield from self.waitTime(32)
        self.playIndexRV(1, 6 - 2, 1, pianoShift)  # [1,2,2,Piano,p6]
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,2,0.5,Piano,p5]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,2,0.75,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,2,0.75,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,2,0.75,Piano,p6]
        self.playIndexRV(1, 6, 2, guitarShift)  # [1,2,1.75,Guitar,g6]
        self.playIndexRV(3, 6, 2, guitarShift)  # [3,2,0.75,Guitar,g6]
        yield from self.waitTime(40)
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,2.5,0.25,Piano,p4]
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,2.5,0.75,Guitar,g4]
        yield from self.waitTime(44)
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,2.75,1.25,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,2.75,1.25,Piano,p6]
        self.playIndexRV(2, 6 - 2, 1, pianoShift)  # [2,2.75,1.25,Piano,p6]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,2.75,1.25,Piano,p6]
        self.playIndexRV(3, 6, 2, guitarShift)  # [3,2.75,1.25,Guitar,g6]
        yield from self.waitTime(52)
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,3.25,0.75,Piano,p6]
        self.playIndexRV(2, 5, 2, guitarShift)  # [2,3.25,0.75,Guitar,g5]
        yield from self.waitTime(56)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,3.5,0.5,Piano,p5]
        yield from self.waitTime(60)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,3.75,0.25,Piano,p5]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,3.75,0.25,Guitar,g5]

    def play_r_1_2(self):
        # 第二小节：
        self.setIns(1, 0)  # 设置一号通道为钢琴
        self.setIns(2, 24)  # 设置二号通道为吉他
        guitarShift = self.shiftPlayList(40)
        pianoShift = self.shiftPlayList(36)
        self.playIndexRV(1, 6 - 2, 1, pianoShift)  # [1,0,2,Piano,p6]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,0,1,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,0,1,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,0,1,Piano,p6]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,0,1.75,Guitar,g5]
        yield from self.waitTime(8)
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,0.5,1,Piano,p4]
        yield from self.waitTime(12)
        self.playIndexRV(2, 6, 2, guitarShift)  # [2,0.75,1.25,Guitar,g6]
        yield from self.waitTime(16)
        self.playIndexRV(3, 5 - 2, 1, pianoShift)  # [3,1,1,Piano,p5]
        self.playIndexRV(4, 5 - 2, 1, pianoShift)  # [4,1,1,Piano,p5]
        self.playIndexRV(5, 5 - 2, 1, pianoShift)  # [5,1,1,Piano,p5]
        yield from self.waitTime(20)
        self.playIndexRV(3, 7, 2, guitarShift)  # [3,1.25,0.75,Guitar,g7]
        yield from self.waitTime(24)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,1.5,0.5,Piano,p5]
        yield from self.waitTime(28)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,1.75,0.25,Piano,p5]
        self.playIndexRV(1, 4, 2, guitarShift)  # [1,1.75,0.25,Guitar,g4]
        yield from self.waitTime(32)
        self.playIndexRV(1, 6 - 2, 1, pianoShift)  # [1,2,2,Piano,p6]
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,2,0.5,Piano,p5]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,2,0.75,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,2,0.75,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,2,0.75,Piano,p6]
        self.playIndexRV(2, 5, 2, guitarShift)  # [2,2,0.75,Guitar,g5]
        yield from self.waitTime(40)
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,2.5,0.25,Piano,p4]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,2.5,1.5,Guitar,g5]
        yield from self.waitTime(44)
        self.playIndexRV(2, 6 - 2, 1, pianoShift)  # [2,2.75,1.25,Piano,p6]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,2.75,1.25,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,2.75,1.25,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,2.75,1.25,Piano,p6]
        self.playIndexRV(2, 5, 2, guitarShift)  # [2,2.75,1.25,Guitar,g5]
        yield from self.waitTime(52)
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,3.25,0.75,Piano,p6]
        self.playIndexRV(3, 6, 2, guitarShift)  # [3,3.25,0.75,Guitar,g6]
        yield from self.waitTime(56)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,3.5,0.5,Piano,p5]
        yield from self.waitTime(60)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,3.75,0.25,Piano,p5]

    def play_r_1_3(self):
        # 第三小节：
        self.setIns(1, 0)  # 设置一号通道为钢琴
        self.setIns(2, 24)  # 设置二号通道为吉他
        guitarShift = self.shiftPlayList(40)
        pianoShift = self.shiftPlayList(36)
        self.playIndexRV(1, 6 - 2, 1, pianoShift)  # [1,0,2,Piano,p6]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,0,1,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,0,1,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,0,1,Piano,p6]
        self.playIndexRV(2, 6, 2, guitarShift)  # [2,0,0.75,Guitar,g6]
        yield from self.waitTime(8)
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,0.5,1,Piano,p4]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,0.5,1.25,Guitar,g5]
        yield from self.waitTime(12)
        self.playIndexRV(2, 6, 2, guitarShift)  # [2,0.75,1.25,Guitar,g6]
        yield from self.waitTime(16)
        self.playIndexRV(3, 5 - 2, 1, pianoShift)  # [3,1,1,Piano,p5]
        self.playIndexRV(4, 5 - 2, 1, pianoShift)  # [4,1,1,Piano,p5]
        self.playIndexRV(5, 5 - 2, 1, pianoShift)  # [5,1,1,Piano,p5]
        yield from self.waitTime(20)
        self.playIndexRV(3, 7, 2, guitarShift)  # [3,1.25,0.75,Guitar,g7]
        yield from self.waitTime(24)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,1.5,0.5,Piano,p5]
        yield from self.waitTime(28)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,1.75,0.75,Piano,p5]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,1.75,0.25,Guitar,g5]
        yield from self.waitTime(32)
        self.playIndexRV(1, 6 - 2, 1, pianoShift)  # [1,2,2,Piano,p6]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,2,0.75,Piano,p6]
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,2,0.5,Piano,p5]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,2,0.75,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,2,0.75,Piano,p6]
        yield from self.waitTime(36)
        self.playIndexRV(1, 7, 2, guitarShift)  # [1,2.25,1.5,Guitar,g7]
        self.playIndexRV(2, 7, 2, guitarShift)  # [2,2.25,1,Guitar,g7]
        yield from self.waitTime(40)
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,2.5,0.25,Piano,p4]
        yield from self.waitTime(44)
        self.playIndexRV(2, 7 - 2, 1, pianoShift)  # [2,2.75,0.25,Piano,p7]
        self.playIndexRV(3, 7 - 2, 1, pianoShift)  # [3,2.75,0.25,Piano,p7]
        self.playIndexRV(4, 7 - 2, 1, pianoShift)  # [4,2.75,0.25,Piano,p7]
        self.playIndexRV(5, 7 - 2, 1, pianoShift)  # [5,2.75,0.25,Piano,p7]
        self.playIndexRV(3, 7, 2, guitarShift)  # [3,2.75,1.25,Guitar,g7]
        yield from self.waitTime(52)
        self.playIndexRV(3, 7 - 2, 1, pianoShift)  # [3,3.25,0.75,Piano,p7]
        self.playIndexRV(2, 5, 2, guitarShift)  # [2,3.25,0.75,Guitar,g5]
        yield from self.waitTime(56)
        self.playIndexRV(2, 6 - 2, 1, pianoShift)  # [2,3.5,0.5,Piano,p6]
        yield from self.waitTime(60)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,3.75,0.25,Piano,p5]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,3.75,0.25,Guitar,g5]

    def play_r_1_4(self):
        # 第四小节：
        self.setIns(1, 0)  # 设置一号通道为钢琴
        self.setIns(2, 24)  # 设置二号通道为吉他
        guitarShift = self.shiftPlayList(40)
        pianoShift = self.shiftPlayList(36)
        self.playIndexRV(1, 6 - 2, 1, pianoShift)  # [1,0,2,Piano,p6]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,0,1,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,0,1,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,0,1,Piano,p6]
        self.playIndexRV(1, 6, 2, guitarShift)  # [1,0,1.75,Guitar,g6]
        yield from self.waitTime(8)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,0.5,1,Piano,p5]
        yield from self.waitTime(12)
        self.playIndexRV(2, 6, 2, guitarShift)  # [2,0.75,1.25,Guitar,g6]
        yield from self.waitTime(16)
        self.playIndexRV(3, 7 - 2, 1, pianoShift)  # [3,1,1,Piano,p7]
        self.playIndexRV(4, 7 - 2, 1, pianoShift)  # [4,1,1,Piano,p7]
        self.playIndexRV(5, 7 - 2, 1, pianoShift)  # [5,1,1,Piano,p7]
        yield from self.waitTime(20)
        self.playIndexRV(3, 7, 2, guitarShift)  # [3,1.25,0.75,Guitar,g7]
        yield from self.waitTime(24)
        self.playIndexRV(2, 6 - 2, 1, pianoShift)  # [2,1.5,0.5,Piano,p6]
        yield from self.waitTime(28)
        self.playIndexRV(1, 6 - 2, 1, pianoShift)  # [1,1.75,0.25,Piano,p6]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,1.75,0.25,Guitar,g5]
        yield from self.waitTime(32)
        self.playIndexRV(1, 7 - 2, 1, pianoShift)  # [1,2,2,Piano,p7]
        self.playIndexRV(2, 6 - 2, 1, pianoShift)  # [2,2,0.5,Piano,p6]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,2,0.75,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,2,0.75,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,2,0.75,Piano,p6]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,2,1.75,Guitar,g5]
        yield from self.waitTime(40)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,2.5,0.25,Piano,p5]
        self.playIndexRV(2, 6, 2, guitarShift)  # [2,2.5,1,Guitar,g6]
        yield from self.waitTime(44)
        self.playIndexRV(2, 7 - 2, 1, pianoShift)  # [2,2.75,1.25,Piano,p7]
        self.playIndexRV(3, 7 - 2, 1, pianoShift)  # [3,2.75,1.25,Piano,p7]
        self.playIndexRV(4, 7 - 2, 1, pianoShift)  # [4,2.75,1.25,Piano,p7]
        self.playIndexRV(5, 7 - 2, 1, pianoShift)  # [5,2.75,1.25,Piano,p7]
        self.playIndexRV(3, 7, 2, guitarShift)  # [3,2.75,1.25,Guitar,g7]
        yield from self.waitTime(52)
        self.playIndexRV(1, 6 - 2, 1, pianoShift)  # [1,3.25,0.75,Piano,p6]
        self.playIndexRV(2, 6, 2, guitarShift)  # [2,3.25,0.75,Guitar,g6]
        yield from self.waitTime(56)
        self.playIndexRV(2, 7 - 2, 1, pianoShift)  # [2,3.5,0.5,Piano,p7]
        yield from self.waitTime(60)
        self.playIndexRV(3, 7 - 2, 1, pianoShift)  # [3,3.75,0.25,Piano,p7]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,3.75,0.25,Guitar,g5]

    def play_r_2_1(self):
        # 副歌钢琴2：是副歌钢琴1的变形，情绪上更加递进一些。各小节具体格式如下：
        # 第一小节：
        self.setIns(1, 0)  # 设置一号通道为钢琴
        self.setIns(2, 24)  # 设置二号通道为吉他
        guitarShift = self.shiftPlayList(40)
        pianoShift = self.shiftPlayList(36)
        self.playIndexRV(1, 7 - 2, 1, pianoShift)  # [1,0,2,Piano,p7]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,0,1,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,0,1,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,0,1,Piano,p6]
        yield from self.waitTime(8)
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,0.5,1.25,Guitar,g5]
        yield from self.waitTime(12)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,0.75,0.75,Piano,p5]
        self.playIndexRV(2, 6, 2, guitarShift)  # [2,0.75,1.25,Guitar,g6]
        yield from self.waitTime(16)
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,1,0.75,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,1,0.75,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,1,0.75,Piano,p6]
        yield from self.waitTime(20)
        self.playIndexRV(3, 7, 2, guitarShift)  # [3,1.25,0.75,Guitar,g7]
        yield from self.waitTime(24)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,1.5,0.25,Piano,p5]
        yield from self.waitTime(28)
        self.playIndexRV(2, 7 - 2, 1, pianoShift)  # [2,1.75,0.25,Piano,p7]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,1.75,0.25,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,1.75,0.25,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,1.75,0.25,Piano,p6]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,1.75,0.25,Guitar,g5]
        yield from self.waitTime(32)
        self.playIndexRV(1, 6 - 2, 1, pianoShift)  # [1,2,2,Piano,p6]
        self.playIndexRV(1, 6, 2, guitarShift)  # [1,2,1.75,Guitar,g6]
        self.playIndexRV(3, 6, 2, guitarShift)  # [3,2,0.75,Guitar,g6]
        yield from self.waitTime(36)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,2.25,0.25,Piano,p5]
        self.playIndexRV(3, 5 - 2, 1, pianoShift)  # [3,2.25,0.5,Piano,p5]
        self.playIndexRV(4, 5 - 2, 1, pianoShift)  # [4,2.25,0.5,Piano,p5]
        self.playIndexRV(5, 5 - 2, 1, pianoShift)  # [5,2.25,0.5,Piano,p5]
        yield from self.waitTime(40)
        self.playIndexRV(2, 6 - 2, 1, pianoShift)  # [2,2.5,0.25,Piano,p6]
        self.playIndexRV(2, 4, 2, guitarShift)  # [2,2.5,0.75,Guitar,g4]
        yield from self.waitTime(44)
        self.playIndexRV(2, 7 - 2, 1, pianoShift)  # [2,2.75,1.25,Piano,p7]
        self.playIndexRV(3, 7 - 2, 1, pianoShift)  # [3,2.75,1.25,Piano,p7]
        self.playIndexRV(4, 7 - 2, 1, pianoShift)  # [4,2.75,1.25,Piano,p7]
        self.playIndexRV(5, 7 - 2, 1, pianoShift)  # [5,2.75,1.25,Piano,p7]
        self.playIndexRV(3, 6, 2, guitarShift)  # [3,2.75,1.25,Guitar,g6]
        yield from self.waitTime(52)
        self.playIndexRV(3, 7 - 2, 1, pianoShift)  # [3,3.25,0.75,Piano,p7]
        self.playIndexRV(2, 5, 2, guitarShift)  # [2,3.25,0.75,Guitar,g5]
        yield from self.waitTime(56)
        self.playIndexRV(2, 6 - 2, 1, pianoShift)  # [2,3.5,0.5,Piano,p6]
        yield from self.waitTime(60)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,3.75,0.25,Piano,p5]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,3.75,0.25,Guitar,g5]

    def play_r_2_2(self):
        # 第二小节：
        self.setIns(1, 0)  # 设置一号通道为钢琴
        self.setIns(2, 24)  # 设置二号通道为吉他
        guitarShift = self.shiftPlayList(40)
        pianoShift = self.shiftPlayList(36)
        self.playIndexRV(1, 7 - 2, 1, pianoShift)  # [1,0,2,Piano,p7]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,0,1,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,0,1,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,0,1,Piano,p6]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,0,1.75,Guitar,g5]
        yield from self.waitTime(8)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,0.5,1,Piano,p5]
        yield from self.waitTime(12)
        self.playIndexRV(2, 6, 2, guitarShift)  # [2,0.75,1.25,Guitar,g6]
        yield from self.waitTime(16)
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,1,0.75,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,1,0.75,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,1,0.75,Piano,p6]
        yield from self.waitTime(20)
        self.playIndexRV(3, 7, 2, guitarShift)  # [3,1.25,0.75,Guitar,g7]
        yield from self.waitTime(24)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,1.5,0.25,Piano,p5]
        yield from self.waitTime(28)
        self.playIndexRV(2, 6 - 2, 1, pianoShift)  # [2,1.75,0.25,Piano,p6]
        self.playIndexRV(3, 5 - 2, 1, pianoShift)  # [3,1.75,0.25,Piano,p5]
        self.playIndexRV(4, 5 - 2, 1, pianoShift)  # [4,1.75,0.25,Piano,p5]
        self.playIndexRV(5, 5 - 2, 1, pianoShift)  # [5,1.75,0.25,Piano,p5]
        self.playIndexRV(1, 4, 2, guitarShift)  # [1,1.75,0.25,Guitar,g4]
        yield from self.waitTime(32)
        self.playIndexRV(1, 6 - 2, 1, pianoShift)  # [1,2,2,Piano,p6]
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,2,0.5,Piano,p5]
        self.playIndexRV(3, 5 - 2, 1, pianoShift)  # [3,2,0.75,Piano,p5]
        self.playIndexRV(4, 5 - 2, 1, pianoShift)  # [4,2,0.75,Piano,p5]
        self.playIndexRV(5, 5 - 2, 1, pianoShift)  # [5,2,0.75,Piano,p5]
        self.playIndexRV(2, 5, 2, guitarShift)  # [2,2,0.75,Guitar,g5]
        yield from self.waitTime(40)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,2.5,0.25,Piano,p5]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,2.5,1.5,Guitar,g5]
        yield from self.waitTime(44)
        self.playIndexRV(2, 7 - 2, 1, pianoShift)  # [2,2.75,1.25,Piano,p7]
        self.playIndexRV(3, 7 - 2, 1, pianoShift)  # [3,2.75,1.25,Piano,p7]
        self.playIndexRV(4, 7 - 2, 1, pianoShift)  # [4,2.75,1.25,Piano,p7]
        self.playIndexRV(5, 7 - 2, 1, pianoShift)  # [5,2.75,1.25,Piano,p7]
        self.playIndexRV(2, 5, 2, guitarShift)  # [2,2.75,1.25,Guitar,g5]
        yield from self.waitTime(52)
        self.playIndexRV(3, 7 - 2, 1, pianoShift)  # [3,3.25,0.75,Piano,p7]
        self.playIndexRV(3, 6, 2, guitarShift)  # [3,3.25,0.75,Guitar,g6]
        yield from self.waitTime(56)
        self.playIndexRV(2, 6 - 2, 1, pianoShift)  # [2,3.5,0.5,Piano,p6]
        yield from self.waitTime(60)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,3.75,0.25,Piano,p5]

    def play_r_2_3(self):
        # 第三小节：
        self.setIns(1, 0)  # 设置一号通道为钢琴
        self.setIns(2, 24)  # 设置二号通道为吉他
        guitarShift = self.shiftPlayList(40)
        pianoShift = self.shiftPlayList(36)
        self.playIndexRV(1, 7 - 2, 1, pianoShift)  # [1,0,2,Piano,p7]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,0,1,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,0,1,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,0,1,Piano,p6]
        self.playIndexRV(2, 6, 2, guitarShift)  # [2,0,0.75,Guitar,g6]
        yield from self.waitTime(8)
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,0.5,1.25,Guitar,g5]
        yield from self.waitTime(12)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,0.75,0.75,Piano,p5]
        self.playIndexRV(2, 6, 2, guitarShift)  # [2,0.75,1.25,Guitar,g6]
        yield from self.waitTime(16)
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,1,0.75,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,1,0.75,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,1,0.75,Piano,p6]
        yield from self.waitTime(20)
        self.playIndexRV(3, 7, 2, guitarShift)  # [3,1.25,0.75,Guitar,g7]
        yield from self.waitTime(24)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,1.5,0.25,Piano,p5]
        yield from self.waitTime(28)
        self.playIndexRV(2, 7 - 2, 1, pianoShift)  # [2,1.75,0.25,Piano,p7]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,1.75,0.25,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,1.75,0.25,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,1.75,0.25,Piano,p6]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,1.75,0.25,Guitar,g5]
        yield from self.waitTime(32)
        self.playIndexRV(1, 6 - 2, 1, pianoShift)  # [1,2,2,Piano,p6]
        yield from self.waitTime(36)
        self.playIndexRV(2, 6 - 2, 1, pianoShift)  # [2,2.25,0.25,Piano,p6]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,2.25,0.25,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,2.25,0.25,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,2.25,0.25,Piano,p6]
        self.playIndexRV(1, 7, 2, guitarShift)  # [1,2.25,1.5,Guitar,g7]
        self.playIndexRV(2, 7, 2, guitarShift)  # [2,2.25,1,Guitar,g7]
        yield from self.waitTime(44)
        self.playIndexRV(2, 7 - 2, 1, pianoShift)  # [2,2.75,1.25,Piano,p7]
        self.playIndexRV(3, 7 - 2, 1, pianoShift)  # [3,2.75,1.25,Piano,p7]
        self.playIndexRV(4, 7 - 2, 1, pianoShift)  # [4,2.75,1.25,Piano,p7]
        self.playIndexRV(5, 7 - 2, 1, pianoShift)  # [5,2.75,1.25,Piano,p7]
        self.playIndexRV(3, 7, 2, guitarShift)  # [3,2.75,1.25,Guitar,g7]
        yield from self.waitTime(52)
        self.playIndexRV(3, 8 - 2, 1, pianoShift)  # [3,3.25,0.75,Piano,p8]
        yield from self.waitTime(56)
        self.playIndexRV(2, 6 - 2, 1, pianoShift)  # [2,3.5,0.5,Piano,p6]
        yield from self.waitTime(60)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,3.75,0.25,Piano,p5]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,3.75,0.25,Guitar,g5]

    def play_r_2_4(self):
        # 第四小节：
        self.setIns(1, 0)  # 设置一号通道为钢琴
        self.setIns(2, 24)  # 设置二号通道为吉他
        guitarShift = self.shiftPlayList(40)
        pianoShift = self.shiftPlayList(36)
        self.playIndexRV(1, 7 - 2, 1, pianoShift)  # [1,0,2,Piano,p7]
        self.playIndexRV(3, 7 - 2, 1, pianoShift)  # [3,0,1,Piano,p7]
        self.playIndexRV(4, 7 - 2, 1, pianoShift)  # [4,0,1,Piano,p7]
        self.playIndexRV(5, 7 - 2, 1, pianoShift)  # [5,0,1,Piano,p7]
        self.playIndexRV(1, 6, 2, guitarShift)  # [1,0,1.75,Guitar,g6]
        yield from self.waitTime(8)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,0.5,1,Piano,p5]
        yield from self.waitTime(16)
        self.playIndexRV(3, 7 - 2, 1, pianoShift)  # [3,1,0.75,Piano,p7]
        self.playIndexRV(4, 7 - 2, 1, pianoShift)  # [4,1,0.75,Piano,p7]
        self.playIndexRV(5, 7 - 2, 1, pianoShift)  # [5,1,0.75,Piano,p7]
        self.playIndexRV(2, 6, 2, guitarShift)  # [2,0.75,1.25,Guitar,g6]
        yield from self.waitTime(20)
        self.playIndexRV(3, 7, 2, guitarShift)  # [3,1.25,0.75,Guitar,g7]
        yield from self.waitTime(24)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,1.5,0.25,Piano,p5]
        yield from self.waitTime(28)
        self.playIndexRV(2, 6 - 2, 1, pianoShift)  # [2,1.75,0.25,Piano,p6]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,1.75,0.25,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,1.75,0.25,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,1.75,0.25,Piano,p6]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,1.75,0.25,Guitar,g5]
        yield from self.waitTime(32)
        self.playIndexRV(1, 6 - 2, 1, pianoShift)  # [1,2,2,Piano,p6]
        self.playIndexRV(2, 6 - 2, 1, pianoShift)  # [2,2,0.5,Piano,p6]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,2,0.75,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,2,0.75,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,2,0.75,Piano,p6]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,2,1.75,Guitar,g5]
        yield from self.waitTime(40)
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,2.5,0.25,Piano,p4]
        self.playIndexRV(2, 6, 2, guitarShift)  # [2,2.5,1,Guitar,g6]
        yield from self.waitTime(44)
        self.playIndexRV(2, 6 - 2, 1, pianoShift)  # [2,2.75,1.25,Piano,p6]
        self.playIndexRV(3, 6 - 2, 1, pianoShift)  # [3,2.75,1.25,Piano,p6]
        self.playIndexRV(4, 6 - 2, 1, pianoShift)  # [4,2.75,1.25,Piano,p6]
        self.playIndexRV(5, 6 - 2, 1, pianoShift)  # [5,2.75,1.25,Piano,p6]
        self.playIndexRV(3, 7, 2, guitarShift)  # [3,2.75,1.25,Guitar,g7]
        yield from self.waitTime(52)
        self.playIndexRV(1, 5 - 2, 1, pianoShift)  # [1,3.25,0.75,Piano,p5]
        self.playIndexRV(2, 6, 2, guitarShift)  # [2,3.25,0.75,Guitar,g6]
        yield from self.waitTime(56)
        self.playIndexRV(2, 5 - 2, 1, pianoShift)  # [2,3.5,0.5,Piano]
        yield from self.waitTime(60)
        self.playIndexRV(3, 7 - 2, 1, pianoShift)  # [3,3.75,0.25,Piano,p7]
        self.playIndexRV(1, 5, 2, guitarShift)  # [1,3.75,0.25,Guitar,g5]

    def play_r_s(self):
        # 终止和弦
        self.setIns(1, 0)  # 设置一号通道为钢琴
        guitarShift = self.shiftPlayList(40)
        pianoShift = self.shiftPlayList(36)
        # 副歌钢琴加花：一小节的长音。具体格式如下：
        self.playIndexRV(1, 6 - 2, 1, pianoShift)  # [1,0,4,Piano,p6]
        self.playIndexRV(2, 4 - 2, 1, pianoShift)  # [2,0,4,Piano,p4]
        self.playIndexRV(3, 5 - 2, 1, pianoShift)  # [3,0,4,Piano,p5]
        self.playIndexRV(4, 5 - 2, 1, pianoShift)  # [4,0,4,Piano,p5]
        self.playIndexRV(5, 5 - 2, 1, pianoShift)  # [5,0,4,Piano,p5]

    def play_r(self):
        secId = math.floor(self.fragId / 64) % 8
        if self.endMode:
            yield from self.play_r_s()
            self.endMode = False
        else:
            if secId == 0:
                yield from self.play_r_1_1()
            elif secId == 1:
                yield from self.play_r_1_2()
            elif secId == 2:
                yield from self.play_r_1_3()
            elif secId == 3:
                yield from self.play_r_1_4()
            elif secId == 4:
                yield from self.play_r_2_1()
            elif secId == 5:
                yield from self.play_r_2_2()
            elif secId == 6:
                yield from self.play_r_2_3()
            elif secId == 7:
                yield from self.play_r_2_4()

    def play_m(self):
        secId = math.floor(self.fragId / 256) % 3
        if self.endMode:
            yield from self.play_m_s()
            self.endMode = False
        else:
            if secId == 0:
                yield from self.play_m_1()
            elif secId == 1:
                yield from self.play_m_2()
            elif secId == 2:
                yield from self.play_m_3()

    def startSec(self):
        for i in range(8):
            yield from self.waitTime(0)
            print("seg", self.playListSize())
            self.setIns(1, 0)  # 设置一号通道为钢琴
            pianoShift = self.shiftPlayList(24)
            self.setIns(2, 24)  # 设置二号通道为吉他
            guitarShift = self.shiftPlayList(40)

            print("pianoShift", pianoShift)

            self.playIndexRV(1, 4, 3, -24)
            self.playIndexRV(2, 4, 3, -24)
            self.playIndexRV(3, 4, 3, -24)
            if self.playListSize() == 1:
                # 一个音：
                self.playIndexRV(1, 4, 2, 0)  # [1,0,4,Guitar,p4]
                self.playIndexRV(1, 3, 1, pianoShift)  # [1,0,4,Piano,p4]
            elif self.playListSize() == 2:
                # 两个音：
                # [1,0,4,Guitar,p4],[2,0,4,Guitar,p4]
                # [1,0,4,Piano,p4],[2,0,4,Piano,p4]
                self.playIndexRV(1, 3, 1, pianoShift)
                self.playIndexRV(1, 4, 2, guitarShift)
                yield from self.waitTime(32)
                self.playIndexRV(2, 3, 1, pianoShift)
                self.playIndexRV(2, 4, 2, guitarShift)
            elif self.playListSize() == 3:
                # 三个音：
                # [1,0,4,Guitar,p4],[2,0,4,Guitar,p4,+12],[3,0,4,Guitar,p4]
                # [1,0,4,Piano,p4],[2,2,2,Piano,p3,+12],[3,0,4,Piano,p4]
                self.playIndexRV(1, 3, 1, pianoShift)
                self.playIndexRV(3, 3, 1, pianoShift)
                self.playIndexRV(1, 4, 2, guitarShift)
                self.playIndexRV(2, 4, 2, guitarShift + 12)
                self.playIndexRV(3, 4, 2, guitarShift)
                yield from self.waitTime(32)
                self.playIndexRV(2, 3, 1, pianoShift + 12)
            elif self.playListSize() == 4:
                # 四个音：
                # [1,0,4,Guitar,p4],[2,0,4,Guitar,p4,+12],[3,0,4,Guitar,p4,+12],[4,0,4,Guitar,p4]
                # [1,0,4,Piano,p4],[2,2,2,Piano,p3,+12],[3,2,2,Piano,p3,+12],[4,0,4,Piano,p4]
                self.playIndexRV(1, 4, 2, guitarShift)
                self.playIndexRV(2, 4, 2, guitarShift + 12)
                self.playIndexRV(3, 4, 2, guitarShift + 12)
                self.playIndexRV(4, 4, 2, guitarShift)
                self.playIndexRV(1, 3, 1, pianoShift)
                self.playIndexRV(4, 3, 1, pianoShift)
                yield from self.waitTime(32)
                self.playIndexRV(2, 3, 1, pianoShift + 12)
                self.playIndexRV(3, 3, 1, pianoShift + 12)
            elif self.playListSize() == 5:
                # 五个音：
                # [1,0,4,Guitar,p4],[2,0,4,Guitar,p4,+12],[3,0,4,Guitar,p4,+12],[4,0,4,Guitar,p4],[5,0,4,Guitar,p4]
                # [1,0,4,Piano,p4],[2,2,2,Piano,p3,+12],[3,0,4,Piano,p3,+12],[4,0,4,Piano,p4],[5,0,4,Piano,p4]
                self.playIndexRV(1, 4, 2, guitarShift)
                self.playIndexRV(2, 4, 2, guitarShift + 12)
                self.playIndexRV(4, 4, 2, guitarShift)
                self.playIndexRV(5, 4, 2, guitarShift)
                yield from self.waitTime(32)
                self.playIndexRV(2, 3, 1, pianoShift + 12)
                self.playIndexRV(3, 4, 2, guitarShift + 12)

    def process_callback(self) -> None:
        self.endMode = False

        yield from self.startSec()

        yield from self.waitTime(0)
        self.setIns(3, 95)  # 设置三号通道为弦乐
        self.playIndexRV(1, 4, 3, -24)
        self.playIndexRV(2, 4, 3, -24)
        self.playIndexRV(3, 4, 3, -24)
        seg = self.isRefrain()
        yield from self.play_m_1()
        yield from self.waitTime(0)
        yield from self.play_m_2()
        yield from self.waitTime(0)
        while True:
            self.playIndexRV(1, 4, 3, -24)
            self.playIndexRV(2, 4, 3, -24)
            self.playIndexRV(3, 4, 3, -24)
            seg = self.isRefrain()
            if seg:
                yield from self.play_r()
            else:
                yield from self.play_m()

            yield from self.waitTime(0)


if __name__ == "__main__":
    print("texture:default")
    midi_in = sys.argv[1]  # "test.mid"
    midi_out = sys.argv[2]  # 'out.mid'
    player = texture_default()
    gen = player.process()
    melody_full, chord_full, tonal = sampler.sampleMidi(midi_in)
    player.setTonal(tonal)
    mid_src = mido.MidiFile(midi_in)
    melody_full = numpy.array(melody_full).reshape(-1, 4)
    for i in range(len(chord_full)):
        melody = melody_full[i]
        chord = chord_full[i]
        for note in melody:
            player.pushMelody(note)
        player.setChord(chord)
        for i in range(16):
            next(gen)

    # print(player.ins)
    # print(player.tracks)
    mf = player.linkEvents(mid_src.ticks_per_beat)
    mf.tracks[0] = mid_src.tracks[0]
    mf.save(midi_out)
