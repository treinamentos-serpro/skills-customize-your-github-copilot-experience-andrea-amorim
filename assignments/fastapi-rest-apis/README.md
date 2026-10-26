# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com FastAPI, definindo endpoints, validando dados com modelos e implementando operações CRUD com respostas HTTP apropriadas.

## 📝 Tarefas

### 🛠️ Inicializar a API e Criar um Endpoint de Leitura

#### Descrição
Complete o código inicial para executar uma aplicação FastAPI e disponibilizar uma rota que liste as tarefas armazenadas em memória. Instale as dependências com `pip install fastapi uvicorn` e inicie o servidor com `uvicorn starter-code:app --reload`.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI com o título `Task API`.
- Definir um modelo Pydantic `TaskCreate` com um título obrigatório e um campo `completed` que seja `False` por padrão.
- Implementar `GET /tasks` para retornar a lista de tarefas, inicialmente vazia.
- Permitir que a documentação interativa da API seja acessada em `/docs`.

### 🛠️ Criar e Consultar Tarefas

#### Descrição
Adicione operações para criar uma tarefa e consultar uma tarefa específica pelo seu identificador. Mantenha os dados em memória durante a execução do servidor.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` para receber e validar dados usando `TaskCreate`.
- Atribuir um identificador único a cada tarefa criada e incluir esse identificador na resposta.
- Implementar `GET /tasks/{task_id}` para retornar a tarefa correspondente.
- Retornar os dados da tarefa criada ou consultada em formato JSON.

### 🛠️ Atualizar e Excluir Tarefas

#### Descrição
Complete as operações CRUD implementando a atualização e a exclusão de tarefas existentes. Trate as solicitações que usam identificadores inexistentes.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /tasks/{task_id}` para atualizar os dados de uma tarefa existente.
- Implementar `DELETE /tasks/{task_id}` para excluir uma tarefa existente.
- Retornar o status HTTP `404` para operações sobre identificadores inexistentes.
- Permitir verificar as alterações e exclusões consultando novamente `GET /tasks` ou `GET /tasks/{task_id}`.
