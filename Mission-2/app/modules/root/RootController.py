from flask import Blueprint, render_template
import pandas as pd 


root_blueprint = Blueprint('root', __name__)

@root_blueprint.route('', methods=['GET'])
def index():
    return render_template('home.html', segment='index')

@root_blueprint.route('usage', methods=['GET'])
def usage():
    return render_template('usage.html', segment='usage')

@root_blueprint.route('about', methods=['GET'])
def about():
    return render_template('about.html', segment='about')

@root_blueprint.route('features', methods=['GET'])
def features():
    return render_template('features.html', segment='features')

@root_blueprint.route('analytics', methods=['GET'])
def analytics():
    li = []
    df = pd.read_csv(r'app\static\log.csv')
    prev = 0
    for row, col in df.iterrows():
        curr = col[1]
        if curr == 1.0:
            li.append(prev)
        prev = float(col[0])

    return render_template('analytics.html', segment='analytics', li=li, labels = ['Day ' + str(i) for i in range(1,len(li)+1)])


