# Kenzie Commerce

API voltado para atividades de e-commerce.

---

# Instalação

### Passo-a-passo

1. Criar um ambiente de desenvolvimento virtual.

```
python -m venv venv
```

2. Ativar o ambiente virtual.

```
source ./venv/Scripts/activate
```

3. Instalar os pacotes necessário.

```
pip install -r requirements.txt
```

4. Realizar as migrações para o banco de dados.

```
python manage.py migrate
```

5. Executar o servidor local.

```
python manage.py runserver
```

# Documentação

Após executar o servidor, acessar a rota:

```
127.0.0.1:8000/api/docs/
```
