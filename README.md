# 🛒 Webstore Mercadinho

Projeto de e-commerce simples desenvolvido com **Django (backend)** e **React (frontend)**.  
O sistema possui autenticação de usuários, gerenciamento de produtos, carrinho de compras e pedidos.

---

## 🚀 Tecnologias Utilizadas

### Backend
- Python 3
- Django & Django REST Framework
- SQLite (padrão, mas pode ser configurado para PostgreSQL/MySQL)
- Django Environ (variáveis de ambiente)

### Frontend
- React
- Vite
- Axios (requisições HTTP)
- Sass/Scss (estilização)

---

## 📂 Estrutura do Projeto

```bash
backend/
│── manage.py
│── requirements.txt
│── .env
│── mercadinho_backend/   # Configurações principais do Django
│── cart/                 # App responsável pelo carrinho de compras
│── products/             # App responsável pelos produtos
│── users/                # App de autenticação e usuários
│── orders/               # App de pedidos

frontend/                 # Aplicação React (interface do usuário)
│── src/                  # Código principal do frontend
│── package.json
│── vite.config.js
```

---

## ⚙️ Como Rodar o Projeto

### 🔹 Backend (Django)

1. Clone o repositório e entre na pasta do backend:
   ```bash
   cd backend
   ```

2. Crie o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o arquivo `.env` (exemplo abaixo):
   ```env
   SECRET_KEY=suachavesecreta
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. Rode as migrações e inicie o servidor:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

---

### 🔹 Frontend (React)

1. Acesse a pasta do frontend:
   ```bash
   cd frontend
   ```

2. Instale as dependências:
   ```bash
   npm install
   ```

3. Inicie o servidor de desenvolvimento:
   ```bash
   npm run dev
   ```

---

## 📌 Funcionalidades

✅ Cadastro e autenticação de usuários  
✅ Listagem e gerenciamento de produtos  
✅ Carrinho de compras persistente  
✅ Criação e gerenciamento de pedidos  
✅ Integração entre frontend e backend via API REST  

---

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b minha-feature`)
3. Commit suas alterações (`git commit -m 'Adicionei nova feature'`)
4. Faça o push para a branch (`git push origin minha-feature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

👨‍💻 Desenvolvido por Adriano Jesus 🚀
