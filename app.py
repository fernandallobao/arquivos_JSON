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
                    usuario = {}
                    campos = ('nome', 'cpf', 'email', 'profissao')
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    usuario['codigo'] = len(usuarios) #verfifica a quantidade de usuários e gera um novo código para o novo usuario
                    for campo in campos:
                        usuario[campo] = input(f'Informe o campo {campo.capitalize()}:')
                    usuarios.append(usuario)
                    print(m.salvar_dados(usuarios, abrir_arquivo))
                except Exception as e:
                    print(f'Não foi possível realizar a operação.{e}')
                finally:
                    continue
            case _:
                print('Opção inválida!')
                continue
