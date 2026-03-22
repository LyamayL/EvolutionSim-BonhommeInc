# EvolutionSim-BonhommeInc
**Projet Personnel – Decembre 2025 - Janvier 2026**

## 🇫🇷 - Présentation
**BonhommeInc** est une simulation multi-agents dans laquelle de petits agents ont pour objectif de **survivre et se reproduire** en collectant des ressources.  
Chaque agent est soumis à des règles locales simples et possède des caractéristiques propres, qui peuvent évoluer au fil des générations grâce à un algorithme inspiré de la **sélection naturelle**.  
Cette simulation permet d’observer l’émergence de comportements **coopératifs ou égoïstes** dans un monde simple mais dynamique.

## Principe de fonctionnement
- **Génération initiale :**  
  La première génération (n°0) est composée d’un unique individu. Chaque agent possède plusieurs caractéristiques :  
  - **Champ de vision**  
  - **Vitesse**  
  - **Égoïsme**  

- **Survie et reproduction :**  
  - Pour survivre à la génération suivante, un agent doit consommer au moins **3 pommes** (points rouges).  
  - Pour chaque tranche de **3 pommes supplémentaires**, l’agent produit un enfant.  
  - L’enfant hérite des caractéristiques de son parent, avec des **mutations légères**, permettant d’observer l’évolution des traits au fil des générations.  

- **Émergence de l’égoïsme :**  
  - Une fois la population **≥ 40 individus**, des vaches (points marron) apparaissent.  
  - Chaque vache fournit jusqu’à **6 unités de nourriture**, mais **nécessite deux agents pour être consommée**.  
  - Chaque agent a une part d’égoïsme (0 à 6) qui détermine sa portion souhaitée :  
    1. **Somme des égoïsmes = 6** : chaque agent reçoit exactement sa part.  
       - Ex : 2 + 4 → premier agent = 2, second agent = 4  
    2. **Somme < 6** : chacun prend sa part, le reste est partagé équitablement.  
       - Si le reste est impair, **le plus égoïste prend l’excédent**.  
       - Si les égoïsmes sont égaux, **le premier arrivé prend l’excédent**.  
    3. **Somme > 6** : les agents ne reçoivent rien, mais un **malus énergétique** est appliqué.  
       - La quantité restante après le malus est partagée comme dans le cas précédent.  
       - Ex : Agent 1 demande 5, Agent 2 demande 4 → 10 > 6 → 10 - 6 = 4 → -2 pour le malus → 2 → chacun reçoit 1  

Cette mécanique permet d’observer **comment l’égoïsme et la coopération influencent la survie et la reproduction** des agents au fil des générations.

## Technologies
- **Python**  
- **Pygame** – animation et affichage des agents et ressources  
- **Matplotlib** – visualisation de l’évolution des statistiques  
- **Algorithme de sélection naturelle simplifié**

---

## 🇬🇧 - Overview
**BonhommeInc** is a multi-agent simulation where small agents aim to **survive and reproduce** by collecting resources.  
Each agent follows simple local rules and has individual traits that can evolve over generations thanks to a simplified **natural selection algorithm**.  
This simulation allows observing the emergence of **cooperative or selfish behaviors** in a simple yet dynamic world.

## How it works
- **Initial generation:**  
  The first generation (Gen 0) consists of a single individual. Each agent has several traits:  
  - **Vision range**  
  - **Speed**  
  - **Selfishness**  

- **Survival and reproduction:**  
  - To survive to the next generation, an agent must consume at least **3 apples** (red points).  
  - For every additional **3 apples eaten**, the agent produces one child.  
  - The child inherits the traits of its parent, with **slight mutations**, allowing us to track the evolution of traits over time.  

- **Emergence of selfishness:**  
  - Once the population reaches **≥ 40 agents**, cows (brown points) appear.  
  - Each cow provides up to **6 units of food**, but **requires two agents to consume it**.  
  - Each agent has a selfishness score (0 to 6) that determines its desired share:  
    1. **Sum of selfishness = 6**: each agent receives exactly their share.  
       - Ex: 2 + 4 → first agent = 2, second agent = 4  
    2. **Sum < 6**: each takes their share, the remainder is split evenly.  
       - If the remainder is odd, **the more selfish agent takes the extra unit**.  
       - If both have the same selfishness, **the first to arrive takes the extra unit**.  
    3. **Sum > 6**: agents receive nothing, but an **energy penalty** is applied.  
       - The remaining food after the penalty is split as above.  
       - Ex: Agent 1 requests 5, Agent 2 requests 4 → 10 > 6 → 10 - 6 = 4 → -2 energy penalty → 2 → each gets 1  

This mechanism allows observing **how selfishness and cooperation influence survival and reproduction** across generations.


## Technologies
- **Python**  
- **Pygame** – animation and display of agents and resources  
- **Matplotlib** – visualization of statistics and evolution  
- **Simplified natural selection algorithm**   


