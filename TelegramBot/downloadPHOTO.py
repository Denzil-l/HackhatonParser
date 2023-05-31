import requests
def download_photo(url,index,src,i):
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'{src}photo{i}{index}.jpg', 'wb') as file:
            file.write(response.content)
        return 'photo.jpg'  # Return the filename under which the photo is saved
    else:
        return None 
    
def make_photos(data_base,src):
    for i in range(len(data_base)):
        if len(data_base[i][3]) > 0:                    
            index = 0
            for url in data_base[i][3]:
                download_photo(url,index,src,i)
                index+=1

