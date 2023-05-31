from bs4 import BeautifulSoup
import json


with open(r"C:\Users\den-s\OneDrive\Desktop\HackathonFinal\Parser\FacebookPage.html",'r',encoding='utf-8') as fp:
    src = fp.read()
soup = BeautifulSoup(src,'html.parser')
items = soup.find_all('div',{'class':'x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z'})

new_list = []
for item in items:
    full_name = item.find('div',{'class':'xu06os2 x1ok221b'}).text
    clock = item.find('span',{'class':'x4k7w5x x1h91t0o x1h9r5lt x1jfb8zj xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j'}).text
    description = item.find('span',{'class':'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h'})
    if description == None:
        description = item.find('div',{'class':'xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs'})
        if description == None:
            description = 'NULL'
        else:
            description = description.text
    else:
        description = description.text
    photos_list = []
    images = item.find_all('img',{'class' : 'x1ey2m1c xds687c x5yr21d x10l6tqk x17qophe x13vifvy xh8yej3'})
    images2 = item.find_all('img',{'class' : 'x1ey2m1c xds687c x5yr21d x10l6tqk x17qophe x13vifvy xh8yej3 xl1xv1r'})
    test = False
    if len(images) != 0:
        for image in images:
            image_src = image['src']
            photos_list.append(image_src)
    elif len(images2) != 0:
        for image in images2:
            image_src = image['src']
            photos_list.append(image_src)
    else:
        photos_list = None
    post_link = item.find('a',{'class':'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv xo1l8bm'})
    post_link = post_link['href']
    new_dict = {
        "full_name" :full_name,
        "clock" :clock,
        "description" :description,
        "photos_list" :photos_list,
        'post_link': post_link
    }
   
    new_list.append(new_dict)



json_data = json.dumps(new_list)

with open('C:/Users/den-s/OneDrive/Desktop/HackathonFinal/DataBase/json.json', 'w',encoding='utf-8') as file:
    file.write(json_data)

print('Json file is done\n')