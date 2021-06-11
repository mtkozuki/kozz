import sys

def extract_domain(url):
    i = 0
    j = i
    domain = ''
    output = []

    while (i < len(url)):
        if (url[i] == '/'):
            j = j + 1

        if (j == 3):
              output.append(domain)
              output.append(i)
              return output
            
        domain = domain + url[i]
        i = i + 1

def extract_path(url, checkpoint):
    i = checkpoint
    path = ''
    output = []

    while (i < len(url)):
        if (url[i] == '?'):
            output.append(path)
            output.append(i)
            return output
        path = path + url[i]
        i = i + 1

def extract_parameters(url, checkpoint):
    i = checkpoint + 1
    j = True
    param = ''
    parameters = []

    while (i < len(url)):
        if (url[i] == '='):
            j = False
            parameters.append(param)
            param = ''
        if (j):
            param = param + url[i]
        if (url[i] == '&'):
            j = True
        i = i + 1
    return parameters

def extract_sections(url):
    domain = []
    path = []
    parameters = []

    domain = extract_domain(url)
    path = extract_path(url, domain[1])
    parameters = extract_parameters(url, path[1])

    append_dict(domain[0], path[0], parameters)

def append_dict(domain,path,parameters):
    i = 0
    key = domain + path
    params = []

    if key not in urls:
        urls[key] = parameters
    else:
        params = set(urls[key])
        for i in parameters:
            params.add(i)
        urls[key] = list(params)

def print_dict(word):
    params = ''
    url = ''
    i = 0

    for key, value in urls.items():
        while (i < len(value)):
            if (i == 0):
                params = params + value[i] + '=' + word
            else:
                params = params + '&' + value[i] + '=' + word
            i = i + 1
        url = key + '?' + params
        params = ''
        i = 0
        print(url)

urls = {}
file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()
for line in Lines:
    extract_sections(str(line.strip()))

print_dict('FUZZ')
