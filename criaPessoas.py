import random
from conexao import Conexao





nomes = ("Aarão", "Abner", "Ada", "Adão", "Adriana", "Adriano", "Afonso", "Agnes", "Alberto", "Alda",
         "Alice", "Alícia", "Alison", "Allan", "Amanda", "Ana", "André", "Andréia", "Angelo", "Anita",
         "Antônio", "Antônia", "Artur", "Augusto", "Aurora", "Beatriz", "Beltrão", "Benedita", "Benjamin",
         "Bernardo", "Bianca", "Bruno", "Camila", "Camilo", "Carlos", "Carolina", "Caroline", "César",
         "Clara", "Claudio", "Cleide", "Cleiton", "Conceição", "Cristiano", "Cristina", "Daniel", "Daniela",
         "Davi", "Débora", "Diego", "Diogo", "Douglas", "Eduardo", "Elaine", "Elena", "Elisa", "Elizabeth",
         "Emília", "Enzo", "Ernesto", "Esther", "Eugênio", "Eva", "Evelyn", "Fabiana", "Fábio", "Fátima",
         "Felipe", "Fernanda", "Fernando", "Flávia", "Francisco", "Gabriela", "Gabriel", "Gabriele", "Genivaldo",
         "George", "Georgia", "Gilberto", "Gilmar", "Giovanna", "Giovanni", "Gisele", "Gláucia", "Godofredo",
         "Gonçalo", "Graça", "Gregório", "Guilherme", "Gustavo", "Hannah", "Helena", "Henrique", "Henriqueta",
         "Hugo", "Iago", "Igor", "Inácio", "Ingrid", "Irene", "Isaías", "Isabel", "Isabela", "Ismael", "Israel",
         "Italo", "Ivan", "Izabela", "Jacqueline", "Jader", "Jaqueline", "Jefferson", "Jeniffer", "Jessica",
         "João", "Joana", "Joaquim", "Jorge", "José", "Josefina", "Josué", "Joana", "Júlia", "Juliana", "Juliano",
         "Júlio", "Júnior", "Jurema", "Juscelino", "Karen", "Karina", "Karla", "Karolline", "Kevin", "Laís",
         "Lara", "Laura", "Leonardo", "Leandro", "Letícia", "Lívia", "Lorena", "Lorenzo", "Lucas", "Luciana",
         "Luciano", "Luciene", "Luís", "Luísa", "Luiz", "Luzia", "Machado", "Madalena", "Mãe", "Maiara", "Manoel",
         "Marcelo", "Márcia", "Marco", "Marcos", "Margarida", "Mariana", "Mariano", "Marina", "Mário", "Marisa",
         "Marlene", "Marta", "Martin", "Mateus", "Matheus", "Matilde", "Maurício", "Maximiliano", "Melissa",
         "Michel", "Michele", "Miguel", "Milena", "Milton", "Miriam", "Mônica", "Monique", "Natália", "Natanael",
         "Nelson", "Neymar", "Nicholas", "Nicole", "Nicolas", "Nilson", "Nina", "Noel", "Noemi", "Olavo",
         "Olivia", "Omar", "Osmar", "Oswaldo", "Otávio", "Otilia", "Pablo", "Paloma", "Pamela", "Patrícia",
         "Patrick", "Paula", "Paulo", "Pedro", "Penha", "Peterson", "Pietra", "Rafael", "Rafaela", "Raimundo",
         "Raquel", "Raul", "Rayane", "Rebeca", "Regina", "Renata", "Renato", "Ricardo", "Roberta", "Roberto",
         "Rodrigo", "Rogerio", "Romário", "Romilda", "Ronaldo", "Rosa", "Rosana", "Roseane", "Rosemary",
         "Rubens", "Sabrina", "Samuel", "Sandra", "Sandro", "Sara", "Saulo", "Sebastião", "Selma", "Sérgio",
         "Sheila", "Silvana", "Silvio", "Simone", "Simony", "Sofia", "Sonia", "Sophia", "Sônia", "Stefanie",
         "Stella", "Sueli", "Suzana", "Tadeu", "Tamara", "Tânia", "Tatiana", "Taynara", "Teodoro", "Teresa"

)

