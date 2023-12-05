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
        #print("Por favo, retorne uma saída válida(S/N): ")
        resposta = input("Por favo, retorne uma saída válida(S/N): ")
        verificar(resposta)

def menu():
    r = input("MENU 1 2 3 4: ")
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
            print("login realizado!")
            usuario = Cliente(i.Id, i.nome, i.emails, i.senhas, i.sobrenomes, i.idades)
            telaprincipal()

    print("Usuário não encontrado, tente novamente!")
    r = input("Você deseja tentar novamente(S) ou sair?(N)")
    r = verificar(r)
    if r == True:
        print("login ou senha incorretos, tente novamente")
        email = input("E-mail: ")
        senha = input("Senha: ")
        login(email,senha)
    else:
        menu()

def confirmarSenhasIguais(senha, senConfirmar):
    if senha == senConfirmar:
        return senha
    else:
        print("Novamente...")
        senha = input("Sua senha: ")
        senConfirmar = input("Confirma senha: ")
        confirmarSenhasIguais(senha, senConfirmar)


def cadastrarCliente():
    print("Menu cadastrar:")
    nome = input("Primeiro nome: ")
    sobrenome = input("Sobrenome completo: ")
    email = input("Seu email: ")
    idade = int(input("Sua idade: "))
    senha = input("Sua senha: ")
    senhaConfirmar = input("Confirme sua senha: ")
    senha = confirmarSenhasIguais(senha, senhaConfirmar)

    ClienteDAO.inserir_cliente(nome, email, senha, sobrenome, idade)
    menu()

def mudarSenha():
    print("Recupere senha ")
    id    = int(input("Seu ID de usuário: "))
    senha = input("Senha nova: ")
    senhaConfirmar = input("Confirmar senha: ")
    senha = confirmarSenhasIguais(senha, senhaConfirmar)
    ClienteDAO.mudar_senha(id, senha)
    menu()

def telaprincipal():
    print("Bem-Vindo ao menu principal!")
    # Printar lista de filmes com todas as sessões disponiveis
    r = int(input("Escolha o que você quer fazer/ver 1/2/3/4"))
    #1 escolher filme
    if r == 1:
        escolherFilme()
    #2 Procurar por genero
    elif r == 2:
        filme = input("Esse filme tem esses generos: ")
        retornarGenerosDoFilme(filme)
    #3 ver ingressos
    elif r == 3:
        print("Falta adicionar ver ingressos")
    elif r == 4:
        menu()
    #deslogar que é voltar para o menu principal

def comprarIngresso():
    valorIngresso = 25
    usuario = Cliente.id
    sessao = Sessão.Id

    IngressoDAO().inserir_ingresso(valorIngresso, usuario, sessao)

def procurarFilme(nomeFilme):
    for f in lista_filmes:
        if nomeFilme == f.titulo:
            r = input("Esse filme existe, deseja comprar(S/N): ")
            if verificar(r):
                comprarIngresso()#comprar ingresso
                print("Compra efetuada com sucesso!!")
                telaprincipal()
            else:
                print("Ok, retornando a tela principal!")
                telaprincipal()
    print("Lamento, filme não encontrado, deseja procurar outro ou retorna(S) ao menu principal(N)?")

            #falta gets and sets na classe titulo

def procurarSessaocomHorario(horario):
    for s in lista_sessoes:
        if horario == s.horario:
            sessao = Sessão(s.sessao_Id, s.capacidade, s.horario)
            return sessao
    print("Nenhum sessão encontrada, tente novamente ou saia")
    sessaoHorario = int(input())
    procurarSessaocomHorario(sessaoHorario)

def escolherFilme():
    print("Escolha o filme com sessão e quantos assentos: ")
    escolhafilme = input("Seu filme: ")
    #ajeitar procurarFilmes e adicionar entidade filme
    #procurarFilme
    sessao = input("Horário de sua sessão: ")
    #ajeitar e criar entidade sessao
    #procurarSessaocomHorario()
    qtdIngressos = input("Quantidade de ingresso:")
    valorTotal = qtdIngressos * 12
    metodoPagamento()
    print("Ótima compra! E bom filme.")
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
    r = input("Debito 1 - NaCaixa 2")
    if(r == 1):
        input("Nome no cartão: ")
        input("Número do cartão: ")
    elif(r == 2):
        print("Boa compra!!")
    else:
        print("Digitação errada, escolha novamente.")
        metodoPagamento()



Gatilho = True
while Gatilho:
    print("Tela de boa vindas")
    #Perguntar qual opção
    r = input("Ir para Menu(S)? Ou deslogar(N)").upper()
    r = verificar(r)
    if r == True:
        menu()
    else:
        print("Tchau, foi um prazer hihihi")
        Gatilho = False
#lista filmes sessões e salas
def lista_filmes_cartaz():
    lista_cartaz = []
    for i in lista_filmes:
        for f in lista_sessoes:
            if i.Codfilme == f.Id_filme:
                for j in lista_salas:
                    if f.Id_sala == j.cod_sala:
                        lista_cartaz.append("Filme: "+i.titulo +" Horario: "+f.horario+" Cadeiras Disponiveis: "+ str(f.capacidade)+" Sala:"+j.nome_sala )
    return lista_cartaz




