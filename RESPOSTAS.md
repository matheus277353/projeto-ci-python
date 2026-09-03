# Respostas — Atividade Guiada GitHub Actions + Python

## 1. Qual evento iniciou o seu workflow?

O workflow foi iniciado pelo evento `push` na branch `main`.
Isso significa que toda vez que um commit é enviado (`git push`) para a branch principal,
o GitHub Actions dispara automaticamente a esteira de CI.

---

## 2. Qual é a função de `actions/checkout@v4`?

A action `actions/checkout@v4` é responsável por **baixar (clonar) o conteúdo do repositório**
para dentro da máquina virtual fornecida pelo GitHub (o runner).  
Sem essa etapa, o runner estaria vazio e não teria acesso ao código para instalar dependências
ou executar os testes.

---

## 3. Por que executar testes localmente e também no GitHub Actions?

Executar testes **localmente** garante um ciclo de desenvolvimento rápido — o desenvolvedor
recebe feedback imediato antes de fazer o push.

Executar os testes **no GitHub Actions** garante que o código funcione em um **ambiente
limpo e padronizado** (Ubuntu, versão de Python definida, sem dependências extras da máquina
do desenvolvedor). Isso protege o projeto de problemas como:
- "Funciona na minha máquina, mas não no servidor."
- Dependências não declaradas em `requirements.txt`.
- Regressões introduzidas por outros membros da equipe.

---

## 4. Em que etapa o defeito foi identificado?

O defeito foi identificado na etapa **"Executar testes"** (`run: python -m pytest -v`).

O teste `test_situacao_aprovado` falhou, pois ele verifica que `situacao_aluno(7.0)` retorna
`"Aprovado"`. Com a alteração de `>= 7` para `> 7`, uma média exatamente igual a 7 passou
a retornar `"Recuperação"` em vez de `"Aprovado"`, violando a regra de negócio.

---

## 5. O que poderia acontecer em um projeto real se essa alteração fosse publicada sem testes?

Em um projeto real, essa alteração causaria uma **regressão silenciosa**:
- Alunos com média exata de **7,0** seriam incorretamente classificados como em **Recuperação**.
- O erro poderia passar semanas sem ser detectado até alguém reclamar.
- Dependendo do sistema (notas escolares, aprovação em concursos), o impacto seria **crítico**
  para os usuários afetados.
- A correção tardia geraria custos extras de suporte, retrabalho e perda de confiança.

A CI com testes automatizados atua como uma **rede de segurança**: ela pega esse tipo de
regressão imediatamente, antes que chegue aos usuários.

---

## Desafio Extra — `strategy.matrix`

O arquivo `.github/workflows/ci.yml` foi atualizado para executar os testes nas versões
**Python 3.10, 3.11 e 3.12** simultaneamente, usando `strategy.matrix`:

```yaml
strategy:
  matrix:
    python-version: ["3.10", "3.11", "3.12"]
```

Isso garante que o projeto é compatível com múltiplas versões do Python ao mesmo tempo.
