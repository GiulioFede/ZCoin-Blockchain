

import datetime
import hashlib
import json
from flask import Flask, jsonify 


'Questa classe rappresenterà la blockchain'

class Blockchain:
    
    '''Alla creazione della nostra Blockchain dovremmo inizializzare un pò di cose. La 
       funzione __init__ è la prima a partire ogni volta che creiamo una instanza Blockchain
    '''
    def __init__ (self): 'con self ci riferiamo alla instanza corrente
        
        ' La chain è una lista che contiene tutti i blocchi della Blockchain '
        self.chain = []

        '''
            Quando la funzione __init__ viene chiamata, chiamiamo la funzione per creare un blocco.
            Gli passiamo come argomenti 1 e '0' in quanto sono quelli per il blocco Genesis,
            ossia il primo blocco della Blockchain (dato che ne stiamo instanziando una)
        '''
        self.create_block(proof = 1, previous_hash = '0')
    
    
    '''
     Funzione per creare un blocco. Riceve due argomenti:
        1) proof: ogni blocco ha una sua prova
        2) prev_hash: l'hash del precedente blocco
    '''
            
            
        