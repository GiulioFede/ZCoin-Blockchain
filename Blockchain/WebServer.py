
import Blockchain
from flask import Flask, jsonify 

'Creo Web App'
app = Flask(__name__)

'Creo una istanza della Blockchain'
blockchain = Blockchain.Blockchain()

'''
    Creo un trigger. Quando contatto un certo url (es. da Postman) il web server farà partire la funzione
    alla quale tale url è collegata.
    Quando avvio il server di default si collegherà al loop ip address 127.0.0.1:5000, pertanto ogni url che definisco,
    dovrà solo contenere il path
'''

'Es. quando da Postman digito http://127.0.0.1:5000/mine_block come richiesta GET, il web server avvierà tale funzione'
@app.route('/mine_block', methods = ['GET']) 
def mine_new_block():
    'Adesso parte il mining. Si prende il nonce dell ultimo blocco e si cerca un nonce tale che nonce^2-prev_nonce^2....'
    prev_block = blockchain.get_last_block()
    nonce_prev_block = prev_block['nonce']
    
    'Cerco il nonce che riesca a minare'
    winner_nonce = blockchain.mine_block(nonce_prev_block)
    
    'Ci sono riuscito. Creo il nuovo blocco e lo aggiungo alla catena corrente'
    'Ho bisogno dell hash del blocco precedente per aggiungerlo al campo prev_hash'
    prev_hash = blockchain.hash_block(prev_block)
    block = blockchain.create_block(winner_nonce, prev_hash)
    
    'Ritorno come risposta i campi stessi del nuovo blocco aggiunto'
    response = {
                'message': 'Block mined!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'winner_nonce': block['nonce'],
                'prev_hash': block['prev_hash'],
                'hash': blockchain.hash_block(block)
                }
    return jsonify(response), 200
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
