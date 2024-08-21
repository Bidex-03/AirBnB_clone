#!/usr/bin/python3
'''
models/review.py
'''
from models.base_model import BaseModel

class Review(BaseModel):
    '''
    review class
    '''
    place = ""
    user_id = ""
    text = ""
