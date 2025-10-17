# models.py

import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Inicializa a extensão SQLAlchemy para ser usada com nosso app Flask
db = SQLAlchemy()

class OrdemServico(db.Model):
    """
    Representa a tabela 'ordem_servico' no banco de dados.
    Cada atributo da classe corresponde a uma coluna na tabela.
    """
    __tablename__ = 'ordem_servico'
    
    # Coluna para um ID numérico simples, que se auto-incrementa. Chave primária.
    id = db.Column(db.Integer, primary_key=True)
    
    # Coluna para um ID universalmente único (UUID). Garante que cada OS tenha um identificador único globalmente.
    unique_id = db.Column(db.String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    
    # --- Dados do Cliente e Serviço ---
    cliente_nome = db.Column(db.String(200), nullable=False)
    descricao_servico = db.Column(db.Text, nullable=False)
    
    # --- Timestamps Automáticos ---
    # Registra a data e hora exatas de quando a OS foi criada.
    data_criacao = db.Column(db.DateTime, default=datetime.now, nullable=False)
    # Registra a data e hora de finalização. Pode ser nulo até a aprovação.
    data_finalizacao = db.Column(db.DateTime, nullable=True)
    
    # --- Dados de Geolocalização ---
    latitude = db.Column(db.String(50), nullable=True)
    longitude = db.Column(db.String(50), nullable=True)
    
    # --- Assinaturas (armazenadas como texto longo - Base64) ---
    assinatura_tecnico_b64 = db.Column(db.Text, nullable=True)
    assinatura_gerente_b64 = db.Column(db.Text, nullable=True)
    
    # --- Anexos ---
    # Armazenará um identificador ou caminho para os arquivos associados a esta OS.
    # A lógica de upload de arquivos será gerenciada no app.py.
    caminho_anexos = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        """Representação em texto do objeto, útil para debug."""
        return f'<OrdemServico {self.unique_id}>'

