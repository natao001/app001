import psycopg2
from flask import Flask, render_template, jsonify

conn = psycopg2.connect("dbname=db43updaq6p2cl user=vyhcdlbkyrbwsw password=6c6fb5267b710dd9d6fe218d6abd72aa7c7704dd809579ffddac152aa2aa6261 host=ec2-54-235-86-226.compute-1.amazonaws.com " )
cur = conn.cursor()
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if 'nome' in session:
        return 'logado'
    if request.method == 'POST':
        username_form  = request.form['nome']
        password_form  = request.form['senha']
        cur.execute("SELECT COUNT(1) FROM users WHERE nome = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
        if cur.fetchone()[0]:
            cur.execute("SELECT senha FROM users WHERE name = %s;", [username_form]) # FETCH THE HASHED PASSWORD
            for row in cur.fetchall():
                if md5(password_form).hexdigest() == row[0]:
                    session['nome'] = request.form['nome']
                    return 'logado'
                else:
                    error = "Senha invalida"
        else:
            error = "Usuario invalido"
    return 'erro ao logar'



@app.route('/contacts')
def contacts():
    try:
        cur.execute("""SELECT senha from usuario""")
        rows = cur.fetchall()
        response = ''
        my_list = []
        for row in rows:
            my_list.append(row[0])

        return jsonify(results=my_list)
    except Exception as e:
        print (e)
        return []

if __name__ == '__main__':
    app.run(debug=True)
