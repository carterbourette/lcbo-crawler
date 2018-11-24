class Product:
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        string = ''
        for k,v in vars(self).items():
            if k == 'image':
                string += k + '=' + str(v[:50]) + '...\n'
            else:
                string += k + '=' + str(v) + '\n'

        return string
