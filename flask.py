from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

@app.route('/start_bot', methods=['POST'])
def start_bot():
    data = request.json
    meeting_link = data['meetingLink']
    email = data['email']
    password = data['password']
    
    bot_thread = threading.Thread(target=run_bot, args=(meeting_link, email, password))
    bot_thread.start()
    
    return jsonify({"status": "Bot started"})

def run_bot(meeting_link, email, password):
    # Bot logic here (Selenium automation, audio handling, etc.)
    pass

if __name__ == '__main__':
    app.run(debug=True)
