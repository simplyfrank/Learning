import socket

class Resolver:

    def __init__(self):
        self._cache = {}


    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache


def sequence_class(immutable):
    # CONDITIONAL EXPRESSION: Inline expression to handle if else based on a single comparison
    return tuple if immutable else list


# Lamda Expression
scientists = ['Marie Curie', 'Albert Einstein', 'Niels Bohr', 'Isaar Newton', 
                'Dmitri Mendeleev', 'Antoine Lavoisier', 'Carl Linnaeus', 
                'Alfred Wegener', 'Charles Darwin']

sorted(scientists, key=lambda name: name.split()[-1])

last_name = lambda name: name.split()[-1]

# Check for callability
callable(list)

def hypervolume(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v

hypervolume(3,4,5)

# Working with additional keyword arguments
def tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))

tag('img', src='monet.jpg', alt='Sunrise by Claude Monet', border=1)

def tag(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result

monday = [12,13, 14, 15, 16]
tuesday = [12,13, 14, 15, 16]
wednesday = [12,13, 14, 15, 16]

