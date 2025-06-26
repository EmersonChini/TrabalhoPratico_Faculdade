def loginUsuario(perfil):
    # Converte o valor para letras minúsculas e verifica se é admin
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Chamadas para teste
loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
loginUsuario('ADMIN')
