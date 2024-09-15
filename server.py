from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def log_server():
    if request.method == 'POST':
        data = request.get_data(as_text=True)
        print(data)  # logging could be done another way.
        return 'SUCCESS'
    else:
        return 'Geranium Log Server v0.3. Invalid request.'

if __name__ == '__main__':
    print("Geranium Log Server v0.3")
    print("made by c22dev")
    print("")
    print("This was made for Geranium. Geranium itself is under GPLv3 license. The license also applies to the log server.")
    app.run(port=3000)
