import re

file_name = 'upTitle.srt'
truncate_length = 6

srt_file = open(file_name, 'r', encoding='utf-8')
output = ''
for line in srt_file:
    if re.search('-->', line):
        time_stamps = line.split(' --> ')
        first_time = time_stamps[0]
        second_time = time_stamps[1]
        first_time_detail = first_time.split(':')
        second_time_detail = second_time.split(':')
        first_time = int(first_time_detail[1]) * 60 + int(first_time_detail[2].split(',')[0])
        second_time = int(second_time_detail[1]) * 60 + int(second_time_detail[2].split(',')[0])
        if (second_time - first_time > truncate_length):
            line = re.sub(r'\d+:\d+,000$', '{:0>2d}'.format(int((first_time + truncate_length) / 60)) + ':' + '{:0>2d}'.format((first_time + truncate_length) % 60) + ',000', line)
    output += line
srt_file.close()
srt_file = open(file_name, 'w', encoding='utf-8')
srt_file.write(output)
srt_file.close()
