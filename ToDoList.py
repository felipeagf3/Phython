from tkinter import*  #Importa biblioteca tkiner
from tkinter import messagebox #importa messagebox

def AdicionarTarefa() :#função para adicionar tarefa ao list box quando botão for clicado
    ListboxTarefa.insert(END,ManipularTarefa.get())


def RemoverTarefa():#remove a tarefa da lista
    try:
        indice = ListboxTarefa.curselection()[0] #armazena na variável indice da tarefa selecionada
        ListboxTarefa.delete(indice)# deleta a tarefa pelo indice
    except IndexError: #é executado caso curselection não retorne nehum indice
        messagebox.showerror("Erro", "Tarefa Não Selecionada" ) #mensagem de erro caso nehuma tarefa seja selecionada

def ConcluirTarefa():#função para marcar como concluida a tarefa quando botão for acionado
    try:

        LtarefasConcluidas = Label(janela, text = ListboxTarefa.get(ANCHOR))#exibe as tarefas concluidas
        tarefas = ListboxTarefa.curselection()[0]#retorna o indice da tarefa selecionada
        ListboxTarefa.delete(tarefas)#remove a tarefa da lista
        LtarefasConcluidas.pack()#exibe o texto da tarefa

    except IndexError:#é executado caso nehuma tarefa seja selecionada
     messagebox.showerror ("Erro","Tarefa Não Selecionada")#mensagem de erro 

janela = Tk()# cria janela principal
janela.title("Gerenciador de Tarefas") #titulo da janela
janela.geometry("300x300") #dimensão da janela


ManipularTarefa = Entry(janela) #caixa de texto para digitar tarefa
ManipularTarefa.pack() #exibe a caixa de texto


BtnInserirTarefa = Button(janela,text="Adicionar Tarefa",command=AdicionarTarefa) #botão para inserir tarefa quando clicado
BtnInserirTarefa.pack() #exibe o botão 

ListboxTarefa = Listbox(janela, height=8) #caixa que armazena as tarefas
ListboxTarefa.pack() #exibe e posiciona as tarefas


BtnRemovertarefa = Button(janela,text="Remover Tarefa",command=RemoverTarefa) #botão remover tarefa selecionada
BtnRemovertarefa.pack()


BtnConcluirTarefa = Button(janela,text="Concluir Tarefa",command=ConcluirTarefa) #botão que marca e remove da lista tarefa selecionadA
BtnConcluirTarefa.pack() #posiciona e exibe o botão
concluidas = Label(janela, text="Tarefas Concluidas")
concluidas.pack()

janela.mainloop() #mantém a janela aberta até que seja fechada

