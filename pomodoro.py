#POMODORO CLI

#1 - Iniciar Pomodoro
#2 - Configurações
#3 - Histórico
#4 - Estatísticas
#5 - Sair


#Arrumar def.pomodoro()

import time
import json
import os
import datetime

#FUNÇÕES

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def data_e_hora_atual():
    data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    return data

def pomodoro():
    tempo = 1#25
    print('Iniciando Pomodoro...')
    time.sleep(1)
    print(f'Tempo de foco: {tempo} minutos')
    time.sleep(1)
    print(f'Ciclo atual: {ciclo}')
    time.sleep(2)
    limpar_tela()
    while True:
        minuto = tempo
        while minuto != 0:
            print(f"{minuto:02d}:00")
            time.sleep(1)
            limpar_tela()
            segundo = 59
            minuto-=1
            while segundo !=0:
                print(f"{minuto:02d}:{segundo:02d}")
                time.sleep(1)
                limpar_tela()
                segundo-=1
            global tempo_foco
            tempo_foco += 25
        except:
                print("Digite uma opção correta!")
                time.sleep(3)
                limpar_tela()


        while True:
            try:
                chc = int(input("""
                        1 - Iniciar pausa
                        2 - Voltar ao menu
                        Escolha algum: """))
                if chc == 1:
                    limpar_tela()
                    input("De enter para começar a pausa")
                    limpar_tela()
                    while True:
                        tempo = 1#5
                        minuto = tempo
                        while minuto != 0:
                            print(f"{minuto:02d}:00")
                            time.sleep(1)
                            limpar_tela()
                            segundo = 59
                            minuto-=1
                            while segundo !=0:
                                print(f"{minuto:02d}:{segundo:02d}")
                                time.sleep(1)
                                limpar_tela()
                                segundo-=1
                        global tempo_pausa
                        tempo_pausa += 5
                
                if chc == 2:
                    print("Saindo...")
                    time.sleep(2)
                    break
            except:
                print("Digite uma opção correta!")
                time.sleep(3)
                limpar_tela()
                
            

    print("Pomodoro concluído!")

#ESTRUTURA DE DADOS

lista_de_tarefas = list()


while True:
    try:   
        chc = int(input("""
    -----------------------
    |1 - Iniciar Pomodoro | 
    |---------------------|
    |2 - Configurações    |
    |---------------------|
    |3 - Histórico        |
    |---------------------|
    |4 - Estatísticas     |
    |---------------------|
    |5 - Sair             |
    -----------------------                
    Selecione algum: """))
        
        if chc == 1:
            limpar_tela()
            tarefa = dict()
            ciclo = 1
            tempo_pausa = 0
            tempo_foco = 0
            while True:
                nome_tarefa = input('Qual tarefa você vai focar?')
                if len(nome_tarefa.strip()) > 0 :
                    #tarefas.append([nome_tarefa, False, data_e_hora_atual()])
                    pomodoro()
                    
                    tarefa = {
                        'nome': nome_tarefa,
                        'ciclo': ciclo,
                        'tempo_foco': tempo_foco,
                        'tempo_pausa': tempo_pausa
                        }
                    lista_de_tarefas.append(tarefa)
                    tarefa.clear()
                    break
                else:
                    print("Digite algo para adicionar!")
                    limpar_tela()
                limpar_tela()

        if chc == 2:
            print()


        if chc == 3:
            print()



        if chc == 4:
            print()




        if chc == 5:
            print()









    except:
        print("Digite uma opção correta!")
        time.sleep(3)
        limpar_tela()