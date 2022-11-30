import mysql.connector

class serverCom():
    def __init__(self):
        host = 'localhost' 
        database = 'happy_home' 
        username = 'root' 
        password = '' 
        self.cnxn = mysql.connector.connect(host=host, database=database, user=username, password=password)
        self.cursor = self.cnxn.cursor()
    
    def close_connection(self):
        self.cursor.close()
        self.cnxn.close()

    ################################################################
    #---------------------------Inserts----------------------------#
    ################################################################
    def insert_client(self, nombre, tel, mail):
        aux = 'SELECT insert_client(\"'+nombre[0]+'\", \"'+nombre[1]+'\", \"'+nombre[2]+'\", \"'+tel+'\", \"'+mail+'\") LIMIT 0, 1;'
        self.cursor.execute(aux)
        fname = self.cursor.fetchone()[0]
        self.cnxn.commit()
        return fname
    
    def insert_offer(self, idCliente, propiedad, oferta):
        self.cursor.execute('SELECT insert_propiedad('+propiedad['tipo']+', '+idCliente+', \"'+propiedad['direccion']+'\", '+propiedad['superficieT']+', '+propiedad['superficieC']+', \"'+propiedad['amueblada']+'\", '+(propiedad['numRecamaras'])+', '+propiedad['numNiveles']+', '+propiedad['numBaños']+', '+propiedad['mascotas']+', \"'+propiedad['posesion']+'\", '+propiedad['adjunto']+') LIMIT 0, 1;')
        fname = self.cursor.fetchone()[0]
        self.cnxn.commit()
        self.cursor.execute('SELECT insert_oferta('+str(fname)+', \"'+oferta["estado"]+'\", \"'+oferta["moneda"]+'\", '+oferta["precio"]+') LIMIT 0, 1;')
        fname = self.cursor.fetchone()[0]
        self.cnxn.commit()
        return fname

    ################################################################
    #---------------------------Geters-----------------------------#
    ################################################################

    def get_clients(self, id = None):
        query = 'SELECT idCliente, nombre, apellidoP, apellidoM FROM cliente WHERE idCliente = '+id+';' if id != None else'SELECT * FROM cliente;'
        self.cursor.execute(query)
        fname = self.cursor.fetchone() if id != None else self.cursor.fetchall()
        self.cnxn.commit()
        return fname

    def get_tipos(self):
        self.cursor.execute('SELECT * FROM tipospropiedad;')
        fname = self.cursor.fetchall()
        self.cnxn.commit()
        return fname
    
    def get_ofertas(self):
        query = 'SELECT c.nombre, c.apellidoP, c.apellidoM, p.*, t.tipo, o.* FROM cliente as c INNER JOIN propiedad as p ON c.idCliente = p.propietario INNER JOIN tipospropiedad as t ON p.idTipo = t.idTipo INNER JOIN oferta as o ON o.idOferta = p.idPropiedad;'
        self.cursor.execute(query)
        fname = self.cursor.fetchall()
        self.cnxn.commit()
        return fname