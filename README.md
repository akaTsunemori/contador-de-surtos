
<h1 align="center">
  <br>
  <a href="https://github.com/akaTsunemori/contador-de-surtos"><img src="https://i.imgur.com/H1zg9gH.jpg" alt="Contador de Surtos" width="200"></a>
  <br>
  Contador de Surtos
  <br>
</h1>

<h4 align="center">Um bot para ser usado no <a href="https://discord.com/" target="_blank">Discord</a>, com intuito de contar surtos dos membros do servidor.</h4>

<p align="center">
  <a href="#funcionalidades">Funcionalidades</a> •
  <a href="#to-do-list">To-Do List</a> •
  <a href="#instalação">Instalação</a> •
  <a href="#permissões">Permissões</a> •
  <a href="#como-usar">Como usar</a> •
  <a href="#créditos">Créditos</a> •
  <a href="#licença">Licença</a>
</p>

![screenshot](https://i.imgur.com/ZZFV6Ys.png)

## Funcionalidades

* Contagem diária
  - Todos os dias, em um horário determinado, uma mensagem é enviada com estatísticas totais e o tempo desde o último surto.
* Histórico de surtos
  - Armazenamento persistente através de JSON permite que um histórico com todos os surtos e suas respectivas datas sejam sempre salvos.
* Isolado entre servidores
  - O bot está em mais de 1 servidor? Sem problemas, a database é isolada entre servidores, permitindo surtos diferentes em servidores diferentes.
* Remover surtos
  - Cometeu um erro gramatical em um surto que acabou de ser adicionado? Basta removê-lo e o adicionar novamente.
* Habilidade de resetar
  - Quer começar tudo do zero? Basta usar o comando de reset.
* Interface amigável
  - Interface separada em páginas para históricos de surtos, melhorando sua legibilidade, principalmente em dispositivos móveis.

## To-Do List

Listas de funcionalidades completas e incompletas:

- [x] Armazenamento persistente
- [x] Novo surto
- [x] Lista de surtos
- [x] Estatísticas de surtos
- [x] Resetar bot
- [x] Remover surto específico
- [x] Comando de ajuda
- [x] Gifs divertidos para acompanhar os comandos

## Instalação

Para clonar e executar esse bot, será necessário que as tecnologias [Git](https://git-scm.com), [Python](https://www.python.org/) e [pip](https://pip.pypa.io/en/stable/index.html) estejam instaladas em seu computador. Em um terminal de comandos:

```bash
# Clonar este repositório
$ git clone https://github.com/akaTsunemori/contador-de-surtos

# Mudar o diretório corrente ao do repositório
$ cd contador-de-surtos

# Instalar dependências
$ pip install -r requirements.txt

# Criar arquivo token.env e, nele, deve-se informar uma variável TOKEN=XXXXX,
# onde XXXXX é o token referente a um bot já criado.
$ touch token.env
$ echo "TOKEN=XXXXX" >> token.env

# Execute a aplicação
$ python3 main.py
```

> **Nota**
> As instruções acima foram direcionadas a um ambiente Linux.

## Permissões

O bot exige as seguintes permissões para funcionar corretamente:
* Scopes
  - bot
* Bot permissions
  - Manage channels
  - Manage roles
  - Send messages
  - Send messages in Threads
  - Embed links
  - Read message history
* Intents
  - Default
  - Message content intent

## Como usar

Uma vez que o bot esteja em execução, o comando `>help` fornecerá instruções sobre cada comando disponível pelo bot.

## Créditos

Esse software usa os seguintes pacotes de código aberto:

- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [pytz](https://pythonhosted.org/pytz/)

## Licença

GNU GENERAL PUBLIC LICENSE<br>
Version 2, June 1991

---

> GitHub [@akaTsunemori](https://github.com/akaTsunemori)

