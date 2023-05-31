import DataBaseConnect
import json
from count_time import count_time
with open(r'C:\Users\den-s\OneDrive\Desktop\HackathonFinal\DataBase\json.json', 'r', encoding='utf-8') as file:
    json_data = file.read()

my_list = json.loads(json_data)

def create_insert_query(list,table):
    posts = ''
    for i in list:
        full_name = i['full_name']
        full_name = full_name.replace("'", "''")
        description = i['description']
        description = description.replace("'", "''")
        img_src = i['photos_list']
        post_link = i['post_link']
        if img_src != None:
            new_string = ''
            for j in img_src:
                new_string += f'{j},'
            all_src = '{' + f'{new_string[:-1]}' + '}'
        else:
            all_src = '{}'
        
        adding_time = count_time(i['clock'])
        posts += f"('{full_name}','{description}','{all_src}','{adding_time}','{post_link}'),"

    posts = f'{posts[:-1]}'
    one_day_query = f"""
    DROP TABLE {table};
    CREATE TABLE {table}
    (
        id SERIAL NOT NULL PRIMARY KEY,
        full_name TEXT NOT NULL,
        description TEXT,
        img_src TEXT[],
        adding_time TIMESTAMP  ,
        post_link text

    );
    INSERT INTO {table}(full_name,description,img_src,adding_time,post_link)
    VALUES
    {posts}

    """

    return one_day_query
def create_give_query(table):
    give_query = f"""
    DROP TABLE {table};
    CREATE TABLE {table} AS
    SELECT *
    FROM one_day_posts
    WHERE description ILIKE ANY (ARRAY['%отдаю%', '%отдаём%', '%отдается%', '%отдам%', '%заберите%']);

    """
    return give_query

DataBaseConnect.change(create_insert_query(my_list,'one_day_posts'))
DataBaseConnect.change(create_give_query('give_posts'))
print('DataBase has uloaded\n')


