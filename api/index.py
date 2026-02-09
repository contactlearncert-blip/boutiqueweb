# api/index.py
from flask import Flask, request, jsonify, render_template
from urllib.parse import quote
import json
import os
import sys

# Ajouter le répertoire parent au chemin Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importer l'application Flask depuis app.py
from app import app as flask_app

# Exporter la fonction handler pour Vercel
def handler(request):
    return flask_app(request.environ, lambda *args: None)