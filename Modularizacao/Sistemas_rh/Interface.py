
from Sistemas.Registros_login import registros
from Sistemas.Cadastros_funcionários import Cadastro_func

#Criar laiout básico
def layout(titulo=''):
    print('='*35)
    print(f'=======   {titulo.upper()}    ========')
    print('='*35)



layout('Sistema de RH')


# Instanciar sistema de login
Sist_usuarios = registros.usuario()

# Instanciar sistema de reistro de funcionários
Cadastros = Cadastro_func.RegistroFuncionarios()


# Anlisar se usuário é cadastrado

while True:
    resp = str(input('Você já possui conta em nosso sistema? ')).strip().lower()
    if resp != 'sim' and resp != 'não':
        print('Resposta inválida! Responda com sim ou não')
    else:
        break

if resp == 'sim':
# Iniciar etapa de login caso esteja registrado

    # Logar no sistema
    while True:
        usuario = str(input('Nome de usuário: '))
        senha = str(input('Informe Senha de 8 dígitos: '))
        Sist_usuarios.criar_banco_dados_us('Registros_login', 'registro_usuarios')

        if Sist_usuarios.logar(usuario, senha):
            print(f'Bem vindo{usuario}!')
            break
        else:
            print('Usuario ou senha inválidos!')


#   Registrar funcionário
    while True:
        # Acessar banco de dados e inserir informações
        Cadastros.criar_banco_dados_func('Cadastros_funcionários','Funcionarios')
        try:
            acao = int(input('''
            0 - Procurar funcionario
            1 - Registrar funcionário
            Informe uma operação:
            '''))

            if acao == 0:
                nome = str(input('Informe um nome: '))
                if Cadastros.mostrar_dados(nome):
                    print(Cadastros.funcionario)
                else:
                    print('Funcionário não registrado!')

            elif acao == 1:
                Cadastros.gravar_registros()

            else:
                print('Operação inválida!')

        except:
            print('Você deve informar uma das opções disponíveis!')

        # Encerrar operação
        resp = str(input('Encerrar seção? ')).lower()
        if Cadastros.encerrar_processo(resp):
            break


# Criar conta de usuário
elif resp == 'não':
    nome_usu = str(input('Informe seu nome de usuário: '))
    data = str(input('Informe sua data de nascimento: '))
    email = str(input('Informe um endereço de email: '))

    while True:
        cpf = str(input('Informe seu cpf: '))
        cad_senha = str(input('Registre uma senha de 8 dígitos: '))
        if len(cpf) != 11 or not cpf.isnumeric():
            print('CPF inválido!\nO cpf deve conter 11 números, não digite o -')
        elif len(cad_senha) < 8 or not cad_senha.isalnum():
            print('Senha inválida!\nSua senha deve conter. no mínimo, 8 caracteres incluindo letras e números')
        else:
            break


    Sist_usuarios.criar_banco_dados_us('Registros_login', 'registro_usuarios')
    Sist_usuarios.registrar_usuario(nome_usu,data,cpf, email,cad_senha)

