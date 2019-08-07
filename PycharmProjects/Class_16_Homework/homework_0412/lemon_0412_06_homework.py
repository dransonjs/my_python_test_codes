# 将你喜欢的一首歌（音乐文件拓展名为mp3，比如刘德华忘情水.mp3），通过文件读写的方法将其复制，并修改文件名

song_1 = open('Akon-Beautiful.flac', mode='rb')
song_2 = open('Akon-Beautiful-copy.flac', mode='wb')

while 1:
    text = song_1.readline()
    if not text:
        break
    song_2.write(text)

song_1.close()
song_2.close()
