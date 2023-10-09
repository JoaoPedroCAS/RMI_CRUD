# README - Sistema de Pokedex com Pyro4

## Visão Geral

Este repositório contém dois scripts Python relacionados a um sistema de Pokedex utilizando a biblioteca Pyro4. Um dos scripts é um servidor que gerencia uma Pokedex, enquanto o outro é um cliente que permite interagir com o servidor para criar, ler, atualizar e excluir informações sobre Pokémon na Pokedex.

## Conteúdo

- [Requisitos](#requisitos)
- [Configuração](#configuração)
- [Instruções de Uso](#instruções-de-uso)
- [Explicação dos Códigos](#explicação-dos-códigos)
- [Exemplo de Uso](#exemplo-de-uso)
- [Considerações Finais](#considerações-finais)

## Requisitos

Certifique-se de que você tenha o Python instalado em seu sistema. Além disso, instale a biblioteca Pyro4:

```
pip install Pyro4
```

## Configuração

1. Clone este repositório ou baixe os arquivos `server.py` e `client.py`.

2. Abra um terminal e navegue até a pasta onde os arquivos estão localizados.

## Instruções de Uso

### Executando o Servidor

1. Execute o servidor da Pokedex com o seguinte comando:

```
python server.py
```

O servidor estará pronto para receber solicitações dos clientes.

### Executando o Cliente

1. Execute o cliente da Pokedex com o seguinte comando:

```
python client.py
```

O cliente exibirá um menu interativo com várias opções para interagir com a Pokedex.

## Explicação dos Códigos

### `server.py`

O arquivo `server.py` contém o código do servidor Pyro4 que gerencia a Pokedex. Ele define uma classe `PokedexServer` que contém métodos para criar, ler, atualizar e excluir Pokémon na Pokedex. O servidor é configurado para expor esses métodos via Pyro4 e é iniciado em um loop para aguardar conexões de clientes.

### `client.py`

O arquivo `client.py` é um cliente Pyro4 que permite ao usuário interagir com o servidor da Pokedex. Ele exibe um menu com opções para adicionar, ler, atualizar e excluir Pokémon na Pokedex. O cliente se conecta ao servidor usando a URI do servidor Pyro4 e envia solicitações com base nas escolhas do usuário.

## Exemplo de Uso

Aqui está um exemplo de como usar o sistema de Pokedex com os códigos fornecidos:

1. Execute o servidor com `python server.py`.

2. Execute o cliente com `python client.py`.

3. No cliente, você verá um menu interativo. Você pode escolher entre as opções do menu para adicionar, ler, atualizar ou excluir Pokémon na Pokedex.

4. Siga as instruções do cliente para realizar as operações desejadas.

## Considerações Finais

Este é um exemplo simples de um sistema de Pokedex utilizando a biblioteca Pyro4. Você pode expandir e aprimorar este sistema adicionando mais recursos, como persistência de dados em um banco de dados, validação de entrada do usuário e autenticação de clientes para maior segurança.

Sinta-se à vontade para explorar e adaptar os códigos de acordo com suas necessidades e objetivos. Se você tiver alguma dúvida ou precisar de ajuda adicional, não hesite em entrar em contato ou procurar recursos adicionais sobre Pyro4 e Python.
