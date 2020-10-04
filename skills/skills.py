from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Skills(Resource): 
    def get(self):
        return {
           "shifting": { "hand" : "left" },
           "finger dropping and lifting" : {"hand" : "left"},
           "vibrato" : {"hand" : "left"},
           "left hand pizzicato" : {"hand" : "left"},
           "bow balance" : {"hand": "right"}, 
           "pressure, speed, sounding point" : {"hand": "right"}, 
           "box changes" : {"hand": "right"}, 
           "detache" : {"hand": "right"}, 
           "legato" : {"hand": "right"}, 
           "collee" : {"hand": "right"}, 
           "martele" : {"hand": "right"}, 
           "staccato" : {"hand": "right"},           
           "sautille" : {"hand": "right"},           
           "richochet" : {"hand": "right"},           
           "three note chords" : {"hand": "right"},           
           "four note chords" : {"hand": "right"},
           "fast scales" : {"hand": "left"}
        }

api.add_resource(Skills, "/")

if __name__ == '__main__':
    app.run(host='0.0.0.0')