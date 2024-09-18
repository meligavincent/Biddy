import requests  

# Remplacez 'votre_access_key' par votre clé d'accès Unsplash  
access_key = '-rRWjpi54q8Y9TXKGCWSnUnDqYtapV4L5eAM50a57Nc'  
photo_name = 'poulet_pane'  # Remplacez par le nom de la photo que vous recherchez  

# Étape 1 : Trouver l'ID de la photo par son nom  
search_url = f'https://api.unsplash.com/search/photos?query={photo_name}&client_id={access_key}'  
response = requests.get(search_url)  
data = response.json()  

if data['results']:  
    photo_url = data['results'][0]['urls']['full']  

    # Étape 2 : Télécharger la photo  
    photo_response = requests.get(photo_url)  
    
    with open(f'{photo_name}.jpg', 'wb') as file:  
        file.write(photo_response.content)  
    print(f'Photo téléchargée : {photo_name}.jpg')  
else:  
    print('Aucune photo trouvée.')