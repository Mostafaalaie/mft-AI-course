def get_music_info():
    switch = 1
    music_info_list = []
    while switch == 1:
        music = input("Enter music information: ")
        if music == '0':
            switch = 0
        else:
            music_info_list.append(music)

    return music_info_list

def orgenize(info_list):
    temp_list = []
    
    for item in info_list:
        temp = item.split('-')
        temp_list.append(temp[0])
        temp_list.append(temp[1])
        
    music_list = temp_list[0::2]
    genre_list = temp_list[1::2]
    rock_counter = 0
    metal_counter = 0
    
    for item in genre_list:
        if item == "rock":
            rock_counter +=1
        elif item == "metal":
            metal_counter +=1
        else:
            pass

    result = [rock_counter, metal_counter]

    return result

# a = ["a-rock","b-metal","c-metal","d-pop"]
a = get_music_info()

b = orgenize(a)

print(b)