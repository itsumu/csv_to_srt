import re

file_name = 'upTitle2.srt'

srt_file = open(file_name, 'r', encoding='utf-8')
output = ''
for line in srt_file:
    if re.search('-->', line):
       line = line.replace('\n',' X1:0\n')
    output += line
srt_file.close()
srt_file = open(file_name, 'w', encoding='utf-8')
srt_file.write(output)
srt_file.close()
