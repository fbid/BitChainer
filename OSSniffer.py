import os

if os.name == 'posix':
    path_slash = '/'

elif os.name == 'nt':
    path_slash = '\\'
