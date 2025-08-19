from flask import Flask, render_template, request, jsonify
from bot_engine import launch_bot
from log_store import get_logs, save_logs_to_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    video_link = request.form['video_link']
    screen_count = int(request.form['screen_count'])
    like_option = request.form['like_option']

    launch_bot(video_link, screen_count, like_option)

    return f"<h2>Started watching {video_link} on {screen_count} screen(s) with likes {like_option.upper()}!</h2>"

@app.route('/status')
def status():
    return jsonify(get_logs())

@app.route('/save-logs')
def save_logs():
    save_logs_to_file()
    return "✅ Logs saved successfully!"

if __name__ == '__main__':
    app.run(debug=True)