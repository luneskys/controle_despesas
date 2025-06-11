# 💰 Controle de Despesas Pessoais

Um sistema web de controle financeiro pessoal desenvolvido com **Django**, com funcionalidades de autenticação, cadastro de transações (despesas/receitas), categorias e dashboard básico.

---

## 🚀 Funcionalidades

- ✅ Registro e login de usuários
- ✅ Autenticação com sessão segura
- ✅ CRUD completo de transações (criar, listar, editar, excluir)
- ✅ Cadastro de categorias de despesas e receitas
- ✅ Filtro por usuário logado
- ✅ Interface simples com navegação clara
- ✅ Estrutura pronta para gráficos e relatórios

---

## 🛠️ Tecnologias utilizadas

- Python 3.11+
- Django 5.2+
- SQLite3 (banco padrão)
- HTML5 + CSS (estilo básico embutido)
- Django Template Language (DTL)

---

## 📦 Instalação

```bash
# Clone o projeto
git clone https://github.com/luneskys/controle-despesas.git
cd controle-despesas

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações
python manage.py migrate

# Crie um superusuário (opcional, para acessar o admin)
python manage.py createsuperuser

# Rode o servidor de desenvolvimento
python manage.py runserver
