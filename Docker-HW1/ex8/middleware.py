from flask import Flask, send_file, render_template_string
import os

app = Flask(__name__)

LOG_PATH = "/log/app.log"

HTML_PAGE = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Loguri Live</title>
    <meta http-equiv="refresh" content="1">
    <style>
        body { font-family: monospace; white-space: pre; background: #f0f0f0; padding: 20px; }
    </style>
</head>
<body>
<h2>Loguri live din container:</h2>
<pre>{{ logs }}</pre>
</body>
</html>
"""

@app.route('/')
def home():
    logs = ""
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, 'r') as f:
            logs = f.read()
    return render_template_string(HTML_PAGE, logs=logs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
