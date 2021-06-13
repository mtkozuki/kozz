import sys

def extract_domain(url):
    i = 2
    j = 0
    c = 0
    domain = ''
    output = []
    port = False

    while (i < len(url)):
        if (url[i] == '/'):
            j = j + 1

        if (j == 3):
            output.append(domain)
            output.append(i)
            return output
        
        if (url[i] == ':'):
            if (c == 1):
                port = True
            c = 1

        if (port == False):
            domain = domain + url[i]

        i = i + 1
    output.append(domain)
    output.append(i)
    return output

def extract_path(url, checkpoint):
    i = checkpoint
    path = ''
    tree = 0
    output = []

    while (i < len(url)):
        if (url[i] == '/'):
            tree = tree + 1
            position = i

        if (url[i] == '?'):
            output.append(path)
            output.append(i)
            output.append(tree)
            output.append(position)
            return output
        path = path + url[i]
        i = i + 1
    output.append(path)
    output.append(i)
    output.append(tree)
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
            if (url[i] != '&'):
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
        is_valid = validate_path(path)
        if (is_valid == 0):
            return 1

    else:
        #print(url)
        return 0

    if (path[1] < len(url)):
        parameters = extract_parameters(url, path[1])
        
        for i in parameters:
            set_of_params.add(i)
        
        append_dict_url(domain[0], path[0], parameters)
        return 1
    else:
        #print(url)
        return 0

def validate_path(path):
    endpath = ''
    subpath = ''
    i = 0
    j = 0
    k = 0

    if (path[2] == 1):
        return 1

    while i < len(path[0]): 
        try:
            x = path[0][(path[3] + 1)]
            if (j != path[2]):
                subpath = subpath + path[0][i]
            else:
                endpath = endpath + path[0][i]
            
            if (path[0][i] == '/'):
                j = j + 1

            if (endpath != ''):
                for path in subpaths:
                    if (path == subpath):
                        k = k + 1
                    if (k == 5):
                        return 0
                subpaths.append(subpath)
                return 1
        except:
            if ('-h' in sys.argv):
                    if (j != (path[2] - 1)):
                        subpath = subpath + path[0][i]
                    else:
                        endpath = endpath + path[0][i]
                    
                    if (path[0][i] == '/'):
                        j = j + 1

                    if (endpath != ''):
                        for path in subpaths:
                            if (path == subpath):
                                k = k + 1
                            if (k == 5):
                                return 0
                        subpaths.append(subpath)
                        return 1
        
        i = i + 1
    return 1

def append_dict_url(domain,path,parameters):
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

        if('-k' in sys.argv):
            print(url)

init = []
set_of_params = set(init)
urls_not_processed = 0
threshold_of_paths = 0
urls = {}
subpaths = []
file1 = open(sys.argv[1], 'r+b')
Lines = file1.readlines()
for line in Lines:
    x = extract_sections(str(line.strip()))
    if (x == 0):
        urls_not_processed = urls_not_processed + 1

if('-k' in sys.argv):
    print_dict('FUZZ')
if ('--params' in sys.argv):
    list_of_params = list(set_of_params)
    for i in list_of_params:
        print(i)
    print()
if ('-n' in sys.argv):
    print("Total Urls: ", len(Lines))
    print("Urls not processed: ", urls_not_processed)
    print("Unique endpoints: ", len(urls))
    
file1.close()

