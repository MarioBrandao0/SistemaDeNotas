from time import sleep
import os
import funcoes as fc
def main():
    os.system('clear')
    guard_alunos = []
    while True:
        print('-'*40)
        escolha = int(input('1-Registrar nota/2-calcular média/3-Sair: '))    
        
        if escolha == 1:
            alunos = fc.registrar_nota()

            guard_alunos.append(alunos)

        elif escolha == 2:
            if not guard_alunos:
                print('Nehum aluno registrado. Registre um aluno primeiro')
            
            else:
                aprovados, recuperacao, reprovados = fc.media(alunos=guard_alunos)
                fc.exportar_excel(aprovados=aprovados, recuperacao= recuperacao, reprovados=reprovados)

        elif escolha == 3:
            print('Obrigado por usar o prgrama de calcular média')
            sleep(1.0)
            
            print('Até mais')
            sleep(1.0)
            
            os.system('clear')
            break


if __name__ == '__main__':
    main()
