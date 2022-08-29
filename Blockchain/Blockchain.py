

import datetime
import hashlib
import json
from flask import Flask, jsonify 


'Questa classe rappresenterà la blockchain'

class Blockchain:
    
    '_________________________________________________________________________________________________'
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
        self.create_block(nonce = 1, previous_hash = '0')
    
    
    '_________________________________________________________________________________________________'
    '''
     Funzione per creare un blocco. Riceve due argomenti:
        1) nonce: ogni blocco ha un suo nonce
        2) prev_hash: l'hash del precedente blocco
    '''
    def create_block(self, nonce, prev_hash):
        
        'Campi del blocco'
        block = {
                 'index', len(self.chain)+1, 
                 'timestamp', str(datetime.datetime.now()),
                 'nonce', proof,
                 'prev_hash', prev_hash
                }
        
        'Aggiungo il blocco alla Blockchain'
        self.chain.append(block)
        
        'Ritorno il blocco'
        return block
    
    
        '_________________________________________________________________________________________________'
    '''
     Funzione per ritornare l'ultimo blocco della Blockchain'
    '''
    def get_last_block(self):
        return self.chain[-1]
        
    
        '_________________________________________________________________________________________________'
    '''
        Funzione per il Mining.
        Qui stabilisco una regola banale e diversa da quella usata in Bitcoin: il blocco viene minato se e solo
        se l'hash del nonce al quadrato meno quella del nonce precedente al quadrato è un hash con 4 zeri iniziali
        allora il blocco è minato. 
        NB: è troppo semplice, ma serve solo a scopo di debugging'
    '''
    def mine_block(self, previous_nonce):
        current_nonce = 1
        check = False ' Quando è a True, è stato trovato un nonce corretto'
        
        while check is False:
            '''
                Genero l'hash che si ottiene elevando al quadrato il corrente nonce e sottraendo
                il quadrato del vecchio nonce. 
                Utilizzo encode() per inserire la 'b prima della stringa dato che la funzione sha256 
                vuole le stringhe in questo formato
            '''
            hash = hashlib.sha256( str(current_nonce^2 - previous_nonce^2).encode() ).hexdigest()
            
            ''' Se l'hash generato ha i 4 zeri iniziali, il miner ha vinto '''
            if hash[:4] == '0000':
                check = True
            else:
                'provo con un altro nonce'
                current_nonce += 1
            
        return current_nonce
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        