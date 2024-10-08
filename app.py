import os
from flask import Flask, render_template, request, jsonify
from werkzeug.urls import url_quote
import random
import redis
import json

app = Flask(__name__)
app.config['SERVER_NAME'] = 'rizzcalculator.com'
redis_client = redis.Redis(host=os.environ.get('REDIS_HOST', 'localhost'), port=6379, db=0)

# Load the configuration file
with open('rizz_config.json', 'r') as config_file:
    config = json.load(config_file)

def get_rizz_info(rizz_level):
    for level_info in config['rizz_levels']:
        if level_info['range'][0] <= rizz_level <= level_info['range'][1]:
            return {
                'label': level_info['label'],
                'description': level_info['description']
            }
    return {
        'label': "Unknown Rizz Level",
        'description': "Score out of range"
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        
        # Check if the name exists in Redis
        stored_rizz = redis_client.get(name)
        if stored_rizz:
            rizz_level = int(stored_rizz)
            from_cache = True
        else:
            # Generate a new rizz level and store it
            rizz_level = random.randint(0, 100)
            redis_client.set(name, rizz_level)
            from_cache = False
        
        rizz_info = get_rizz_info(rizz_level)
        
        return jsonify({
            'rizz_level': rizz_level,
            'rizz_label': rizz_info['label'],
            'rizz_description': rizz_info['description'],
            'from_cache': from_cache
        })
    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')