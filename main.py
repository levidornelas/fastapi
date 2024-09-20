from fastapi import FastAPI, HTTPException
from typing import List, Optional

app = FastAPI()

# Banco de dados simulado
FILMS = [
    {'id': 1, 'nome': 'Retratos fantasmas', 'autor': 'kmf', 'spinoffs': [{'nome': 'Teste', 'release': '2024-09-11'}]},
    {'id': 2, 'nome': 'Aquarius', 'autor': 'kmf'},
    {'id': 3, 'nome': 'O agente Secreto', 'autor': 'jubileu'},
    {'id': 4, 'nome': 'Recife Frio', 'autor': 'jubileu'},
    {'id': 5, 'nome': 'O som ao redor', 'autor': 'jamaica'}
]

# Função de busca em profundidade (DFS) para recomendação de filmes
def dfs_recommendation(tree, preference, path=None):
    if path is None:
        path = []

    # Adiciona o gênero escolhido ao caminho
    path.append(preference)

    if preference in tree:
        return path + [tree[preference][0]]  # retorna o primeiro item como recomendação

    # Se o gênero não for encontrado
    return None

@app.post("/recommend/")
async def recommend(preferences: List[str]):
    # Itera sobre as preferências e tenta encontrar uma recomendação usando DFS
    for preference in preferences:
        recommendation_path = dfs_recommendation(FILMS, preference)
        if recommendation_path:
            return {"path": recommendation_path, "recommendation": recommendation_path[-1]}
    
    raise HTTPException(status_code=404, detail="Nenhuma recomendação encontrada")

# Endpoints de CRUD

@app.get('/films')
async def get_films(autor: Optional[str] = None):
    if autor:
        return [f for f in FILMS if f['autor'].lower() == autor.lower()]
    return FILMS

@app.get('/films/{films_id}')
async def get_film_by_id(films_id: int):
    film = next((f for f in FILMS if f['id'] == films_id), None)
    if film is None:
        raise HTTPException(status_code=404, detail='Film not found.')
    return film

@app.get('/films/autor/{autor}')
async def get_films_by_author(autor: str):
    films = [f for f in FILMS if f['autor'].lower() == autor.lower()]
    if not films:
        raise HTTPException(status_code=404, detail='No films found for this author.')
    return films

@app.post('/create')
async def create_films(film_data: dict):
    new_id = max(f['id'] for f in FILMS) + 1
    new_film = {
        'id': new_id,
        'nome': film_data['nome'],
        'autor': film_data['autor'],
        'spinoffs': film_data.get('spinoffs', [])
    }
    FILMS.append(new_film)
    return new_film

@app.put("/films/{film_id}")
async def update_film(film_id: int, film_data: dict):
    film = next((f for f in FILMS if f['id'] == film_id), None)
    if film is None:
        raise HTTPException(status_code=404, detail="Film not found.")
    
    film.update({
        'nome': film_data['nome'],
        'autor': film_data['autor'],
        'spinoffs': film_data.get('spinoffs', [])
    })
    
    return film

@app.delete("/films/{film_id}")
async def delete_film(film_id: int):
    film = next((f for f in FILMS if f['id'] == film_id), None)
    if film is None:
        raise HTTPException(status_code=404, detail="Film not found.")
    
    FILMS.remove(film)
    return {"message": "Film deleted successfully."}
