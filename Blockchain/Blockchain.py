

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
        Qui stabilisco una regola banale e diversa da quella usata in Bitcoin (per evitarmi grossi sprechi di energia): il 
        blocco viene minato se e solo se l'hash del nonce al quadrato meno quella del nonce precedente al quadrato è un hash 
        con 4 zeri iniziali allora il blocco è minato. 
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
        
    
        '_________________________________________________________________________________________________'
    '''
        Funzione per ritornare l'hash di un Blocco
        Si ordinano i campi del Blocco in ordine lessicografico e si converte il dizionario in stringa.
            Esempio:
                dizionario = {"name": "Giulio", "Age": 26}  --> json.dumps(dizionario) --> {"name": "Giulio", "Age": 26} come stringa
        Si passa questa stringa (ricordandosi di codificarla opportunamente con encode() ) alla funzione hash per ottenere l'hash del blocco
    '''
    def hash_block(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    
    
        '_________________________________________________________________________________________________'
    '''
        Funzione per la Validazione di un solo blocco.
        Questa funzione verrà chiamata da ogni nodo per validare un blocco ricevut o una intera catena. 
        Un blocco è valido se:
            1) Il suo prev_hash corrisponde all'hash del blocco nella catena a lui precedente'
            2) L'hash del suo contenuto ha 4 zeri iniziali
    '''
    def is_block_valid(self, block, hash_prev_block, nonce_prev_block):    
        
        'Se il suo campo prev_hash ha valore diverso dall hash del precedente blocco, il blocco è non valido '
        if block['prev_hash'] != hash_prev_block:
            return False
        
        'Calcolo hash del blocco'
        'Ne prendo il nonce'
        nonce = block['nonce']
        'Eseguo operazione di hashing come definita per questa Blockchain '
        hash_block = hashlib.sha256( str(nonce**2 - nonce_prev_block**2).encode() ).hexdigest()
        'Se non ha 4 zeri iniziali, il blocco è non valido'
        if hash_block[:4] != '0000':
            return False
        
        'Se siamo arrivati fino a qui, il blocco risulta valido'
        return True
        
        
        
        '_________________________________________________________________________________________________'
    '''
        Funzione per la Validazione dell'intera catena.
        Questa funzione chiama ricorsivamente is_block_valid su ogni blocco della catena per stabilirne la sua validità
    '''
    def is_chain_valid(self, chain):     
        'Prendo il blocco iniziale (lo chiamo prev perchè poi lo sovrascriverò nel loop)'
        prev_block = chain[0]
        'Inizializzo indice che punterà sempre al blocco corrente (quello dopo il prev_block)'
        current_block_index = 1
        
        'Faccio un loop su ogni blocco per stabilirne la validità'
        while current_block_index < len(chain):
            'Prendo il blocco corrente'
            current_block = chain[current_block_index]
            
            'Controllo se è valido'
            check_block_validity = is_block_valid(self, current_block, hash_block(prev_block), prev_block['nonce'])
            'Se è invalido, la catena è non valida'
            if check_block_validity is False:
                return False
            
            'Passo al blocco successivo'
            prev_block = current_block
            current_block_index += 1
        
        'Se sono arrivato fin qui, la catena è interamente valida'
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        