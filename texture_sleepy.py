import math
import sys
import chordDec
import mido


class sleepy(chordDec.chordDec):
    def process_callback(self) -> None:

        index = 0
        while True:
            print("index", index)
            index += 1
            yield from self.waitTime(0)
            print("seg", self.playListSize())
            self.setIns(1, 0)  # 设置一号通道为钢琴
            pianoShift = self.shiftPlayList(24)
            self.setIns(2, 24)  # 设置二号通道为吉他
            guitarShift = self.shiftPlayList(40)
            self.setIns(3, 95)  # 设置二号通道为吉他

            print("pianoShift", pianoShift)

            self.playIndexRV(1, 4, 3, -12)
            self.playIndexRV(2, 4, 3, -12)
            self.playIndexRV(3, 4, 3, -12)
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


if __name__ == "__main__":
    print("texture:sleepy")
    player = sleepy()
    gen = player.process()
    with open('test.2line.txt') as f:
        line = f.readline()
        while line:
            pair_str = line.strip()
            if pair_str == "":
                break
            pair = pair_str.split("|")
            melody = eval(pair[0])
            chord = eval(pair[1])
            for note in melody:
                player.pushMelody(note)
            player.setChord(chord)
            for i in range(16):
                next(gen)
            line = f.readline()

    # print(player.ins)
    # print(player.tracks)
    mf = player.linkEvents()
    mf.save('out.mid')
