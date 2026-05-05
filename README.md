# projetos_estruturas_lineares
Desafio 1 — Sistema de votação de representantes

Qual problema o programa resolve? Registrar os votos dos alunos de uma turma para três candidatos (Ana, Bruno ou Carlos) e ao final exibir o resultado da eleição, indicando o vencedor ou empate.
Quais estruturas foram utilizadas? Lista — cada voto digitado é armazenado com .append() e ao final contado com .count().
Como executar o programa? • Execute o arquivo desafio1.py • O programa exibe os candidatos disponíveis • Digite o nome do candidato e pressione Enter para registrar o voto • Repita para cada aluno da turma • Digite fim para encerrar e ver o resultado
Exemplo de entrada e saída:Candidatos:
Ana
Bruno
Carlos
Digite o nome do candidato (fim para encerrar): Ana Digite o nome do candidato (fim para encerrar): Bruno Digite o nome do candidato (fim para encerrar): Ana Digite o nome do candidato (fim para encerrar): Bruno Digite o nome do candidato (fim para encerrar): Bruno Digite o nome do candidato (fim para encerrar): fim

Resultado da votação: Ana: 2 votos Bruno: 3 votos Carlos: 0 votos O vencedor é: Bruno
Desafio 2 — Editor com a opção de desfazer

Qual problema o programa resolve? Simular um editor de texto simples onde o usuário digita palavras e pode desfazer a última palavra adicionada, como o famoso Ctrl+Z.
Quais estruturas foram utilizadas? Pilha (LIFO — Last In, First Out) — as palavras são adicionadas com .append() no topo e removidas com .pop(), ou seja, a última palavra digitada é a primeira a ser desfeita.
Como executar o programa? • Execute o arquivo desafio2.py • Escolha a opção 1 para digitar uma palavra • Escolha a opção 2 para desfazer a última palavra • Escolha a opção 3 para ver o texto atual • Escolha a opção 4 para sair
Exemplo de entrada e saída:EDITOR DE TEXTO [1] - Digitar palavra [2] - Desfazer última palavra [3] - Mostrar texto [4] - Sair Escolha uma opção: 1 Digite uma palavra: minha Palavra adicionada: minha
Escolha uma opção: 1 Digite uma palavra: terra Palavra adicionada: terra

Escolha uma opção: 3 Texto atual: minha terra

Escolha uma opção: 2 Palavra removida: terra

Escolha uma opção: 3 Texto atual: minha
Desafio 3 — Fila de atendimento

Qual problema o programa resolve? Simular a fila de atendimento de uma secretaria acadêmica, garantindo que o primeiro aluno a entrar na fila seja o primeiro a ser atendido.
Quais estruturas foram utilizadas? Fila (FIFO — First In, First Out) — os alunos entram no final da fila com .append() e são atendidos pelo início com .pop(0), respeitando a ordem de chegada.
Como executar o programa? • Execute o arquivo desafio3.py • Escolha a opção 1 para adicionar um aluno à fila • Escolha a opção 2 para chamar o próximo aluno • Escolha a opção 3 para ver a fila atual • Escolha a opção 4 para sair
Exemplo de entrada e saída:SECRETARIA ACADÊMICA [1] - Retirar senha [2] - Chamar próximo aluno [3] - Mostrar fila [4] - Sair Escolha uma opção: 1 Nome do aluno: Marco Marco entrou na fila de atendimento.
Escolha uma opção: 1 Nome do aluno: Ana Ana entrou na fila de atendimento.

Escolha uma opção: 3 Fila atual: 1º - Marco 2º - Ana

Escolha uma opção: 2 Chamando aluno: Marco

Escolha uma opção: 3 Fila atual: 1º - Ana
