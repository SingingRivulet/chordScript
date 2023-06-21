# 和弦织体转换器

使用方法：  
先将旋律放在 midi 的 0 号轨，和弦放在 1 号轨，然后

```
python3 texture_sleepy.py 输入midi文件 输出midi文件
```

或者

```
python3 texture_default.py 输入midi文件 输出midi文件
```

例如

```
python3 texture_sleepy.py test.mid out.mid
```

如果轨道不是 0 号和 1 号轨，可以手动指定轨道，格式为

```
python3 texture_sleepy.py 输入midi文件 输出midi文件 旋律轨道 和弦轨道
```

由于 music21 机制，会自动忽略空轨道，可能导致采样的旋律轨编号和实际旋律轨不一致，最终导致输出 midi 中旋律轨为空  
可以通过手动指定原来的旋律轨解决:

```
python3 texture_sleepy.py 输入midi文件 输出midi文件 旋律轨道 和弦轨道 实际旋律轨道
```
