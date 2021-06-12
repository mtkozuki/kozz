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
    output.append(domain)
    output.append(i)
    return output

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
    output.append(path)
    output.append(i)
    return output

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

    if (domain[1] < len(url)):
        path = extract_path(url, domain[1])
    else:
        print(url)
        return 0

    if (path[1] < len(url)):
        parameters = extract_parameters(url, path[1])
    else:
        print(url)
        return 0
    
    append_dict(domain[0], path[0], parameters)
    return 1

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
        if('-vv' in sys.argv):
            print(url)

urls_processed = 0
urls = {}
file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()
for line in Lines:
    x = extract_sections(str(line.strip()))
    if (x != 1):
        urls_processed = urls_processed + 1


print_dict('FUZZ')
if ('-v' in sys.argv or '-vv' in sys.argv):
    print("Total Urls: ", len(Lines))
    print("Urls not processed: ", urls_processed)
    print("Unique endpoints: ", len(urls))

