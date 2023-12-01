import pytest
from flask import Flask, request
from main import app
from routes.main import db, q
import json

# Напишем тест для проверки отправки POST-запроса на /get_form
def test_post_request():
    db.insert({"name": "Form template name copy","field_name_1_copy": "email","field_name_2_copy": "phone"})
    test_client = app.test_client()
    response = test_client.post('/get_form?field_name_2_copy=79194660001&field_name_1_copy=ressiwage@ya.ru')
    db.remove(q.fragment({"field_name_1_copy": "email","field_name_2_copy": "phone"}))    
    assert response.status_code == 200
    assert len(response.json)>0
    
def test_post_request():
    test_client = app.test_client()
    response = test_client.post('/get_form?AAAAAAAAAAAAAAAAAAAA=79194660001&AAAAAAAAAAAAA=ressiwage@ya.ru')
    assert response.status_code == 200
    assert json.dumps(response.json, sort_keys=True) == json.dumps({'AAAAAAAAAAAAA': 'email', 'AAAAAAAAAAAAAAAAAAAA': 'phone'}, sort_keys=True)