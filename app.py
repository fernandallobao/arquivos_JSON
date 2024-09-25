#importação
import os
from pessoa import *
from manipulador import *

if __name__ == '__main__':
    #instanciando objetos
    p = Pessoa(0,'','','','')
    m = Manipulador()

    while True:
        print('1 - Criar novo arquirvo JSON')
        print('2 - Abrir e ler arquirvo JSON')
        print('3 - Salvar novo usuário')
        print('4 - Alterar dados do usuário')
        print('5 - Deletar usuário')
        print('0 - Sair do programa.')

        op = input('Informe a opção desejada: ')

        #limpeza do console
        os.system('cls')

        match op:
            case '0':
                break
            case '1':
                novo_arquivo = input('Informe o nome do arquivo que deseja criar: ')
                print(m.criar_arquivo(novo_arquivo))
                continue
            case '2':
                abrir_arquivo = input('Informe o nome do arquivo que deseja abrir: ')
                try:
                    os.system('cls')
                    usuarios = m.abrir_arquivo(abrir_arquivo)
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    for i in range(len(usuarios)):
                        for campo in usuarios[i]:
                            print(f'{campo.capitalize()}:{usuarios[i].get(campo)}.')
                        print(f'\n{'-'*10}\n')
                except Exception as e:
                    print(f'Não foi possivel abrir o arquivo. {e}.')
                finally:
                    continue
            case '3':
                try:
                    #primeira forma de fazer
                    # usuario = {}
                    # campos = ('nome', 'cpf', 'email', 'profissao')
                    # print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    # usuario['codigo'] = len(usuarios) #verfifica a quantidade de usuários e gera um novo código para o novo usuario
                    # for campo in campos:
                    #     usuario[campo] = input(f'Informe o campo {campo.capitalize()}:')
                    # usuarios.append(usuario)
                    # print(m.salvar_dados(usuarios, abrir_arquivo))
                    #--------------------------------------------
                    #segunda forma de fazer
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    p.codigo = len(usuarios)
                    p.nome = input('Informe o nome: ')
                    p.cpf = input('Informe o cpf: ')
                    p.email = input('Informe o email: ')
                    p.profissao = input('Informe a profissao: ')
                    usuario = dict(codigo=p.codigo, nome=p.nome, cpf=p.cpf, email=p.email, profissao=p.profissao) #dict outra forma de criar um dicionário
                    usuarios.append(usuario)
                    print(m.salvar_dados(usuarios, abrir_arquivo))
                except Exception as e:
                    print(f'Não foi possível realizar a operação.{e}')
                finally:
                    continue
            case '4':
                try:
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    codigo = int(input('Informe o código do usuário que deseja alterar: '))
                    for campo in usuarios[codigo]:
                        print(f'Valor do campo código: {campo}:{usuarios[codigo].get(campo)}')
                        novo_dado = input(f'Informe o novo dado do campo {campo} ou aperte "Enter" caso deseje manter o mesmo valor: ')
                        if novo_dado:
                            usuarios[codigo][campo] = novo_dado #no dict usuarios, ele pega o valor da variavel codigo e subistitui o valor no campo e novo_dado recebe esse novo valor
                        else:
                            ...
                    print(m.salvar_dados(usuarios, abrir_arquivo)) #faz a gravação do JSON
                except Exception as e:
                    print(f'Não foi possivel alterar os dados!.{e}')
                finally:
                    continue
            case '5':
                try:
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    codigo = int(input('Informe o código do usuário que deseja deletar: '))
                    nome_deletado = usuarios[codigo]['nome']
                    confirmacao = input(f'Deseja dele o usuário {nome_deletado}? Digite "SIM" para confirmar: ').upper()
                    if confirmacao == 'SIM':
                        del(usuarios[codigo])
                        print(m.salvar_dados(usuarios, abrir_arquivo))
                        print(f'Usuário {nome_deletado} deletado com sucesso!')
                    else:
                        print(f'Usuário {nome_deletado} não foi excluído!')
                except Exception as e:
                    print(f'Não foi possivel alterar os dados!.{e}')
                finally:
                    continue
            case _:
                print('Opção inválida!')
                continue
