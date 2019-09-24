csv_file = open('fff.csv', 'r', encoding='utf-8-sig')
srt_file = open('humburger.srt', 'w', encoding='utf-8')
line = 'start'
while True:
    line = csv_file.readline()
    if (line == ''): break
    elements = line.split(',')
    srt_file.write(elements[0] + '\n' + elements[1] + ' --> ' + elements[2] + '\n' + elements[3] + '\n')
srt_file.close()
csv_file.close()