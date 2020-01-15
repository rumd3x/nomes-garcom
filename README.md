# nomes-garcom

Coletânea de nomes de garçom, meu Workaholic!

![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/edmur/nomes-garcom.svg)
![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/edmur/nomes-garcom.svg)

## O Projeto

Este projeto existe. Não sabemos o porque.

### gencreds.py

Preencher com as suas credenciais da API do Twitter e executar para gerar o arquivo "creds.json".

### fetch.py

Utiliza as credentials acima, pra varrer a [conta do twitter NomesGarcom](https://twitter.com/NomesGarcom) e baixar todas as imagens pra pasta "images".

### processor.py

Trata as imagens da pasta images utilizando opencv e pytesseract para extrair o nome escrito na imagem em forma de texto, e salvar no arquivo "nomes.txt".

### server.py

Disponibiliza uma aplicação http, que quando acessada, retorna um dos nomes contidos no arquivo "nomes.txt" aleatóriamente.
