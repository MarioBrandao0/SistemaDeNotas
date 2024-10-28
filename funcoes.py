import os
from time import sleep
import pandas as pd
import numpy as np
from openpyxl.styles import PatternFill

def registrar_nota():
    os.system('clear')
    nome = input('Digite o nome do aluno: ')
    alunos = {}
    notas = []
    media = 0
    while True:
        nota = float(input('Digite a nota do aluno[-1 --> Sair]: '))
        if nota < 0:
            break
        media += nota
    notas.append(media)

    alunos['nome'] = nome
    alunos['notas'] = notas
    print(alunos)
    return alunos

def media(alunos):
    #Colocar notas em uma lista para colocar na tabela excel
    os.system('clear')
    alunos_aprovados = []
    alunos_recuperacao = []
    alunos_reprovados = []
    for aluno in alunos:
        for nota in aluno['notas']:
            if 3 < nota < 6:
                alunos_recuperacao.append(f'{aluno['nome']}')
                
                
            elif nota >= 7:
                alunos_aprovados.append(f'{aluno['nome']}')
        
        
            else:
                alunos_reprovados.append(f'{aluno['nome']} ')
                        
    print(alunos_aprovados, alunos_recuperacao, alunos_reprovados )
    #exportar_excel(aprovados=alunos_aprovados, recuperacao=alunos_recuperacao ,reprovados=alunos_reprovados)

def atualizar_nota():
    #Desenvolver isso aqui
    pass

def exportar_excel(aprovados, recuperacao, reprovados):
    #colocar as notas inves das situações
    dados_aprovados = {
        'Nome': aprovados,
        'Situação': ['Aprovado'] * len(aprovados)
    }
    dados_recuperacao = {
        'Nome': recuperacao,
        'Situação': 'Recuperação' * len(recuperacao)
    }
    dados_reprovados = {
        'Nome': reprovados,
        'Situação': 'Reprovados' * len(reprovados)
    }

    dataframe = pd.DataFrame(dados_aprovados)
    with pd.ExcelWriter('Alunos.xlsx', engine='openpyxl') as writer:
        dataframe.to_excel(writer, sheet_name='Alunos', index=False)

        workbook = writer.book
        worksheet = writer.sheets['Alunos']

        verde = PatternFill(start_color='00FF00', end_color='00FF00', fill_type='solid')
        amarelo = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')
        vermelho = PatternFill(start_color='FF0000', end_color='FF0000', fill_type='solid')

        for row in range(2, len(dataframe) + 2):
            status = worksheet.cell(row=row, column=2).value
            if status == 'Aprovado':
                worksheet.cell(row=row, column=2).fill = verde
            elif status == 'Recuperação':
                worksheet.cell(row=row, column=2).fill = amarelo
            elif status == 'Reprovado':
                worksheet.cell(row=row, column=2).fill = vermelho
    print(dataframe)    
