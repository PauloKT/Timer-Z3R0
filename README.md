# 💣 Timer Z3R0

**Timer Z3R0** é um jogo de suspense e raciocínio rápido que se passa inteiramente no terminal.\
Você é um agente encarregado de desarmar bombas prestes a explodir. Cada rodada desafia seus reflexos e sua mente: descubra o código secreto antes que o tempo chegue a zero.

A cada bomba desarmada, a dificuldade aumenta. O tempo fica mais curto e os códigos se tornam mais complexos.\
Você tem nervos de aço o bastante para enfrentar o **Timer Z3R0**?

---

## 🛠 Requisitos

- Python 3
- Terminal (cmd, bash, PowerShell, etc.)
- Bibliotecas: `random`, `os`, `time` (somente `sleep`, já inclusas no Python)

---

## 💾 Como Instalar e Rodar

### 1. Clone o repositório

Se ainda não tiver o projeto na sua máquina:

```bash
git clone https://github.com/PauloKT/Timer-Z3R0.git
cd Timer-Z3R0
```

### 2. Execute o jogo

```bash
python nome_do_arquivo.py
```

(Substitua `nome_do_arquivo.py` pelo nome real do arquivo principal do jogo.)

---

## ▶️ Como Jogar

1. Execute o arquivo `.py` no terminal.
2. Tente digitar corretamente a senha antes do tempo acabar.
3. Cada erro custa tempo precioso.
4. A cada sucesso, você avança para uma bomba mais difícil.

---

## 🚀 Fluxo Git Essencial

### ✅ Adicionar e fazer commit dos arquivos

```bash
git add .
git commit -m "mensagem explicando o que foi feito"
```
## 🌿 Criando uma nova branch

```bash
git checkout -b nome-da-nova-branch
```

### 📤 Enviar (push) para o GitHub

Conecte o projeto local ao repositório remoto (caso ainda não tenha feito isso):

```bash
git remote add origin https://github.com/PauloKT/Timer-Z3R0.git
git branch -M
git push -u origin
```

### 📥 Atualizar seu projeto local (pull)

```bash
git pull origin main
```

### 🌿 Mudar de branch

```bash
git checkout nome-da-branch
```

Exemplo:

```bash
git checkout dev
```

### 🔄 Atualizar uma branch local com a versão remota

Se já estiver na branch:

```bash
git pull origin nome-da-branch
```

Exemplo:

```bash
git pull origin dev
```

### 🔁 Mudar de repositório remoto (trocar origem)

Caso deseje apontar seu projeto local para outro repositório:

```bash
git remote set-url origin https://github.com/usuario/novo-repositorio.git
```

Você pode verificar o repositório atual com:

```bash
git remote -v
```

---

## ✨ Exemplo de commit legal

```bash
git commit -m "Adiciona lógica de tempo e verificação da senha"
```

