# Desert Gun - Relatório do projeto - Equipe 3

Relatório de desenvolvimento do jogo Desert Gun feito para a disciplina de Introdução a Programação do curso de Ciências da Computação do CIn/UFPE.

## Índice
- [1. Equipe](#equipe)
    - [1.1 Desenvolvido por](#equipe)
    - [1.2 Divisão de tarefas](#divisao)
- [2. Ideação e Design](#ideacao)
- [3. Bibliotecas Utilizadas](#bibliotecas)
- [4. Organização do código](#organizacao)
- [5. Conceitos aprendidos na disciplina](#conceitos)
- [6. Desafios enfrentados](#desafios)
- [7. Capturas de tela](#capturas)
- [8. Video de demonstração](#demo)
- [9. Como instalar](#como-instalar)

<a id="equipe"></a>
## Equipe

### Desenvolvido por

<table>
  <tr>
<td align="center"><a href="https://www.linkedin.com/in/rencab/"><img src="https://i.imgur.com/UqrnL0zs.jpg" width="100px;" alt=""/><br /><sub><b>Renato Cabral</b></sub></a><br/></td>

<td align="center"><a href="https://www.linkedin.com/in/thalesvgfraga/"><img src="https://i.imgur.com/K39AuNm.jpeg" width="100px;" alt=""/><br /><sub><b>Thales Fraga</b></sub></a><br/></td>

<td align="center"><a href="https://github.com/caionsantos"><img src="https://i.imgur.com/pLDSE9L.jpg" width="100px;" alt=""/><br /><sub><b>Caio Santos</b></sub></a><br/></td>

<td align="center"><a href="https://www.linkedin.com/in/rinaldo-da-silva-bento-júnior-416a15201/"><img src="https://i.imgur.com/EYin5ui.jpeg" width="100px;" alt=""/><br /><sub><b>Rinaldo Júnior</b></sub></a><br/>

<td align="center"><a href="https://github.com/ham5"><img src="https://avatars.githubusercontent.com/u/125143251?v=4" width="100px;" alt=""/><br /><sub><b>Heitor Machado</b></sub></a><br/>
</td>
</tr>
 </table>

<a id="divisao"></a>
### Divisão de tarefas
- <strong>Renato Cabral</strong>: Implementação das mecânicas de tiro do jogador, organização e legibilidade do código
- <strong>Thales Fraga</strong>: Correção de bugs, organização do time, ideação (sugestão do tema central) e relatório
- <strong>Caio Santos</strong>: Criação dos coletáveis, movimentação do personagem, dos inimigos e sua IA (disparo/movimento), da câmera, do sistema de geração de mapa, mecânica de ondas, sistema de HP e sede e da apresentação
- <strong>Rinaldo Júnior</strong>: Escolha e criação de artes, implementação de animações para jogador e inimigo, colisão entre as entidades, visuais, movimentação e correção de bugs 
- <strong>Heitor Machado</strong>: Implementação da mecânica de drops dinâmicos e sua coleta, ideação 

<a id="ideacao"></a>
## Ideação e design

O processo de ideação e design em grupo para o nosso projeto de jogo teve início com uma abordagem colaborativa, visando criar uma experiência única e cativante para os jogadores. Abaixo, descreveremos em detalhes as etapas desse processo.

<strong>1. Votação para Escolha do Estilo de Jogo</strong>

Para dar início ao processo criativo, realizamos uma votação entre os membros da equipe para escolher o estilo de jogo que gostaríamos de desenvolver. Após uma análise cuidadosa das opções disponíveis, optamos por criar um jogo do estilo "bullet hell". Esse gênero desafiador e cheio de ação foi escolhido por sua capacidade de proporcionar uma experiência intensa e empolgante aos jogadores.

<strong>2. Brainwriting Colaborativo</strong>

Para gerar ideias e conceitos inovadores para o jogo, implementamos uma técnica chamada "brainwriting". Cada membro da equipe recebeu um bloco de anotações e teve um período de 3 minutos para registrar suas ideias relacionadas ao jogo. Após esse tempo, passamos o bloco de anotações para a direita, permitindo que o próximo colega de equipe adicionasse suas próprias contribuições durante mais 3 minutos. Esse processo de passagem de blocos continuou até que todos os membros da equipe tivessem a oportunidade de contribuir. Esse método colaborativo resultou em uma riqueza de ideias e conceitos para nosso jogo.

<strong>3. Votação para Seleção do Tema</strong>

Com um grande número de ideias geradas no processo de brainwriting, realizamos uma votação para escolher o tema que mais instigasse, inovasse, fosse belo e de fácil desenvolvimento. Após cuidadosa deliberação, o tema vencedor foi escolhido: "Você está em um deserto, mas sua única arma é o cuspe, e você precisa pegar água que é dropada pelos inimigos". Esse tema prometia desafios únicos e uma experiência de jogo intrigante que atendia aos critérios estabelecidos.

<strong>4. Desenvolvimento de Artes e Recursos Visuais</strong>

Com o tema definido, começamos a desenvolver as artes e recursos visuais para o jogo. Alguns dos elementos visuais foram criados internamente pela equipe. Além disso, também utilizamos recursos visuais de fontes da internet que não infringissem direitos autorais, garantindo que todas as imagens e gráficos estivessem em conformidade com as leis de propriedade intelectual.

O processo de ideação e design em grupo foi fundamental para a criação de um jogo envolvente e inovador, garantindo que todas as etapas fossem colaborativas e alinhadas com os objetivos estabelecidos. Com o tema escolhido e os recursos visuais em desenvolvimento, nossa equipe estava pronta para dar continuidade ao processo de desenvolvimento do jogo.

<a id="bibliotecas"></a>
## Bibliotecas Utilizadas
- [ PyGame ]( https://www.pygame.org/news ): É a principal biblioteca utilizada no projeto. Usada majoritariamente para montar as cenas e mecânicas do jogo.
- [ Sys ]( https://docs.python.org/pt-br/3/library/sys.html ): Usada para encerrar o programa quando o jogador desejar.
- [ Random ]( https://docs.python.org/pt-br/3/library/random.html ): Usada para randomizar o spawn, drop de itens, etc e deixar o jogo mais dinâmico.
- [ Math ]( https://docs.python.org/pt-br/3/library/math.html ): Usada para facilitar cálculos matemáticos com funções como seno e cosseno.


<a id="organizacao"></a>
## Organização do código

### main.py

Esse arquivo possui o loop principal do jogo. Além disso, é nele que configuramos e utilizamos as outras classes existentes no projeto.

### mapa.py

Esse arquivo contém o mapa do jogo que é baseado em uma matriz. Além disso é neste arquivo que se encontra a classe Mapa que contém os métodos "criar_mapa" (responsável por ler a matriz e transformá-la em um elemento gráfico) e "desenhar" (responsável por fazer o mapa aparecer na tela).

### player.py

Esse arquivo contém a classe Player. Nela encontramos os métodos "move" (responsável pela movimentação do jogador), "desenhar" (responsável por renderizar o jogador na tela), "get_posicao", "get_posicao_list" (responsáveis pelo retorno da posição do jogador), "rect" (responsável pelo hitbox do jogador), "morte_check" (responsável por checar se o jogador morreu) e "coleta" (responsável pela checagem e coleta de itens).

### inimigo.py

Esse arquivo contém a classe Inimigo. Nela encontramos os métodos "desenhar" (responsável pela renderização do inimigo na tela de jogo), "comportamento" (responsável pela IA do inimigo), "rect_inimigo" e "rect_inicial" (responsável pelo hitbox do inimigo e por mover essa hitbox de acordo com a câmera) e "reposicionar", que gera uma nova posição pro inimigo caso necessário.

### coletavel.py

Esse arquivo contém a classe Coletável. Nela encontramos os métodos "desenhar" (responsável por desenhar os drops na tela), "rect_coleta" e "rect_inicial" (responsável pelo hitbox dos itens e por movê-los de acordo com a câmera) e "get_pc" (retorna a posição do item)

### bloco.py

Esse arquivo contém a classe Bloco que é usada na classe Mapa e é responsável por decodificar a matriz de mapa em imagens (tiles).

### barras.py

Esse arquivo contém as classes Vida e Sede que são responsáveis respectivamente por renderizar e controlar as barras de vida e de sede do jogo.

### bullets.py
Esse arquivo contém a classe PlayerBullets que é responsável por renderizar e checar colisões dos projéteis com outros objetos por meio dos métodos "desenhar", "rect" e "check_if_hit" respectivamente, bem como sua classe filha EnemyBullets que possui as mesmas funções porém para os inimigos, e um método de desenhar próprio chamado "desenhar_offset" que faz com que as balas inimigas respeitem a câmera.

<a id="conceitos"></a>
## Conceitos aprendidos na disciplina
- <strong>Funções</strong>: De longe esse foi o conceito aprendido na disciplina que foi mais utilizado durante o desenvolvimento do jogo, sendo usada para quase todas as mecânicas e elementos essenciais, geração de inimigos/coletáveis e telas de menu. Possibilitou o reuso e a organização do código.
- <strong>Loop</strong>: Conceito essencial para o desenvolvimento de jogos, pois esse tipo de mídia se baseia em um grande loop para execução e processamento de inputs. As funções para desenhar entidades e admnistrar hitboxes estão em loops para permitir que sejam usadas em todas as entidades na tela, armazenadas em listas.
- <strong>Orientação a objetos</strong>: Outro conceito aprendido na disciplina e amplamente utilizado no projeto, que permitiu uma maior organização, reuso e legibilidade do código graças às diversas classes mencionadas anteriormente.
- <strong>Listas</strong>: Muito utilizada para lidar com posições e realizar cálculos matemáticos. O mapa do jogo é uma matriz (lista de listas) e as entidades estão armazenadas em listas.
- <strong>Condicionais</strong>: Estruturas condicionais são fundamentais em um jogo, pois várias funcionalidades possuem pré-requisitos. Por exemplo, uma estrutura condicional checa se a sede do personagem está em 0 e toma as atitudes apropriadas para isso, como mudar a música e iniciar o contador para dano contínuo.

<a id="desafios"></a>
## Desafios enfrentados

Desde o começo esse foi um projeto desafiador por se tratar de um sistema interativo baseado na biblioteca PyGame, a qual nenhum dos integrantes do grupo tinha conhecimento. Nosso principal erro foi a falta de organização inicial do código, pois ainda estávamos nos acostumando com o projeto, mas que rapidamente foi resolvido com a introdução de novas funcões, arquivos e orientação a objetos. Apesar disso, foi um projeto divertido de fazer, desde a parte de ideação até a entrega trabalhamos sempre juntos para superar os desafios que apareceram e as dificuldades individuais de cada integrante e esse trabalho em equipe foi nosso principal aprendizado fora do código. Dentro do código nosso principal aprendizado foi a orientação a objetos e organização.

<a id="capturas"></a>
## Capturas de tela

Tela Inicial | Tela de Jogo
:-------------------------:|:-------------------------:
<img src="https://media.discordapp.net/attachments/1150492210702331965/1158197767089426442/image.png?ex=651b5f39&is=651a0db9&hm=08dd54633b50c43d28c7aba9faab67070638cba6b68322552f36b03a1310f44f&=" alt="Tela Inicial" height="240"> | <img src="https://i.ytimg.com/vi/c1Fv1uKTd-w/sddefault.jpg" alt="Tela de Jogo" height="240"> 

Jogador sem vida | Game Over
:-------------------------:|:-------------------------:
<img src="https://media.discordapp.net/attachments/1150492210702331965/1158198563843624960/image.png?ex=651b5ff7&is=651a0e77&hm=9412eac676223ebe812f9bdac225cd971aafd6bacbf3c32b3d71adbca627655f&=" alt="Jogador sem vida" height="240"> | <img src="https://i.ytimg.com/vi/c1Fv1uKTd-w/sddefault.jpg" alt="Game Over"  height="240">

<a id="demo"></a>
## Video de demonstração
[![Demo](https://i.ytimg.com/vi/c1Fv1uKTd-w/sddefault.jpg)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

<a id="como-instalar"></a>
## Como instalar
### Certifique-se de ter Python3 e PyGame instalados em seu computador

### Abra o terminal do seu sistema em uma pasta à sua escolha, copie e cole o seguinte comando:

#### Se você usa Windows, execute esse comando:
```
#Clone esse repositório
git clone https://github.com/ditthales/projeto-ip.git
#Entre na pasta do projeto
cd projeto-ip
#Execute o arquivo 'main.py'
py main.py
```
#### Se você usa MacOS ou Linux, execute esse comando:
```
#Clone esse repositório
git clone https://github.com/ditthales/projeto-ip.git
#Entre na pasta do projeto
cd projeto-ip
#Execute o arquivo 'main.py'
python3 main.py
```
 Ou apenas baixe o arquivo .zip, extraia em algum lugar da sua escolha e execute o arquivo 'main.py'.
