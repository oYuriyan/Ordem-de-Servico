from flask import Flask
from models import db, OrdemServico

# --- Configuração da Aplicação Flask ---
app = Flask(__name__)

# Configura o caminho para o nosso banco de dados SQLite.
# O arquivo 'ordens.db' será criado na raiz do projeto.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ordens.db'
# Desativa uma funcionalidade de rastreamento de modificações do SQLAlchemy para economizar recursos.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Vincula a instância do nosso banco de dados (db) com a aplicação Flask.
db.init_app(app)

# --- Rotas da Aplicação ---
@app.route('/')
def index():
    """
    Rota principal que será responsável por exibir o formulário da Ordem de Serviço.
    Por enquanto, retorna uma mensagem simples.
    """
    return "Servidor da Aplicação de Ordem de Serviço está no ar!"

# --- Ponto de Entrada da Aplicação ---
if __name__ == '__main__':
    # Bloco para criar o banco de dados e a tabela se eles não existirem.
    with app.app_context():
        db.create_all()
    
    # Inicia o servidor de desenvolvimento do Flask.
    # debug=True faz com que o servidor reinicie automaticamente após mudanças no código.
    app.run(debug=True)
