Rota Inteligente: Otimização de Entregas com Algoritmos de IA
1. Descrição do Problema, Desafio Proposto e Objetivos
1.1 Descrição do Problema

A empresa de delivery de alimentos “Sabor Express”, que atua na região central da cidade, enfrenta desafios significativos na gestão de suas entregas, especialmente em horários de pico. Atualmente, as rotas são definidas manualmente, com base apenas na experiência dos entregadores, o que gera ineficiências como atrasos, aumento do consumo de combustível e, consequentemente, insatisfação dos clientes.

Para que a empresa se mantenha competitiva, torna-se essencial desenvolver um sistema que torne as entregas mais rápidas, econômicas e eficientes, reduzindo custos e aumentando a satisfação dos clientes.

1.2 Objetivos

O projeto tem como principais objetivos:

Implementar algoritmos de busca em grafos (como A*, BFS ou DFS) para determinar o caminho mais curto entre múltiplos pontos de entrega.

Aplicar algoritmos de clustering (como K-Means) para agrupar pedidos em zonas geograficamente próximas, especialmente durante períodos de alta demanda.

Avaliar e comparar as soluções propostas com métricas de desempenho, como distância percorrida, tempo total e custos de combustível.

Desenvolver uma solução que demonstre raciocínio analítico, visão sistêmica e criatividade na aplicação de conceitos de Inteligência Artificial a problemas logísticos reais.

Contribuir para a melhoria da qualidade do serviço, redução de custos operacionais e aumento da satisfação dos clientes da "Sabor Express".

2. Abordagem Adotada

Para enfrentar o desafio de otimização das rotas da “Sabor Express”, propomos uma abordagem híbrida que integra Teoria dos Grafos, Algoritmos de Busca de Caminho Mínimo e Clustering. Essa estratégia busca otimizar tanto o percurso de cada entregador quanto a distribuição de pedidos em cenários de alta demanda.

2.1 Modelagem do Problema como Grafo

A cidade será representada como um grafo ponderado e direcionado, onde:

Nós (vértices) representam os locais de entrega (endereços de clientes e bairros) e o centro de distribuição da empresa.

Arestas representam as ruas ou conexões entre os pontos, com pesos associados que podem ser:

Distância física

Tempo estimado de viagem

Custo de combustível

A escolha do peso dependerá da métrica de otimização desejada (menor distância, menor tempo ou menor custo).

2.2 Otimização de Rotas com Algoritmos de Busca

Para encontrar o caminho mais curto entre os pontos de entrega, será utilizado o algoritmo A*.

O A* combina a eficiência da busca gulosa com a garantia de otimalidade do algoritmo de Dijkstra, desde que seja usada uma heurística admissível.

A heurística escolhida será a distância euclidiana entre o ponto atual e o destino, oferecendo uma estimativa eficiente e precisa para roteamento.

Comparativamente:

BFS (Busca em Largura) é adequado para grafos não ponderados e garante o caminho mais curto em número de arestas, mas não necessariamente em peso total.

DFS (Busca em Profundidade) é útil para explorar todas as possibilidades, mas não garante a rota mais eficiente.

Assim, o A* será aplicado tanto do depósito aos pontos de entrega quanto entre os próprios pontos, minimizando custo total em termos de distância, tempo ou combustível.

2.3 Agrupamento de Entregas com Clustering

Em situações de alta demanda, otimizar rotas individualmente se torna ineficiente. Para contornar isso, será aplicado K-Means, um algoritmo de aprendizado não supervisionado, para agrupar pedidos geograficamente.

Cada cluster representará um conjunto de entregas próximas.

O número de clusters (k) será determinado dinamicamente, considerando a capacidade dos entregadores ou usando o Método do Cotovelo (Elbow Method).

O agrupamento permite transformar o problema de múltiplos pontos em um problema de clusters, facilitando a distribuição equilibrada das entregas e reduzindo a complexidade do roteamento.

Após o agrupamento, o A* será usado dentro de cada cluster para traçar a rota mais eficiente para cada entregador, garantindo a minimização de distância e otimização do tempo de entrega.

2.4 Avaliação e Comparação

A solução será avaliada por meio de métricas como:

Distância total percorrida, comparando rotas manuais e otimizadas

Tempo total de entrega, buscando reduzir o tempo médio por pedido

Custo de combustível, estimando a economia gerada

Satisfação do cliente, potencialmente maior devido a entregas mais rápidas e pontuais

Simulações serão realizadas em diferentes cenários de demanda, validando a eficácia da integração de IA na otimização logística.

3. Algoritmos Utilizados
3.1 A* (A-star)

Descrição: Algoritmo de busca informada que encontra o caminho de menor custo entre um nó inicial e um nó objetivo em um grafo.

Funcionamento: Usa a função 
𝑓
(
𝑛
)
=
𝑔
(
𝑛
)
+
ℎ
(
𝑛
)
f(n)=g(n)+h(n)

𝑔
(
𝑛
)
g(n): custo do caminho até o nó n

ℎ
(
𝑛
)
h(n): estimativa heurística do custo restante até o objetivo

Aplicação: Calcula o caminho mais curto entre depósito e entregas, considerando distância ou tempo. A heurística utilizada é a distância em linha reta (euclidiana).

3.2 K-Means

Descrição: Algoritmo de aprendizado não supervisionado que particiona n pontos em k clusters, associando cada ponto ao centróide mais próximo.

Funcionamento:

Inicializa k centróides

Atribui cada ponto ao centróide mais próximo

Recalcula os centróides

Repete até convergência

Aplicação: Agrupa pedidos em zonas próximas, permitindo que cada entregador atue em um cluster específico. O número ideal de clusters será definido pelo Método do Cotovelo.

A combinação de K-Means (agrupamento) e A* (roteamento) garante eficiência tanto em nível macro (distribuição de carga de trabalho) quanto nível micro (roteamento individual dentro de cada cluster).
