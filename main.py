import requests
import json
import networkx as nx
import matplotlib.pyplot as plt
from termcolor import colored


API_KEY = ' e9331fd8e416356119df66fbeed97751'
BASE_URL = 'http://ws.audioscrobbler.com/2.0/'

def get_similar_tracks(artist, track):
    params = {
        'method': 'track.getsimilar',
        'artist': artist,
        'track': track,
        'api_key': API_KEY,
        'format': 'json'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        tracks = json.loads(response.text)['similartracks']['track']
        return [track['name'] for track in tracks]
    else:
        return []

def get_track_tags(artist, track):
    params = {
        'method': 'track.gettoptags',
        'artist': artist,
        'track': track,
        'api_key': API_KEY,
        'format': 'json'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        response_json = json.loads(response.text)
        if 'toptags' in response_json:
            tags = response_json['toptags']['tag']
            return [tag['name'] for tag in tags]
    return []


def get_similar_tracks_graph(artist, track, num_similar=5):
    graph = nx.Graph()
    graph.add_node((artist, track))

    similar_tracks = get_similar_tracks(artist, track)[:num_similar]
    for similar_track in similar_tracks:
        graph.add_node((artist, similar_track))
        graph.add_edge((artist, track), (artist, similar_track))

        similar_tags = get_track_tags(artist, similar_track)
        for neighbor in graph.nodes():
            if neighbor == (artist, track) or neighbor == (artist, similar_track):
                continue
            tags = get_track_tags(*neighbor)
            if not similar_tags or not tags:
                continue
            similarity = len(set(similar_tags) & set(tags)) / len(set(similar_tags) | set(tags))
            if similarity > 0:
                graph.add_edge((artist, similar_track), neighbor, weight=similarity)

    return graph

def recommend_tracks(artist, track, num_similar=5, num_recommendations=10):
    graph = get_similar_tracks_graph(artist, track, num_similar=num_similar)
    similarities = nx.shortest_path_length(graph, (artist, track), weight='weight')
    similarities = {k[1]: v for k, v in similarities.items() if k[0] == artist and k[1] != track}
    sorted_similarities = sorted(similarities.items(), key=lambda x: x[1])
    recommended_tracks = [track for track, similarity in sorted_similarities][:num_recommendations]
    return recommended_tracks


ascii_art = colored(r'''
  __  __           _  _____                 _    __   __
 |  \/  |         (_)/ ____|               | |   \ \ / /
 | \  / |_   _ ___ _| |  __ _ __ __ _ _ __ | |__  \ V / 
 | |\/| | | | / __| | | |_ | '__/ _` | '_ \| '_ \  > <  
 | |  | | |_| \__ \ | |__| | | | (_| | |_) | | | |/ . \ 
 |_|  |_|\__,_|___/_|\_____|_|  \__,_| .__/|_| |_/_/ \_\
                                     | |                
                                     |_|                
''', 'green', attrs=['bold'])

print(ascii_art)

artist = input('Escreva o nome do artista: ')
track = input('Escreva o nome da música: ')
num_similar = int(input('Quantas musicas similares devo procurar? (default=5): ') or 5)
num_recommendations = int(input('Quantas recomendações (default=10): ') or 10)

# Get and display the recommended tracks
recommended_tracks = recommend_tracks(artist, track, num_similar=num_similar, num_recommendations=num_recommendations)
print(f'\nMusicas recomendadas para "{track}" de {artist}:')
for i, recommended_track in enumerate(recommended_tracks):
    print(f'{i+1}. {recommended_track}')
