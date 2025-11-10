# Sabor Express – Otimização Inteligente de Entregas

## 1. Descrição do Problema
A empresa **Sabor Express**, que realiza delivery de alimentos na região central da cidade, enfrenta dificuldades em gerenciar suas entregas durante horários de pico, como almoço e jantar. As rotas são definidas manualmente, resultando em:

- Entregas atrasadas
- Rotas ineficientes
- Aumento do custo de combustível
- Insatisfação dos clientes

**Objetivo do projeto:**  
Desenvolver uma solução baseada em Inteligência Artificial capaz de sugerir rotas otimizadas para entregadores, reduzindo tempo, distância percorrida e custos operacionais, ao mesmo tempo em que melhora a experiência do cliente.

---

## 2. Desafio Proposto
O desafio consiste em:

1. Representar a cidade como um **grafo ponderado**, onde:
   - **Nós:** bairros ou pontos de entrega
   - **Arestas:** ruas com peso baseado em distância ou tempo estimado
2. Encontrar o **menor caminho** entre múltiplos pontos de entrega.
3. Agrupar pedidos próximos em **zonas de entrega** para otimizar o trabalho dos entregadores.
4. Gerar rotas eficientes considerando:
   - Capacidade limitada dos entregadores
   - Tempo máximo de entrega
   - Prioridade dos pedidos

---

## 3. Abordagem Adotada

### 3.1 Modelagem
- A cidade é modelada como um **grafo**, com ruas e distâncias reais.
- Pedidos são representados por coordenadas geográficas (lat, lon).
- Cada entregador recebe um **cluster de pedidos** baseado na proximidade (K-Means).

### 3.2 Clusterização
- Algoritmo utilizado: **K-Means**.
- Função: agrupar pedidos próximos em zonas, permitindo que cada entregador tenha rotas otimizadas.
- Número de clusters = número de entregadores ativos.

### 3.3 Roteamento
- Algoritmos utilizados:
  - **Nearest Neighbor:** define a rota inicial dentro do cluster.
  - **2-opt (opcional):** refina a rota para reduzir distância total.
  - **A*** (opcional): busca o menor caminho em grafos ponderados.

### 3.4 Fluxo do Sistema
Pedidos ativos + localização dos entregadores
│
▼
Agrupamento de entregas (K-Means)
│
▼
Atribuição de clusters a entregadores
│
▼
Otimização da rota interna (Nearest Neighbor + 2-opt)
│
▼
Avaliação de rotas (distância, tempo, custo)
│
▼
Entregadores recebem rotas otimizadas
## 4. Algoritmos Utilizados
| Algoritmo | Aplicação |
|-----------|-----------|
| **K-Means** | Agrupamento de pedidos próximos em zonas de entrega |
| **Nearest Neighbor** | Heurística para ordenar entregas dentro de cada cluster |
| **2-opt** | Otimização das rotas calculadas pelo Nearest Neighbor |
| **A*** | Cálculo do menor caminho entre pontos do grafo (opcional) |
| **BFS / DFS** | Exploração do grafo e checagem de conectividade (opcional) |

---

## 5. Diagrama do Grafo / Modelo

O grafo da cidade é representado com nós (pontos de entrega) e arestas (ruas com distância).  

![Grafo da Cidade](docs/grafo.png)

- Cada cluster representa a rota de um entregador.
- O diagrama facilita a visualização das rotas e clusters.

---

## 6. Resultados e Análise

- **Comparação:** rotas manuais vs. rotas otimizadas.
- **Métricas avaliadas:**
  - Distância total percorrida
  - Tempo estimado de entrega
  - Número de entregas dentro do prazo
  - Distribuição de carga entre entregadores
- **Eficiência observada:**
  - Redução significativa da distância percorrida.
  - Otimização das entregas em horários de pico.
- **Limitações:**
  - K-Means exige definir o número de clusters (entregadores) previamente.
  - Algoritmos heurísticos não garantem solução global ótima.
  - Não considera tráfego em tempo real (poderia ser melhorado com APIs externas).

---

## 7. Sugestões de Melhoria

1. Integrar **dados de tráfego em tempo real** (Google Maps API, OSRM).
2. Implementar **Aprendizado por Reforço (RL)** para roteamento dinâmico.
3. Adotar **Programação Linear Inteira (MILP)** para otimizar multi-entregador simultaneamente.
4. Criar interface visual interativa para os entregadores acompanharem rotas em tempo real.

---

## 8. Referências

1. **UPS – ORION**: Sistema de otimização de rotas em tempo real, economizando milhões de milhas.  
2. **Medium – “Optimizing Logistics: Clustering e MILP”**: Aplicação de K-Means e Programação Linear para entrega eficiente.  
3. **ResearchGate – AI-Powered Route Optimization**: Integração de IA, sensores IoT e algoritmos heurísticos para roteamento dinâmico.  
4. **Kardinal.ai – Fresh Product Delivery**: Otimização contínua de rotas e planejamento de território.

---

**Instruções de Execução:**

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar script principal
python src/main.py