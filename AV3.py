from datetime import date
from novo import db

class Coren(db.Model):
    # colocação do nome da tabela para o banco de dado
    __tablename__ = "coren"

    id = db.Column(db.Integer, primary_key=True)
    uf = db.Column(db.String(2)) 
    num_inscricao = db.Column(db.Text)
    categoria = db.Column(db.String(4))

    # criação do método para a junção do coren
    def format_coren(self):
        coren = self.uf+self.num_inscricao+self.categoria
        return coren

    # representação dos dados por meio de string
    def __repr__(self):
        return f"<COREN {self.format_coren()}>"

    # método construtor que torna desnecessário especificar atributos na instância
    def __init__(self, uf:str, num_inscricao:str, categoria:str):
        self.uf = uf
        self.num_inscricao = num_inscricao
        self.categoria = categoria

    # método para retornar os dados em formato JSON
    def json(self):
        return {
            "id": self.id,
            "uf": self.uf,
            "num_inscricao": self.num_inscricao,
            "categoria": self.categoria
        }

class Enfermeiro(db.Model):
    # colocação do nome da tabela para o banco de dado
    __tablename__ = "enfermeiros"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    data_nascimento = db.Column(db.DateTime)
    CPF = db.Column(db.Text, nullable=False, unique=True)
    telefone = db.Column(db.Text)
    email = db.Column(db.Text)
    sexo = db.Column(db.Text)
    senha = db.Column(db.Text)
    
    # relacionando as classes Enfermeiro e Coren com relacionamento de Composição
    id_coren = db.Column(db.Integer, db.ForeignKey(Coren.id), nullable=False)
    coren = db.relationship("Coren")

    # representação dos dados por meio de string
    def __repr__(self):
        return f"<Enfermeiro {self.nome}"

    # método construtor que torna desnecessário especificar atributos na instância
    def __init__(self, nome:str, data_nascimento:date,
                CPF:str, telefone:str, email:str, sexo:str, senha:str, coren:Coren):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.CPF = CPF
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.senha = senha
        self.coren = coren.format_coren()

    # método para retornar os dados em formato JSON
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "CPF": self.CPF,
            "telefone": self.telefone,
            "email": self.email,
            "sexo": self.sexo,
            "senha": self. senha
        }

if __name__ == "__main__":
    
    # instânciando as classes
    coren_1 = Coren("SC", "123.321", "ENF")

    # do objeto do tipo Coren para a composição do objeto tipo Enfermeiro
    enfermeiro_1 = Enfermeiro("José da Silva", "21/01/1989", "106.406.886.46", "(47) 9 91112020", "js@gmail.com", "masculino", "123", coren_1)

    # testando classes e os retornos
    print(f"O enfermeiro {enfermeiro_1.nome} atua com o {coren_1}")
