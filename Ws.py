import psycopg2
from flask_cors import CORS
from flask import Flask, render_template, jsonify, request,session

conn = psycopg2.connect("dbname=db43updaq6p2cl user=vyhcdlbkyrbwsw password=6c6fb5267b710dd9d6fe218d6abd72aa7c7704dd809579ffddac152aa2aa6261 host=ec2-54-235-86-226.compute-1.amazonaws.com " )
cur = conn.cursor()
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome  = request.json['nomeUsuario']
        senha  = request.json['senha']
        cur.execute("SELECT COUNT(1) FROM usuario WHERE nome = '%s';"% nome) # CHECKS IF USERNAME EXSIST
        if cur.fetchone()[0]:
            cur.execute("SELECT senha FROM usuario WHERE nome = '%s';"% nome) # FETCH THE HASHED PASSWORD
            for row in cur.fetchall():
                if senha == row[0]:
                    return jsonify({'resultado':'logado'})
                else:
                    error = "Senha invalida"
        else:
            error = "Usuario invalido"
    return jsonify({'resultado':error})



@app.route('/contacts')
def contacts():
    try:
        nomeUsuario ='NADSON'
        cur.execute("SELECT senha FROM usuario WHERE nome ='%s'"% nomeUsuario)
        rows = cur.fetchall()
       
        my_list = []
        for row in rows:
            my_list.append(row[0])
            print(my_list)

        return jsonify(results=my_list)
    except Exception as e:
        print (e)
        return []

if __name__ == '__main__':
    app.run(debug=True)
