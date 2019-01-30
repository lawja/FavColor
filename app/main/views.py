from flask import (abort, jsonify, g, session, render_template, redirect,
                   request, url_for)
from manage import app, client, moment
from . import main
from datetime import datetime
from .mergesort import merge_sort_time as mst

# import self written modules from modules dir
# from ..modules import ...


@main.route('/')
def index():

    db = client.tudev_checkout
    entries = []

    form_data = list(db.form_data.find({}))
    mst(form_data)

    red, blue, yellow, green, purple, orange, other = 0,0,0,0,0,0,0

    for entry in form_data:
        formatted_entry = '''
            <tr>
                <td>{name}</td>
                <td>{age}</td>
                <td>{color}</td>
                <td>{time}</td>
            </tr>
            '''.format(time=moment.create(entry['time']).fromNow(), name=entry['name'],
                       age=entry['age'], color=entry['color'])

        if(entry['color'].lower() == 'red'):
            red+=1
        elif(entry['color'].lower() == 'blue'):
            blue+=1
        elif(entry['color'].lower() == 'yellow'):
            yellow+=1
        elif(entry['color'].lower() == 'green'):
            green+=1
        elif(entry['color'].lower() == 'purple'):
            purple+=1
        elif(entry['color'].lower() == 'orange'):
            orange+=1
        else:
            other+=1

        entries.append(formatted_entry)
    entries = '\n'.join(entries)
    
    return render_template('index.html', entries=entries, red=red, blue=blue,
                           yellow=yellow, green=green, purple=purple,
                           orange=orange, other=other)

@main.route('/submit_form', methods=['POST'])
def submit():
    db = client.tudev_checkout

    data = request.form
    try:
        name = str(data['name'])
        age = str(data['age'])
        color = str(data['color'])

        db.form_data.insert({
                'name': name, 'age': age, 'color': color,
                'time': datetime.utcnow() 
            })

    except KeyError:
        pass

    return redirect(url_for('.index'))
