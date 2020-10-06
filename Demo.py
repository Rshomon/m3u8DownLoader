import m3u8
url = 'https://meinv.jingyu-zuida.com/20200212/12629_bf2d8745/1000k/hls/'
m3u8_obj = m3u8.load(url + 'index.m3u8')
f = open('shortname.txt', 'w')
g = open('longname.txt', 'w')
for i in m3u8_obj.segments:
    surl = str(i).split('\n')[-1]
    lurl = url + surl
    f.write('file \'' + surl + '\'\n')
    g.write(lurl + '\n')
f.close()
g.close()