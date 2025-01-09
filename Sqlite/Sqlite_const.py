'''
Константы для работы с SQLite
'''

ini_fn = 'Ini_Chinook_Sqlite.sqlite'
wrk_fn = 'Chinook_Sqlite.sqlite'
my_db_fn = 'MyChinook_Sqlite.sqlite'
tables_list = ['albums','artists','customers','employees','genres','invoice_items',
               'invoices','media_types', 'playlist_track','playlists','tracks']

def create_dict_with_tables()->dict:
    '''
    https/stackoverflow.com/questions/35830612/how-to-create-a-new-dictionary-in-for-loop
    '''
    tables_dict:dict ={}
    i = 0
    for s in tables_list:
        tables_dict[s] =[]
        i += 1
    return tables_dict

if __name__ == "__main__":
    # print(tables_list)
    # print('-- main_dict --')
    # print(create_dict_with_tables())
    pass
