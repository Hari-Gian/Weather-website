from flask import Flask, request, jsonify
from weather import Weather

app = Flask(__name__)
