from fastapi import FastAPI
import pandas as pd

#cargo los datasets que voy a necesitar

user_stats = pd.read_parquet("user_stats.parquet")            #leo estos archivos para
user_total_price = pd.read_parquet("user_total_price.parquet") #la PRIMER funcion

user_review = pd.read_parquet("countreviews.parquet")#leo este archivo para la SEGUNDA funcion

ranking = pd.read_parquet("genre.parquet") #leo este archivo para la TERCER funcion

genero_y_usuario_agrupado = pd.read_parquet("userforgenres.parquet")#leo este archivo para la CUARTA funcion

#http://127.0.0.1:8000/

app = FastAPI()

@app.get("/")
def inicio():
    return {'mensaje' : 'hola'}

@app.get("/userdata/{user_id}") 
def userdata(user_id):
    user_price_data = user_total_price[user_total_price['user_id'] == user_id]
    user_stats_data = user_stats[user_stats['user_id'] == user_id]
    
    if not user_price_data.empty and not user_stats_data.empty:
        gasto = round(user_price_data['price'].iloc[0], 2)
        recomendacion = user_stats_data['recommend_sum'].iloc[0]
        total_items = user_stats_data['items_count'].iloc[0]
        
        return {                        #en el return tengo que indicarle que tipo es porque si no tira error interno
            'Usuario:': str(user_id),
            'Cantidad de dinero gastado:': int(gasto),
            'Porcentaje de recomendación:':  round((recomendacion / total_items) * 100, 2),
            'Cantidad de ítems:': int(total_items)
        }
    else:
        return 'Usuario no encontrado'
    
userdata('76561197970982479')

@app.get("/reviews{inicio}/{final}")

def get_reviews_count(inicio: str, final: str):
    mask = (user_review['posted'] >= inicio) & (user_review['posted'] <= final)
    reviews = user_review[mask]

    usuarios_unicos = reviews['user_id'].nunique()
    porcentaje_recomendacion = round(reviews['recommend'].sum() / reviews['recommend'].count() * 100,2)

    return {
        'Cantidad de usuarios con reviews': int(usuarios_unicos),
        'Porcentaje de recomendación': round(porcentaje_recomendacion, 2)
    }


@app.get("/genre/{genero}")
def genre(genero: str):
    posicion = ranking[ranking['genres'] == genero].index[0] + 1  #busco el genero en el df y su posicion
    return f"Eel genre {str(genero)} se encuentra en el puesto {int(posicion)}"

genre('RPG')

@app.get("/genre_ranking/{genero_ranking}")
def userforgenre(genre: str):
    genero_filtrado = genero_y_usuario_agrupado[genero_y_usuario_agrupado['genres'] == genre]
    top_usuario = genero_filtrado.sort_values(by='playtime_forever', ascending=False).head(5)
    return top_usuario[['user_id', 'user_url', 'playtime_forever']]

userforgenre('Action')