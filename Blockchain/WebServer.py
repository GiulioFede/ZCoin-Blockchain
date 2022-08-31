
import Blockchain
from flask import Flask, jsonify 

'Creo Web App'
app = Flask(__name__)

'Creo una istanza della Blockchain'
blockchain = Blockchain.Blockchain()
