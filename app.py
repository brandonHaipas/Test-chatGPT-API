# -*- coding:utf-8 -*-
import json
import openai
from openai import OpenAI
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

openai.api_key  = os.getenv('OPENAI_API_KEY')
client = OpenAI()
app = Flask(__name__)


DEBUG = True