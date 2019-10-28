import re


def clean_data(message):
    print('message', message)
    stripped = (c for c in message if 0 < ord(c) < 127)
    return ''.join(stripped)


def structure_message(message):
    clean_message = clean_data(message)
    holograms = get_holograms(clean_message)
    plates = get_plates(clean_message)
    color = get_color(clean_message)
    return {'hologramas': holograms,
            'placas': plates,
            'color': color}


def get_holograms(message):
    return find_numbers_from_string(r'holograma (\d) y (\d)', message)


def get_plates(message):
    return find_numbers_from_string(r'de placa(\d) y (\d)', message)


def get_color(message):
    color = re.findall(r'engomado (\S+) ', message)
    return color[0] if len(color) > 0 else ''


def find_numbers_from_string(pattern, message):
    data = re.findall(pattern, message)
    if len(data) > 0:
        data = [int(x) for x in data[0]]
    else:
        data = []
    return data
