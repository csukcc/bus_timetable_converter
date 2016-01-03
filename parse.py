#!/usr/bin/env python3

import re
import csv

def convert_timetable(read_file_name, write_file_name):
    read_file = open(read_file_name, mode='rt', encoding='utf-8')
    sections = breakdown_file(read_file)
    json_data = "["
    for section in sections:
        print(section)
        timetable = []
        for line in section:
            timetable.append(line.strip().split(','))
        temp_json = parse_data(timetable)
        # print(temp_json)
        if not len(json_data) == 0:
            json_data += temp_json
    json_data += "]"
    write_json(write_file_name, json_data)
    read_file.close()
    print("Conversion Completed!")


def breakdown_file(file, ):
    token = '[BREAK]'
    chunks = []
    current_chunk = []
    for line in file:
        if line.startswith(token) and current_chunk:
           # if line starts with token and the current chunk is not empty
           chunks.append(current_chunk[:]) #  add not empty chunk to chunks
           current_chunk = [] #  make current chunk blank
        else:
            # just append a line to the current chunk on each iteration
            current_chunk.append(line)
    chunks.append(current_chunk)  #  append the last chunk outside the loop
    return chunks


def parse_data(timetable):
    row = len(timetable)
    col = len(timetable[0])
    add_comma = False
    data = ""

    for j in range(1,col):
        temp_data = '{'
        for i in range(row):
            if len(timetable[i][j]) == 0:
                add_comma = False
                # print('Empty, skip...')
            else:
                add_comma = True
                temp_data += parse_stop_and_time(timetable[i][0], timetable[i][j])

            if add_comma == True and (i+1) < row:
                temp_data += ','

        if add_comma == True and (j+1) < col:
            temp_data += '},'
        else:
            temp_data += '}'
        # if the result is an empty object, then do not include it
        if not temp_data == '{}':
            data += temp_data
    # If the last character is , then remove it
    if data[-1] == ',':
        data = data[:-1]

    return data


def parse_stop_and_time(stop, time):
    if not time.isdigit():
        stop = 'Service'

    return '"'+fix_stop(stop)+'":'+'"'+fix_time(time)+'"'


def fix_stop(stop):
    stop = re.sub(r'\s{2}', ' ', stop)
    if stop[-1] == " ":
        stop = stop[:-1]
    return stop


def fix_time(time):
    time = re.sub(r'\s*', '', time)
    if len(time) == 3 and time.isdigit():
        return "0"+time
    else:
        return time


def write_json(write_file_name, json):
    write_file = open(write_file_name, mode='wt', encoding='utf-8')
    write_file.write(json)


if __name__ == '__main__':
    convert_timetable('test.csv', 'test.json')
