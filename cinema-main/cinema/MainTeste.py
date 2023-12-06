from DAO.ClienteDAO import ClienteDAO
from DAO.ComboDAO import ComboDAO
from DAO.FilmeDAO import FilmeDAO
from DAO.GeneroDAO import GeneroDAO
from DAO.IngressoDAO import IngressoDAO
from DAO.FilmeGeneroDAO import FilmeGeneroDAO
from DAO.SessãoDAO import SessaoDAO
from DAO.SalaDAO import SalaDAO
from DAO.AssentosDAO import AssentosDAO
from Cliente import Cliente
from classes import Sessão
from classes import Filme
from classes import Genero
import sys

cliente = ClienteDAO()
lista_clientes = cliente.inicia()
filme = FilmeDAO()
lista_filmes = filme.inicia()
genero = GeneroDAO()
lista_generos = genero.inicia()
combo = ComboDAO()
lista_combos = combo.inicia()
ingresso = IngressoDAO()
lista_ingresso = ingresso.inicia()
sessao = SessaoDAO()
lista_sessoes = sessao.inicia()
relacao = FilmeGeneroDAO()
lista_relaçoes = relacao.inicia()
sala = SalaDAO()
lista_salas = sala.inicia()

usuario = 0

def verificar(resposta):
    if resposta == "N":
        return False
    elif resposta == "S":
        return True
    else:
        resposta = input("Por favor, retorne uma saída válida (S/N): ")
        verificar(resposta)


def menu():
    print('')
    print("-----------------------------MENU-----------------------------")
    r = int(input("1 (Login), 2 (Cadastro), 3 (Mudar Senha), 4 (Finalizar) \n Opção:"))
    if r == 1:
        email = input("E-mail: ")
        senha = input("Senha: ")
        login(email, senha)
        #Vai pra tela principal
    elif r == 2:
        cadastrarCliente()
        #volta Pro menu
    elif r == 3:
        mudarSenha()
        #Volta pro menu

#Funções para o menu
#VERSION PEDRO MODIFICADA
def login(email, senha):
    for i in lista_clientes:
        if email == i.emails and senha == i.senhas:
            print("Login realizado!")
            usuario = Cliente(i.Id, i.nome, i.emails, i.senhas, i.sobrenomes, i.idades)
            telaprincipal()

    print("Usuário não encontrado, tente novamente!")
    r = input("Você deseja tentar novamente (S) ou sair (N)? ").upper()
    r = verificar(r)
    if r == True:
        print("Login ou Senha incorretos, tente novamente")
        email = input("E-mail: ")
        senha = input("Senha: ")
        login(email,senha)
    else:
        menu()

def confirmarSenhasIguais(senha, senConfirmar):
    if senha == senConfirmar:
        return senha
    else:
        print("Tentne Novamente...")
        senha = input("Sua senha: ")
        senConfirmar = input("Confirma senha: ")
        confirmarSenhasIguais(senha, senConfirmar)


def cadastrarCliente():
    print("Tela de Cadastro:")
    nome = input("Primeiro Nome: ")
    sobrenome = input("Sobrenome Completo: ")
    email = input("Seu E-mail: ")
    idade = input("Sua idade: ")
    senha = input("Sua senha: ")
    senhaConfirmar = input("Confirme sua senha: ")
    senha = confirmarSenhasIguais(senha, senhaConfirmar)
    idade = int(idade)
    cliente.inserir_cliente(nome, email, senha, sobrenome, idade)
    menu()


def mudarSenha():
    print("Recuperar senha")
    email = input("Seu E-mail de Usuário: ")
    senha = input("Nova Senha: ")
    senhaConfirmar = input("Confirmar Senha: ")
    senha = confirmarSenhasIguais(senha, senhaConfirmar)
    cliente.mudar_senha(senha, email)
    menu()

def telaprincipal():
    print("Seja Bem-Vindo ao Menu Principal!" )
    # Printar lista de filmes com todas as sessões disponiveis
    print('')
    print("------------------------------ Escolha o que você deseja fazer: ------------------------------")
    r = int(input(" 1 (Escolher Filme), 2 (Procurar Filme Por Gênero), 3 (Ver Seus Ingressos), 4 (Sair)\n Opção:"))
    #1 escolher filme
    if r == 1:
        escolherFilme()
    #2 Procurar por genero
    elif r == 2:
        filme = input("Qual o gênero de filme deseja?: ")
        retornarGenerosDoFilme(filme)
    #3 ver ingressos
    elif r == 3:
        print("Falta adicionar ver ingressos")
        telaprincipal()
    elif r == 4:
        menu()
    #deslogar que é voltar para o menu principal

