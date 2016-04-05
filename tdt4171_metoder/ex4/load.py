def get_data(file_type='training'):
    data = []
    with open('./data/%s.txt' % file_type) as f:
        for line in f.readlines():
            line_as_list = list(map(lambda x: int(x), line.strip('\n').split('\t')))
            classification = line_as_list.pop()
            data.append({
                'class': classification,
                'object': line_as_list
            })
    return data
