from camelcase import CamelCase

instanciaCC = CamelCase('mundo', 'del')

texto = 'bienvenido al mundo del backend';

print(instanciaCC.hump(texto))