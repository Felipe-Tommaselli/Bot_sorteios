# Bot_sorteios
Programa de automatização em python com o objetivo de realizar comentarios em plataformas de sorteios (como redes sociais), evitando a utilziação de webdrivers e bibliotecas como a Selenium, a qual pode deixar rastros para a plataforma. 
O código contempla uma lista de palavras que podem ser alteradas dependendo do sorteio. Além disso, vale ressaltar que o código digitara as palavras da lista de forma aleatória, bem como o emoji que poderá acompanhar o texto. 

## Instalação
Simples assim. Apenas é necessario ter o Google Chrome e o python instalado, alem disso o chromeriver.exe deixado no repositório tambem deve ser executado. 
As bibliotecas usadas podem ser instaladas pelos comandos no temrinal, ele pode ser acessado pesquisando prompt de comando na barra de pesquisa do windows:

`pip install pyautogui`

`pip install datetime`

O link a seguir pode ser util para esclarecimentos acerca do assunto:
https://www.treinaweb.com.br/blog/gerenciando-pacotes-em-projetos-python-com-o-pip/

**Não se preocupe! Não temos acesso aos seus dados, eles ficam salvos no seu computador**

## Uso do bot
É necessario apenas rodar o script em python (lembre que seu computador deve ter o python 3 instalado para isso). Para isso, com o arquivo ja adicionado ao seu computador, apenas sera necessario clicar em seu icone ou através do prompt de comando. https://cursos.alura.com.br/forum/topico-executar-o-programa-em-python3-pelo-prompt-de-comando-83408#

O programa fara um questionamento por meio do terminal que ele esta rodando, nesse momento sera necessario adicionar o modo em que é esperado que o progrmaa funcione. Após isso, em alguns segundos é **imprescindivel** que o cursor do mouse seja posicionado no campo em que sera realizado os comentarios.
O programa então enviara aleatoriamente atraves de algoritmos de randomização os comentarios por tempo indeterminado. Caso deseje intorromper o funcionamento, recomenda-se que o programa seja interrompido selecionando o terminal (onde foi feito a pergunta incial) e aplicando o comando *CTRL + C*. Dessa forma, o bot sera interrompido, teoricamente, sem problemas. Caso haja, algum incoveniente, apenas seria necessario fechar o terminal para interromper o andamento do programa definitivamente.

## Para desenvolvedores:
- O código em Python esta no repositório em bot_sorteios_code.py;
- As bibliotecas de python necessárias são a **random**, **re**, **time**, **pyautogui** e **datetime**. Use o pip install para a instalação das duas ultimas;
- O codigo foi estruturado em funções independentes e um looping principal, dessa forma é possivel identificar em que momento o bot esta exibindo algum erro de forma mais organizada e analitica;

### **Disclaimer**
Esse Bot foi feito com fins de treinamento e aprendizado, seu uso indevido pode ferir as diretrizes de comunidade da plataforma utilizada. Para isso, consulte anteriormente as restrições da plataforma e do sorteio com relação a softwares de automatização.