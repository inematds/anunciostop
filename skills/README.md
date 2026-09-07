# Anúncios Top com IA · as 4 skills do curso

As quatro skills usadas no curso, prontas pra instalar no Claude Code. Cada uma faz **uma** coisa
e passa o bastão pra seguinte por escrito.

```
/espiona-ads        →  o que está funcionando lá fora e por quê
/video-ia           →  da sua ideia a 10 roteiros; do escolhido à ficha de personagem, modelo e prompts
/auditor-video-ia   →  isso se conserva, se salva na montagem ou se regenera?
/anuncio-edita      →  a peça final montada e masterizada pra Meta
```

> Se o bruto for **gravado com câmera** em vez de gerado com IA, a montagem não é
> `/anuncio-edita`: é `reel-edita-inema`, que é uma skill à parte do ecossistema INEMA.

---

## Instalação (2 minutos)

1. Descompacte o zip.
2. Copie as quatro pastas de `skills/` pra sua pasta de skills:

```bash
cp -R skills/* ~/.claude/skills/
```

3. Abra o Claude Code e digite `/video-ia`. Se ele fizer cinco perguntas, está instalado.

> **Windows / outro caminho:** a pasta é a que a sua instalação do Claude Code usa pra skills de
> usuário. Se você já tem outras skills, é a mesma pasta onde elas estão.

---

## O que mais você precisa

| Pra quê | O que precisa | Obrigatório |
|---|---|---|
| Tudo | Claude Code | Sim |
| `/espiona-ads` e `/anuncio-edita` | `ffmpeg` e `ffprobe` | Sim pra essas duas |
| `/espiona-ads` (transcrição) | Uma chave da Groq em `GROQ_API_KEY` | Sim pra essa |
| Legendas queimadas | Python com Pillow (`pip install pillow`), só se o seu ffmpeg não tiver `libass` | Só nesse caso |
| Gerar o vídeo | Conta na plataforma que você escolher | Sim; Agnes é a custo zero, as demais se pagam à parte |

**A chave da Groq** entra de um destes jeitos, o que preferir:

```bash
export GROQ_API_KEY="sua-chave"
```

…ou num arquivo `.env` na raiz do seu projeto com a linha `GROQ_API_KEY=sua-chave`. A skill
procura primeiro na variável de ambiente, depois no `.env` do projeto. Nunca copie a chave pra
dentro de um prompt ou de um arquivo de saída.

**A Agnes** (provedor padrão, custo zero) precisa de `AGNES_API_KEY`, no mesmo esquema. Os outros
provedores (Seedance via TopView/Higgsfield, Dreamina, Magnific) funcionam pela interface web deles:
você cola o prompt lá, nada precisa ser configurado aqui.

---

## A primeira coisa a fazer (não pule)

Essas skills trabalham com **a sua** marca, e vêm com a ficha em branco de propósito:

**Ficha de marca:** copie `video-ia/marcas/_modelo.md` pra `anuncios/marcas/<sua-marca>.md` e
preencha. Tem um exemplo preenchido em `_exemplo-oficina-do-bairro.md` (marca inventada). Quinze
minutos, uma vez só.

Sem ela as skills funcionam, mas vão perguntar mais, e os roteiros vão soar genéricos.

## Onde elas escrevem

Por padrão trabalham numa pasta `anuncios/` dentro do seu projeto:

```
anuncios/
├── marcas/                  a sua ficha de marca
├── roteiros/                os dossiês de cada peça
├── criativos/               uma pasta por peça: módulos, master, SRT
├── _apresentadores/         fichas de continuidade (mesma cara em todos os anúncios)
└── referencias-criativas/   o que o /espiona-ads produz
```

Não precisa criar: ela se cria sozinha na primeira vez.

---

## Dois avisos honestos

- **Gerar vídeo custa dinheiro** (fora da Agnes). As skills não gastam crédito sozinhas e avisam
  antes, mas o vídeo gerado se paga na plataforma que você usar. `/auditor-video-ia` existe
  justamente pra você não regenerar cinco vezes o que se resolve na montagem.
- **Os limites de cada modelo caducam rápido.** Os adaptadores por interface têm data dentro de
  `video-ia/references/adapters/`. Quando um número não bater com o que você vê na tela, mande o que
  viu: corrige-se o adaptador e segue.
