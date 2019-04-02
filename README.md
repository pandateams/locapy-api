#### Fluxo de Desenvolvimento da equipe

* **master** - Branch utilizado somente para funcionalidades já testadas e aprovadas pelo cliente
* **develop** - Branch que consiste no desenvolvimento atual da equipe

* **features** - Demais funcionalidades que estão sendo desenvolvidas


![alt text](https://www.bitbull.it/blog/git-flow-come-funziona/gitflow-1.png "GitFlow")
__fonte__: https://www.bitbull.it/blog/git-flow-come-funziona/gitflow-1.png

**SEMPRE**:
* Para novas funcionalidades utilize: feature/nome_da_func
* Para melhorias no codigo: bugfix/nome_da_correcao

---




#### Trabalhe na branch correta

Para visualizar todas as branches:
```sh
    git branch -a
```


Utilize uma branch já existente:
```sh
    git checkout <nome_da_branch>
```

Ou crie uma nova para a sua funcionalidade:
```sh
    git checkout -b <nome_da_branch>

    <Exemplo>
    git checkout -b DBconnection
```

Certifique-se de que sua branch está atualizada:
```sh
    git pull origin <nome_da_branch_mais_att>

    <Exemplo>
    git pull origin develop
```
---


#### Adicione suas credenciais
Para trabalhar com o projeto, crie um arquivo chamado .env na raiz do diretorio, e
adicione as credenciais fornecidas pela **equipe de desenvolvimento**.


---
#### Rodando o projeto com Docker Compose

Docker é uma tecnologia que fornece containers que isolam processos, com a ajuda do Docker Compose é possível orquestrar containers e subir aplicações complexas com poucos comandos.

Instalação do Docker no Windows: [https://docs.docker.com/docker-for-windows/install/](https://docs.docker.com/docker-for-windows/install/)

Instalação do Docker Compose no Linux: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

**Iniciando o projeto**

Atualize o repositorio local
```sh
    git pull origin develop
```
Para iniciar o projeto:

```sh
    docker-compose up
```
