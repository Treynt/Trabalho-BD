from DAO.SessãoDAO import SessaoDAO
from DAO.SalaDAO import SalaDAO
from DAO.FilmeDAO import FilmeDAO
sessao = SessaoDAO()
listasessao = sessao.inicia()
sala = SalaDAO()
listasala = sala.inicia()
filme = FilmeDAO()
lista_filmes = filme.inicia()
def lista_filmes_cartaz():
    lista_cartaz = []
    for i in lista_filmes:
        for f in listasessao:
            if i.Codfilme == f.Id_filme:
                for j in listasala:
                    if f.Id_sala == j.cod_sala:
                        lista_cartaz.append("Filme: "+i.titulo +" Horario: "+f.horario+" Cadeiras Disponiveis: "+ str(f.capacidade)+" Sala:"+j.nome_sala )
    return lista_cartaz

z = lista_filmes_cartaz()
for i in z:
    print(i)