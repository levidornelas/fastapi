from fastapi import FastAPI, HTTPException
from schemas import Authors, FilmBase, FilmWithID, FilmCreate

app = FastAPI()

# Banco de dados simulado
FILMS = [
    {'id': 1, 'nome': 'Retratos fantasmas', 'autor': 'kmf', 'spinoffs': [{'nome': 'Teste', 'release': '2024-09-11'}]},
    {'id': 2, 'nome': 'Aquarius', 'autor': 'kmf'},
    {'id': 3, 'nome': 'O agente Secreto', 'autor': 'jubileu'},
    {'id': 4, 'nome': 'Recife Frio', 'autor': 'jubileu'},
    {'id': 5, 'nome': 'O som ao redor', 'autor': 'jamaica'}
]

@app.get('/films')
async def get_films(autor: Authors | None = None) -> list[FilmBase]:
    if autor: 
        return [FilmWithID(**f) for f in FILMS if f['autor'].lower() == autor.value]
    return [FilmWithID(**f) for f in FILMS]

@app.get('/films/{films_id}')
async def get_film_by_id(films_id: int) -> FilmWithID:
    film = next((FilmWithID(**f) for f in FILMS if f['id'] == films_id), None)
    if film is None:
        raise HTTPException(status_code=404, detail='Film not found.')
    return film

@app.get('/films/autor/{autor}')
async def get_films_by_author(autor: Authors) -> list[dict]:
    films = [f for f in FILMS if f['autor'].lower() == autor.value]
    if not films:
        raise HTTPException(status_code=404, detail='No films found for this author.')
    return films

@app.post('/create')
async def create_films(film_data: FilmCreate) -> FilmWithID:
    new_id = max(f['id'] for f in FILMS) + 1
    new_film = {
        'id': new_id,
        'nome': film_data.nome,
        'autor': film_data.autor,
        'spinoffs': film_data.spinoffs
    }
    FILMS.append(new_film)
    return FilmWithID(**new_film)

@app.put("/films/{film_id}")
async def update_film(film_id: int, film_data: FilmCreate) -> FilmWithID:
    film = next((f for f in FILMS if f['id'] == film_id), None)
    if film is None:
        raise HTTPException(status_code=404, detail="Film not found.")
    
    film.update({
        'nome': film_data.nome,
        'autor': film_data.autor,
        'spinoffs': film_data.spinoffs
    })
    
    return FilmWithID(**film)

# Deleta um filme específico
@app.delete("/films/{film_id}")
async def delete_film(film_id: int):
    film = next((f for f in FILMS if f['id'] == film_id), None)
    if film is None:
        raise HTTPException(status_code=404, detail="Film not found.")
    
    FILMS.remove(film)
    return {"message": "Film deleted successfully."}