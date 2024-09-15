from flask import Flask, request
import os
import re
import time

app = Flask(__name__)
log_directory = 'log'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

def get_current_timestamp():
    return int(time.time())

def extract_uuid(data):
    uuid_pattern = r'UUID\s+([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'
    match = re.search(uuid_pattern, data)
    return match.group(1) if match else 'unknown-uuid'

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

@app.route('/', methods=['POST'])
def log_server():
    if request.method == 'POST':
        data = request.get_data(as_text=True)

        uuid = extract_uuid(data)
        timestamp = get_current_timestamp()

        folder_path = os.path.join(log_directory, uuid)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_name = f"{timestamp}.log"
        file_path = os.path.join(folder_path, file_name)

        while get_folder_size(folder_path) > 8 * 1024 * 1024:  # 8 MB
            oldest_file = min(os.listdir(folder_path), key=lambda f: os.path.getmtime(os.path.join(folder_path, f)))
            os.remove(os.path.join(folder_path, oldest_file))

        with open(file_path, 'w') as log_file:
            log_file.write(data.replace('\\n', '\n')[:500 * 1024])  # 500 KB limit

        return 'SUCCESS'
    else:
        return 'Invalid request. If you know what you are doing, contact me at c22dev on Discord.'

if __name__ == '__main__':
    print("Geranium Log Server v1.0")
    print("made by c22dev\n")
    print("This was made for Geranium. Geranium itself is under GPLv3 license. The license also applies to the log server.")
    app.run(port=3000)
