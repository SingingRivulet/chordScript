import music21
import dispatch


class midiExport(dispatch.dispatcher):
    def __init__(self, numTrack: int = 4) -> None:
        super().__init__()

    # 演奏用的函数
    def playNote(self,
                 tone: int,  # 音高
                 vel: int,  # 音量，为0说明停止演奏
                 track: int  # 轨道
                 ) -> None:
        pass

    # 设置通道的乐器
    def setIns(self,
               track: int,  # 通道
               ins: int  # 乐器id
               ) -> None:
        pass
