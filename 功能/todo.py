import os
import json


def check(directory, s):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return False
    files = os.listdir(directory)
    for file in files:
        if file == f'{s}.json':
            return True
    return False


def savejson(data, file_path):
    try:
        with open(file_path, 'w') as f:
            json.dump(json.dumps(data), f, indent=4)
        print(f"JSON data saved to '{file_path}' successfully.")
    except IOError:
        print(f"Error: Unable to write to file '{file_path}'.")


path = '功能/todo_data/'


def readjson(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from file '{file_path}'.")
        return None


def addtodo(s, content):
    if check(path, s):
        datalist = list(json.loads(readjson(path + s + '.json')))
        datalist.append(content)
        savejson(datalist, path + s + '.json')
    else:
        datalist = [content]
        savejson(datalist, path + s + '.json')


def outtodo(s):
    if check(path, s):
        datalist = list(json.loads(readjson(path + s + '.json')))
        if len(datalist) == 0:
            datalist = ['没有待办...']
        return datalist
    else:
        return ['没有待办...']


def deltodo(s):
    datalist = []
    savejson(datalist, path + s + '.json')
