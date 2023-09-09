import sys
import json 
import clipboard



SAVED_DATA= "clipboard.json"

def save_items(filepath , data):
    with open(filepath, "w") as f:
        json.dump(data,f)

def load_items(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                data = {}  # If data is not a dictionary, initialize an empty one
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
if len(sys.argv) == 2 :
    command = sys.argv[1]
    data = load_items(SAVED_DATA)

    if command == 'save':
        data = load_items(SAVED_DATA)
        key = input('Enter a key: ')
        data[key] = clipboard.paste()
        save_items(SAVED_DATA,data)
        print("Data saved")

    elif command == "load":
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipbboard")
        else: 
            print("Key does not exist ")
    elif command == "list":
        print(data)

    elif command == "del":
        delkey = input("What is the name of the key you want to delete?: ")
        del data[delkey]
        print(data)

    else:
        print("unkown command") 
else:
    print("please type in a command")


