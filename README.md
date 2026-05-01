# 🧠 Dynamic Wumpus Logic Agent (Web App)

A Web-based Knowledge-Based Agent that navigates a dynamic Wumpus World using **Propositional Logic** and **Resolution Refutation**.  
The agent learns about the environment through percepts (Breeze, Stench) and uses a **Knowledge Base (KB)** to infer safe and unsafe cells in real-time.

---

## 🚀 Features

- 📊 Dynamic grid size (configurable rows × columns)
- 💨 Percept-based reasoning:
  - Breeze → nearby pit exists
  - Stench → nearby Wumpus exists
- 🧠 Knowledge Base using CNF logic
- 🔍 Resolution Refutation inference engine
- 🟩 Safe / 🟥 Dangerous cell classification
- 🕹️ Web-based interactive UI
- 📈 Real-time metrics:
  - Inference steps
  - Clause count
  - Current percepts

---

## 🧩 Project Structure

---

## ⚙️ How It Works

### 1. Knowledge Base (KB)
The agent stores world knowledge in **Conjunctive Normal Form (CNF)** using clauses of literals.

Example:
- `B_1_1 ⇔ P_1_2 ∨ P_2_1`
- Converted into CNF for inference

---

### 2. TELL Operation
When the agent receives percepts:
- Breeze / Stench rules are added to KB
- Logical constraints are encoded as clauses

---

### 3. ASK Operation (Resolution Refutation)
Before moving:
- The agent checks if a cell is safe
- It proves:
  - ¬Pit AND ¬Wumpus
- Uses **resolution** to derive contradiction

If contradiction is found → cell is safe

---

### 4. Agent Decision Policy
Priority-based movement:

1. Move to **safe unvisited cell**
2. Move to **unvisited unknown cell**
3. Backtrack if necessary

---

## 🌐 Web Server

Run the system:

```bash
python server.py
🌐 Live Demo: https://wumpus-project.vercel.app/
