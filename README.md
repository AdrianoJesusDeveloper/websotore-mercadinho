# Webstore Mercadinho - Backend

Este é o backend do projeto **Webstore Mercadinho**, desenvolvido em **Django** para gerenciar carrinho de compras, produtos, usuários e pedidos.

---

## 🚀 Tecnologias Utilizadas
- **Python 3**
- **Django**
- **Django REST Framework**
- **SQLite3** (padrão, pode ser substituído por PostgreSQL ou MySQL)
- **dotenv** para variáveis de ambiente

---

## 📂 Estrutura do Projeto

```
backend/
│── manage.py
│── requirements.txt
│── .env
│── mercadinho_backend/   # Configurações principais do Django
│── cart/                 # App responsável pelo carrinho de compras
│── products/             # App responsável pelos produtos
│── users/                # App de autenticação e usuários
│── orders/               # App de pedidos
```

---

## ⚙️ Configuração do Ambiente

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/webstore-mercadinho.git
   cd webstore-mercadinho/backend
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o arquivo `.env` com as variáveis necessárias:
   ```env
   SECRET_KEY=sua_chave_secreta
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```

6. Crie um superusuário para acessar o Django Admin:
   ```bash
   python manage.py createsuperuser
   ```

7. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

---

## 📌 Endpoints Principais

- `/api/products/` → Listagem e gestão de produtos
- `/api/cart/` → Operações do carrinho de compras
- `/api/orders/` → Gestão de pedidos
- `/api/users/` → Autenticação e gerenciamento de usuários

---

## ✅ Próximos Passos
- Implementar autenticação com JWT
- Adicionar testes unitários
- Configurar deploy em produção (Render, Railway, ou AWS)

---

## 👨‍💻 Autor
Projeto desenvolvido por **Adriano Jesus** como parte do estudo em **Django + APIs REST**.
