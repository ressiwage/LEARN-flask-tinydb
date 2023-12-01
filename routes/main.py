from routes import bp
from tinydb import TinyDB, Query
import os, random, string, re
from flask import request, jsonify

db = TinyDB(os.path.dirname(__file__)+'\\..\\db\\main.json')
q = Query()

random_word = lambda startlen, endlen : ''.join(random.choice(string.ascii_letters) for i in range(random.randint(startlen,endlen))).lower()

#возможное исправление: сделать метод гетом, т.к. используются url параметры, но не используется тело
#возможное исправление: сохранение даты в iso файле, т.к. это значительно облегчит дело если подключатся другие фреймворки и языки

def check_string_format(input_string):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, input_string):
        return 'email'
    phone_pattern = r'^7\d{10}$'
    if re.match(phone_pattern, input_string):
        return 'phone'
    date_pattern = r'^(?:\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2})$'
    if re.match(date_pattern, input_string):
        return 'date'
    return 'text'

def process_args(args):
    res = dict()
    for k in args:
        res[k] = check_string_format(args[k])
    return res

@bp.route('/get_form', methods=['POST'])
def get_form():
    args = process_args(dict(request.args))
    result = db.search(q.fragment(args))
    if len(result)>0:
        return jsonify(result)
    return jsonify(args)

@bp.route('/populate', methods=['GET'])
def populate():
    data = dict()
    POSSIBLE_TYPES = ['email', 'phone', 'text', 'date']
    fields_num = random.randint(1, 5)
    for i in range(fields_num):
        data[random_word(3,8)] = random.choice(POSSIBLE_TYPES)
    data['name'] = random_word(3,8)
    db.insert(data)
    return {'code':200}

@bp.route('/', methods=['GET'])
def hw():
    return """<h1>hello world</h1>"""