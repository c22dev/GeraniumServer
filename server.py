from flask import Flask, request
import os
import uuid
import random
import string

app = Flask(__name__)

log_directory = 'log'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

def generate_random_string(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['POST'])
def log_server():
    if request.method == 'POST':
        data = request.get_data(as_text=True)
        
        uuid_prefix = "UUID "
        uuid_start = data.find(uuid_prefix) + len(uuid_prefix)
        uuid_end = data.find("\n", uuid_start)
        usr_uuid = data[uuid_start:uuid_end] if uuid_start > -1 else 'unknown-uuid'

        random_filename = generate_random_string()

        file_path = os.path.join(log_directory, f"{usr_uuid}_{random_filename}.log")

        with open(file_path, 'w') as log_file:
            log_file.write(data)

        return 'SUCCESS'
    else:
        return 'Invalid request..? If you know what you are doing, contact me at c22dev on Discord.'

if __name__ == '__main__':
    print("Geranium Log Server v0.3")
    print("made by c22dev")
    print("")
    print("This was made for Geranium. Geranium itself is under GPLv3 license. The license also applies to the log server.")
    app.run(port=3000)
