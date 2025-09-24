import os
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder='.', static_url_path='')

# In-memory database for simplicity
scores = {}

# Route to serve the front-end (index.html)
@app.route('/')
def serve_index():
    return app.send_static_file('index.html')

# Existing API routes
@app.route('/scores', methods=['GET'])
def get_scores():
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return jsonify(sorted_scores)

@app.route('/scores', methods=['POST'])
def add_score():
    data = request.json
    player = data.get('player')
    score = data.get('score')
    if not player or not score:
        return jsonify({'error': 'Player and score are required.'}), 400
    scores[player] = score
    return jsonify({'message': f'Score for {player} added successfully.'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)