def comprarIngresso(pessoa, sessao):
    valorIngresso = 25
    capacidadeSala = 20
    lotacao = capacidadeSala - 1
    user = pessoa.Id
    sessao = sessao.sessao_Id


    IngressoDAO().inserir_ingresso(valorIngresso, user, sessao)
    SessaoDAO().alterar_capacidade(lotacao, sessao)
    

def procurarFilme(nomeFilme):
    for f in lista_filmes:
        if nomeFilme == f.titulo:
            r = input("Esse filme está disponível, deseja comprar o ingresso (S/N)? : ")
            if verificar(r):
                comprarIngresso()
                print("Compra efetuada com sucesso!!")
                telaprincipal()
            else:
                print("Ok, retornando a tela principal!")
                telaprincipal()
    print("Lamento, filme não encontrado. Deseja procurar outro (S) ou retornar ao Menu principal (N)?")

            #falta gets and sets na classe titulo

def procurarSessaocomHorario(horario):
    for s in lista_sessoes:
        if horario == s.horario:
            sessao = Sessão(s.sessao_Id, s.capacidade, s.horario)
            return sessao
    print("Nenhuma sessão encontrada, tente novamente ou volte ao Menu")
    sessaoHorario = int(input())
    procurarSessaocomHorario(sessaoHorario)

def escolherFilme():
    print('')
    print("--------Escolha o filme com sessão e quantos assentos deseja:-------- ")
    escolhafilme = input("Seu filme: ")
    #ajeitar procurarFilmes e adicionar entidade filme
    #procurarFilme
    sessao = input("Horário da sua sessão: ")
    #ajeitar e criar entidade sessao
    #procurarSessaocomHorario()
    qtdIngressos = input("Quantidade de ingressos:")
    valorTotal = qtdIngressos * 12
    metodoPagamento()
    print("Ótima compra e aproveite o filme!!")
    telaprincipal()

def retornarGenerosDoFilme(filme):
    listaId = []
    listagenero = []
    for i in lista_filmes:
        if i.titulo == filme:
            filmeP = Filme(i.Codfilme, i.titulo, i.classifcacao)
            break
    for i in lista_relaçoes:
        if filmeP.Codfilme == i.Idfilme:
            listaId.append(i.Idgenero)
    for i in lista_generos:
        for f in listaId:
            if f == i.IdGenero:
                listagenero.append(i.NomeGenero)
    return listagenero

def generosDeFilme(genero):
    listaId = []
    listafilme = []
    for i in lista_generos:
        if i.NomeGenero == genero:
            generoP = Genero(i.IdGenero, i.NomeGenero)
            break
    for i in lista_relaçoes:
        if generoP.IdGenero == i.Idgenero:
            listaId.append(i.Idfilme)
    for i in lista_filmes:
        for f in listaId:
            if f == i.Codfilme:
                listafilme.append(i.titulo)
    return listafilme


def metodoPagamento():
    r = int(input("Debito 1 - NaCaixa 2"))
    if(r == 1):
        input("Nome no cartão: ")
        input("Número do cartão: ")
    elif(r == 2):
        print("Compra Efetuada!")
    else:
        print("Digitação errada, escolha novamente.")
        metodoPagamento()


def lista_filmes_cartaz():
    lista_cartaz = []
    for i in lista_filmes:
        for f in lista_sessoes:
            if i.Codfilme == f.Id_filme:
                for j in lista_salas:
                    if f.Id_sala == j.cod_sala:
                        lista_cartaz.append("Filme: "+i.titulo +" Horario: "+f.horario+" Cadeiras Disponiveis: "+ str(f.capacidade)+" Sala:"+j.nome_sala )
    return lista_cartaz



Gatilho = True
while Gatilho:
    print("Bem-Vindo!")
    #Perguntar qual opção
    r = input("Deseja ir para Menu(S) ou Deslogar(N)?").upper()
    r = verificar(r)
    if r == True:
        menu()
    else:
        print("Até logo, foi um prazer! :)")
        Gatilho = False