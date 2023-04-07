
from joblib import load
from flask import Blueprint
import sys


sys.path.append("../../../..")
sys.path.append("../../")


home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def home():
    return "hi"