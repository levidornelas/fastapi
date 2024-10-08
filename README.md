# Documentação do Projeto FastAPI: Gerenciamento de Filmes

#### Sumário

- Introdução
- Requisitos
- Endpoints da API

## Introdução

Este projeto é uma API simples de gerenciamento de filmes, utilizando FastAPI e Pydantic para a validação dos dados. A API permite listar filmes, consultar por autor, adicionar novos filmes, atualizar e deletar filmes. Spin-offs de filmes também podem ser registrados.

## Requisitos
- Python 3.9+
- FastAPI - Framework para construir APIs rápidas com Python.
- Uvicorn - Servidor ASGI para rodar o FastAPI.

## Endpoints da API

### 1. Listar Todos os Filmes:
  `GET /films`

**Exemplo de Resposta:**
```
[
  {
    "id": 1,
    "nome": "Retratos fantasmas",
    "autor": "kmf",
    "spinoffs": [
      {
        "nome": "Teste",
        "release": "2024-09-11"
      }
    ]
  },
  ...
]
```

### 2. Filtrar Filmes por Autor:
  `GET /films?autor={autor}`

**Exemplo de Resposta:**
```
[
  {
    "id": 3,
    "nome": "O agente Secreto",
    "autor": "jubileu",
    "spinoffs": []
  },
  ...
]
```

### 3. Obter Filme por ID:
  `GET /films/{film_id}`

**Exemplo de Resposta:**
```
{
  "id": 1,
  "nome": "Retratos fantasmas",
  "autor": "kmf",
  "spinoffs": [
    {
      "nome": "Teste",
      "release": "2024-09-11"
    }
  ]
}
```

### 4. Adicionar um Novo Filme:
  `POST /create`

**Corpo da Requisição:**
```
{
  "id": 6,
  "nome": "Novo Filme",
  "autor": "kmf",
  "spinoffs": []
}
```

### 5. Atualizar um Filme:
  `PUT /films/{film_id}`

**Corpo da Requisição:**
```
{
  "nome": "Novo Nome do Filme",
  "autor": "kmf",
  "spinoffs": [
    {
      "nome": "SpinOff Exemplo",
      "release": "2025-01-01"
    }
  ]
}
```

### 6. Deletar um Filme:
  `DELETE /films/{film_id}`
  
**Exemplo de resposta:** 
```
{
  "message": "Film deleted successfully."
}
```

### 7. Recomendar um filme com base na escolha de gênero:
`POST /recommend/`