sobrenomes = ("Alves", "Andrade", "Barbosa", "Barros", "Batista", "Bezerra", "Braga", "Cabral", "Cardoso", "Carvalho",
             "Castro", "Costa", "Cruz", "Dias", "Duarte", "Evangelista", "Fernandes", "Ferreira", "Fonseca", "França",
             "Gomes", "Gonçalves", "Guimarães", "Henrique", "Jesus", "Lima", "Lopes", "Machado", "Martins", "Mendes",
             "Miranda", "Monteiro", "Moraes", "Moreira", "Nascimento", "Nunes", "Oliveira", "Pereira", "Pinto", "Ramos",
             "Reis", "Ribeiro", "Rodrigues", "Santos", "Silva", "Souza", "Teixeira", "Vieira", "Almeida", "Azevedo",
             "Bueno", "Campos", "Coelho", "Correia", "Dias", "Domingues", "Fagundes", "Ferreira", "Gomes", "Gonçalves",
             "Guedes", "Lopes", "Machado", "Martins", "Mendes", "Morais", "Moreira", "Nascimento", "Nunes", "Oliveira",
             "Pereira", "Pinto", "Ramos", "Reis", "Ribeiro", "Rodrigues", "Santos", "Silva", "Souza", "Teixeira", "Vieira",
             "Alves", "Andrade", "Barbosa", "Barros", "Batista", "Bezerra", "Braga", "Cabral", "Cardoso", "Carvalho",
             "Castro", "Costa", "Cruz", "Dias", "Duarte", "Evangelista", "Fernandes", "Ferreira", "Fonseca", "França",
             "Gomes", "Gonçalves", "Guimarães", "Henrique", "Jesus", "Lima", "Lopes", "Machado", "Martins", "Mendes",
             "Miranda", "Monteiro", "Moraes", "Moreira", "Nascimento", "Nunes", "Oliveira", "Pereira", "Pinto", "Ramos",
             "Reis", "Ribeiro", "Rodrigues", "Santos", "Silva", "Souza", "Teixeira", "Vieira", "Almeida", "Azevedo",
             "Bueno", "Campos", "Coelho", "Correia", "Dias", "Domingues", "Fagundes", "Ferreira", "Gomes", "Gonçalves",
             "Guedes", "Lopes", "Machado", "Martins", "Mendes", "Morais", "Moreira", "Nascimento", "Nunes", "Oliveira",
             "Pereira", "Pinto", "Ramos", "Reis", "Ribeiro", "Rodrigues", "Santos", "Silva", "Souza", "Teixeira", "Vieira"
             )


sexo = ('M','F')

formacao = ('fundamental','ensino medio','graduacao','mestrado','doutorado')

id =0
empregoArea = (True, False)
cor = ('branco', 'preto', 'pardo')
estados = (
    'AC',  # Acre
    'AL',  # Alagoas
    'AP',  # Amapá
    'AM',  # Amazonas
    'BA',  # Bahia
    'CE',  # Ceará
    'DF',  # Distrito Federal
    'ES',  # Espírito Santo
    'GO',  # Goiás
    'MA',  # Maranhão
    'MT',  # Mato Grosso
    'MS',  # Mato Grosso do Sul
    'MG',  # Minas Gerais
    'PA',  # Pará
    'PB',  # Paraíba
    'PR',  # Paraná
    'PE',  # Pernambuco
    'PI',  # Piauí
    'RJ',  # Rio de Janeiro
    'RN',  # Rio Grande do Norte
    'RS',  # Rio Grande do Sul
    'RO',  # Rondônia
    'RR',  # Roraima
    'SC',  # Santa Catarina
    'SP',  # São Paulo
    'SE',  # Sergipe
    'TO'   # Tocantins
)


# Instanciando a classe Conexao
db = Conexao('127.0.0.1', 3306, 'pessoas', 'root', 'darkzed45')

# Conectando ao banco de dados
def insert(quntidadePesoa,tabela):
    db.conectar()


    for i in range(quntidadePesoa):
        nFormacao = random.randint(0, len(formacao) - 1)
        nNome = random.randint(0, len(nomes) - 1)
        nSexo = random.randint(0, len(sexo) - 1)
        nEmpregoArea = random.randint(0, len(empregoArea) - 1)
        Sobre = f"{sobrenomes[random.randint(0, len(sobrenomes) - 1)]} {sobrenomes[random.randint(0, len(sobrenomes) - 1)]} {sobrenomes[random.randint(0, len(sobrenomes) - 1)]}{sobrenomes[random.randint(0, len(sobrenomes) - 1)]}"
        Cor = f"{cor[random.randint(0,len(cor)-1)]}"
        Estado = f"{estados[random.randint(0,len(estados)-1)]}"
        if formacao[nFormacao] == 'mestrado':
            idade = random.randint(24, 50)
        elif formacao[nFormacao] == "doutorado":
            idade = random.randint(26, 50)
        else:
            idade = random.randint(18, 50)
        
        # Construindo a consulta SQL com placeholders %s
        sql = f"INSERT INTO {tabela} (nome, idade, sobrenome, empregoArea, sexo, formacao, cor, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        
        # Passando os valores para a consulta SQL
        valores = (nomes[nNome], idade, Sobre, empregoArea[nEmpregoArea], sexo[nSexo], formacao[nFormacao],Cor,Estado)
        
        # Executando a consulta SQL
        db.query(sql, valores)
        db.connection.commit()
    

    # Desconectando do banco de dados
    db.desconectar()
     
def select(table):
    db.conectar()

    sql = f"select * from {table}"
    cursor = db.query(sql)
    resultados = cursor.fetchall()
    db.desconectar()
    return resultados

insert(10000,'pessoaP')
insert(10000,'pessoaM')
insert(10000,'pessoaG')
insert(10000,'pessoaBG')



