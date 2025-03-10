def sort_on(dict):
    return dict["count"]

def sorted_char(dict):
    sorted_result = []
    for key in dict:
        sorted_result.append({"char": key, "count": dict[key]})
    sorted_result.sort(key=sort_on, reverse=True)
    return sorted_result

def print_result(list):

    for key in list:
      print(f"{key.get('char')}: {key.get('count')}")
        

def get_num_words(content):
    words = content.split()
    return len(words)

def get_num_characters(content):
    characters = {}
    words = content.split()
    for word in words:
        for char in word:
            if char.lower() in characters:
                characters[char.lower()] += 1
            else:
                characters[char.lower()] = 1
    return characters