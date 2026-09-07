# Anúncios Top com IA

Sistema de quatro decisões pra transformar uma ideia em um anúncio em vídeo gerado por IA, pronto
pra Meta, sem gastar crédito às cegas. Quatro skills pro Claude Code, em português, encadeadas:
cada uma faz **uma** coisa e deixa um documento escrito pra seguinte.

```
/espiona-ads        →  o que está funcionando lá fora e por quê
/video-ia           →  da sua ideia a 10 roteiros; do escolhido à ficha de personagem, modelo e prompts
/auditor-video-ia   →  isso se conserva, se salva na montagem ou se regenera?
/anuncio-edita      →  a peça final montada e masterizada pra Meta
```

**A tese:** o prompt não é o trabalho. O trabalho é decidir o ângulo, congelar a identidade,
dirigir o plano e auditar antes de publicar. Por isso o sistema continua valendo quando o modelo
da moda mudar.

- Guia de uso: `guia/index.html` (publicado em `https://inematds.github.io/anunciostop/guia/`)
- Download das skills: [`anuncios-top-skills.zip`](anuncios-top-skills.zip)
- Plano do curso: [`PLANO-CURSO.md`](PLANO-CURSO.md)

---

## Índice

1. [Instalação](#1-instalação)
2. [O que mais você precisa](#2-o-que-mais-você-precisa)
3. [A primeira coisa a fazer: a ficha de marca](#3-a-primeira-coisa-a-fazer-a-ficha-de-marca)
4. [A cadeia de quatro decisões](#4-a-cadeia-de-quatro-decisões)
5. [As skills, uma a uma](#5-as-skills-uma-a-uma)
6. [Provedores e adaptadores](#6-provedores-e-adaptadores)
7. [Onde as skills escrevem](#7-onde-as-skills-escrevem)
8. [Estrutura do repositório](#8-estrutura-do-repositório)
9. [O curso](#9-o-curso)
10. [Avisos honestos](#10-avisos-honestos)
11. [Origem e adaptação](#11-origem-e-adaptação)

---

## 1. Instalação

Dois minutos, sem programar.

1. Baixe e descompacte [`anuncios-top-skills.zip`](anuncios-top-skills.zip) (ou clone este repo).
2. Copie as quatro pastas pra sua pasta de skills do Claude Code:

```bash
cp -R skills/* ~/.claude/skills/
```

3. Abra o Claude Code e digite `/video-ia`. Se ele fizer cinco perguntas, está instalado.

> **Windows / outro caminho:** a pasta é a que a sua instalação do Claude Code usa pra skills de
> usuário. Se você já tem outras skills, é a mesma pasta onde elas estão.

## 2. O que mais você precisa

| Pra quê | O que precisa | Obrigatório |
|---|---|---|
| Tudo | Claude Code | Sim |
| `/espiona-ads` e `/anuncio-edita` | `ffmpeg` e `ffprobe` | Sim pra essas duas |
| `/espiona-ads` (transcrição) | Chave da Groq em `GROQ_API_KEY` | Sim pra essa |
| Gerar imagem e vídeo a custo zero | Chave da Agnes em `AGNES_API_KEY` | Sim, se usar o provedor padrão |
| Legendas queimadas | Python com Pillow, só se o seu ffmpeg não tiver `libass` | Só nesse caso |
| Gerar em Seedance, Dreamina ou similar | Conta na plataforma; usa-se pela web | Não; pago à parte |

As chaves entram por variável de ambiente ou num `.env` na raiz do seu projeto:

```bash
export GROQ_API_KEY="sua-chave"
export AGNES_API_KEY="sua-chave"
```

Os scripts leem as chaves em runtime e nunca as imprimem nem copiam pra outro lugar.

## 3. A primeira coisa a fazer: a ficha de marca

As skills trabalham com **a sua** marca, e vêm com a ficha em branco de propósito.

Copie `skills/video-ia/marcas/_modelo.md` pra `anuncios/marcas/<sua-marca>.md` e preencha:

- o que se vende e o que se pede no fim do vídeo;
- pra quem, descrito como uma pessoa e não como segmento;
- a oferta com a redação exata;
- a prova que dá pra mostrar, com fonte;
- o tom, com uma frase real da marca;
- as proibições;
- identidade visual (a cor de acento vira a cor da palavra-chave nas legendas);
- caras e vozes disponíveis;
- plataforma de geração padrão.

Tem um exemplo preenchido em `_exemplo-oficina-do-bairro.md` (marca inventada). Quinze minutos,
uma vez só. Sem a ficha as skills funcionam, mas perguntam mais e os roteiros soam genéricos.

## 4. A cadeia de quatro decisões

| # | Decisão | Skill | O que entra | O que sai (documento pro próximo) |
|---|---|---|---|---|
| 1 | De onde vem a ideia | `/espiona-ads` | uma conta que já anuncia | playbook: hooks literais, ritmo medido, esqueleto persuasivo |
| 2 | Dirigir, não pedir | `/video-ia` | uma ideia (ou o playbook) + uma foto | 10 roteiros; por escolhido, um dossiê com imagens a criar, ordem de upload e prompts prontos |
| 3 | O que se salva e o que se refaz | `/auditor-video-ia` | o MP4 gerado | uma decisão: conservar, editar local, estender, salvar na montagem ou regenerar |
| 4 | Deixar pronto | `/anuncio-edita` | os módulos aprovados | master 1080×1920 + SRT |

Duas se usam sempre: a que busca a ideia e a que produz. As outras duas são opcionais e existem
pra economizar dinheiro quando você já está gerando.

**Regra que atravessa tudo:** o documento é a memória. Cada skill escreve um markdown e atualiza no
lugar, nunca duplica. Renomear ou criar "v2" quebra a cadeia.

**Nada se gera sem você.** Nenhuma das quatro gasta um centavo por conta própria: `/video-ia` deixa
os prompts e o botão quem aperta é você.

## 5. As skills, uma a uma

### `/espiona-ads`: espionar quem já está pagando

Você dá uma URL da Biblioteca de Anúncios da Meta (ou o nome de uma marca) e sai com a fórmula
desmontada: hooks literais, ritmo de corte medido, palavras por minuto, esqueleto persuasivo
minutado, e um veredito com evidência sobre se estão usando IA.

Seis fases: extração no navegador (a Meta bloqueia `curl`), ranking por dias em circulação e
variantes vivas (a Biblioteca não publica gasto nem CTR), processamento mecânico com ffmpeg e
Whisper, análise de frames com subagentes, contexto do funil (a landing), síntese.

O relatório termina com um bloco obrigatório: o que é transplantável, o que com cuidado, e o que
NÃO se copia. Copia-se a estrutura, nunca a mentira.

Arquivos: `skills/espiona-ads/SKILL.md`, `references/prompt-subagente.md`, `scripts/extrai.js`,
`scripts/processa.sh`.

### `/video-ia`: dirigir o vídeo, não pedir

O coração do sistema. Cinco passos, sem pular:

1. **Escuta a ideia.** Uma frase vaga, um playbook, ou um roteiro fechado.
2. **Cinco perguntas sobre a mensagem, de uma vez.** O que se vende, pra quem, o que a pessoa tem
   que pensar ao terminar, que prova existe, o que não se pode dizer. Nada técnico ainda.
3. **O menu de dez.** Dez conceitos com dez mecanismos diferentes, cada um com a cena em prosa,
   cold open, mini-roteiro com frases literais e tempo, onde vai a oferta, ritmo e risco. Padrão:
   3 UGC, 3 mini-ficção, 2 demonstração, 2 cinema. Depois do menu, PARA e pergunta quais desenvolver.
4. **O técnico, só dos escolhidos.** Duração, quem aparece (cinco vias de identidade), ritmo
   proposto, plataforma, idioma, e que material já existe.
5. **Um Markdown por vídeo**, com quatro blocos fixos: imagens a criar antes, roteiro pra ler em
   voz alta, o que subir e em que ordem, prompts pra copiar e colar.

O que a skill sabe, nas referências:

| Referência | O que cobre |
|---|---|
| `entrevista.md` | Os dois blocos de perguntas e por que não se misturam |
| `menu.md` | Como se constrói o menu de dez e as sete regras |
| `modos.md` | Catálogo de 21 modos (UGC, depoimento, demonstração, entrevista de rua, objeto que fala, mascote, escala impossível, POV, absurdo, cinema puro, letreiro em cena…) e o que vigiar em cada um |
| `cold-open.md` | Os três primeiros segundos: doutrina, seis mecanismos, teste de sete perguntas, anti-padrões |
| `ritmo.md` | Níveis de ritmo, orçamento de palavras por trilho, teto da interface, forma do ritmo, arquiteturas |
| `estilos.md` | Quatro blocos de textura (UGC de celular, mini-ficção, cinema, estilizado); escolhe um e cola inteiro |
| `identidade-e-voz.md` | As cinco vias: personagem inventado, cara real com referências, foto + áudio, voz off, gravar e transformar |
| `apresentador.md` | Ficha de apresentador em sete dimensões: a mesma cara em todos os anúncios |
| `referencias-de-identidade.md` | As três imagens de referência de uma pessoa real e os prompts pra gerá-las |
| `gravar-e-transformar.md` | Quinze segundos de celular viram outra cena mantendo cara, gestos e câmera |
| `direcao-de-plano.md` | Como se dirige um plano: geografia, atuação observável, câmera com motivo, escala como lock |
| `imagens.md` | O que se assa em imagem antes do vídeo: texto, logos, props, interfaces em HTML |
| `assets.md` | Bíblia visual: assets neutros, locação com look, último frame como ponte |
| `saida.md` | O formato exato do dossiê de saída |
| `adapters/` | Como o prompt se compila pra cada plataforma (ver seção 6) |

### `/auditor-video-ia`: auditar antes de gastar de novo

Recebe o prompt (preflight) ou o MP4 gerado (postflight) e devolve uma única decisão com motivo e
faixa de tempo exata:

```
DECISÃO: EDITAR LOCALMENTE
Porque: a identidade, o roteiro e o ritmo funcionam; só falha o produto entre 00:11–00:13.
Ação: substituir o produto nessa faixa e preservar câmera, atuação, luz e áudio.
Não tocar: hook, cara, timing, voz e CTA.
```

Hierarquia de reparação: conservar → editar localmente → estender → salvar na montagem →
regenerar. Não se regenera tudo por um objeto local. Um bloqueante (claim sem evidência, cara sem
consentimento, produto diferente do real, CTA ausente) impede publicar mesmo com nota alta no resto.

Inclui um checador mecânico de prompt:

```bash
python3 ~/.claude/skills/auditor-video-ia/scripts/checa-prompt.py prompt.txt --interface seedance25 --duracao 30
```

Pega colchetes sem preencher, prompt maior que a caixa, timestamps com buraco, planos sem
diálogo, sotaque errado e palavras de grading que devolvem preto e branco.

Arquivos: `references/preflight.md`, `postflight.md` (com tabela sintoma → causa → conserto),
`hierarquia-de-reparacao.md`, `publicacao-e-transparencia.md`, `assets/modelo-auditoria-video-ia.md`,
`assets/registro-experimentos.csv`.

### `/anuncio-edita`: montar a peça final

A doutrina: a melhor edição é a que não se nota. O material entra já dirigido; aqui se monta,
limpa e entrega. Sempre: montar módulos, pista de voz, legendas sóbrias, letreiro de fechamento,
master a 1080×1920 com loudness de plataforma. Tudo o mais é opcional e se propõe antes de fazer.

Legendas: pastilha escura, 2 a 4 palavras por página, palavra-chave na cor da marca, nível do
peito, nunca tapando uma cara. Dois caminhos pra queimar: `ass=` direto quando o ffmpeg tem
libass, ou overlay por PNG (Pillow) como fallback.

Scripts: `captions.py`, `jargon-fix.py`, `export-srt.py`, `master-audio.py`, `overlay-fallback/`.
Configuração do overlay por variáveis: `CAPTION_FONT` (fonte) e `KEYWORD_COLOR` (cor de acento).

Se o bruto foi **gravado com câmera** em vez de gerado, a montagem é outra skill
(`reel-edita-inema`), não esta.

## 6. Provedores e adaptadores

O método é neutro; o prompt final muda conforme onde você cola. Três adaptadores em
`skills/video-ia/references/adapters/`:

| Adaptador | Custo | Como se usa | O que faz |
|---|---|---|---|
| **Agnes por keyframes** (padrão) | zero | `AGNES_API_KEY` | Imagem (text2img e img2img) e vídeo por par de keyframes A→B, até 20 s por clipe em 720p. Só via D (voz off): a voz vem do inemavox ou gravada e se monta depois |
| **Seedance 2.5 multishot** | pago | pela web do provedor (TopView, Higgsfield, Magnific…) | Até 30 s com cortes dentro do prompt, referências de imagem, vídeo e áudio, diálogo com lip-sync |
| **Dreamina one-take / Seedance 2.0 modular** | pago | pela web | Uma tomada contínua de 30 s, ou módulos de 15 s pra montar |

Só a Agnes precisa de configuração. As demais funcionam colando o prompt na interface deles.

Os limites de cada modelo caducam rápido. Os adaptadores têm data; quando um número não bater com
o que você vê na tela, corrija o adaptador e siga.

## 7. Onde as skills escrevem

Por padrão, numa pasta `anuncios/` dentro do seu projeto. Não precisa criar: ela se cria sozinha.

```
anuncios/
├── marcas/                  a sua ficha de marca
├── roteiros/                os dossiês de cada peça (um markdown por vídeo)
├── criativos/               uma pasta por peça: módulos, master, SRT
├── _apresentadores/         fichas de continuidade e as três referências de identidade
└── referencias-criativas/   os relatórios do /espiona-ads
```

## 8. Estrutura do repositório

```
anunciostop/
├── README.md                    esta documentação
├── PLANO-CURSO.md               plano completo do curso (7 módulos, projeto-fio, adaptações)
├── anuncios-top-skills.zip      as 4 skills prontas pra download
├── skills/                      as 4 skills, fonte
│   ├── README.md                instalação resumida (vai na raiz do zip)
│   ├── espiona-ads/
│   ├── video-ia/
│   ├── auditor-video-ia/
│   └── anuncio-edita/
├── guia/                        landing + guia de uso (GitHub Pages)
├── fonte/                       material de origem e mapa módulo → arquivo (uso interno)
└── FALHAS.md                    changelog de falhas (uma linha por falha)
```

## 9. O curso

O plano completo está em [`PLANO-CURSO.md`](PLANO-CURSO.md). Resumo:

| Módulo | Tema | Entregável |
|---|---|---|
| 0 | Preparação: instalar as skills e preencher a ficha de marca | `anuncios/marcas/<marca>.md` |
| 1 | Espionar quem já está pagando | relatório de espionagem com banco de hooks |
| 2 | Dirigir, parte 1: da ideia ao menu de dez | menu com 2-3 conceitos escolhidos |
| 3 | Dirigir, parte 2: do conceito ao prompt | dossiê completo + três referências de identidade |
| 4 | Gerar e auditar antes de gastar de novo | auditoria preenchida + primeira linha do registro |
| 5 | Montar a peça final | master 1080×1920 + SRT |
| 6 | Publicar com cabeça e aprender com o quarto anúncio | registro com a próxima hipótese |

Um único anúncio atravessa os módulos 1 a 6 (o projeto-fio). No fim, a pasta `anuncios/` do aluno
é o portfólio do curso. Formato: INEMA `/formato-curso-v2`. Provedor das demonstrações: Agnes.

## 10. Avisos honestos

- **Gerar vídeo custa dinheiro** fora da Agnes, e se paga por segundo. `/auditor-video-ia` existe
  justamente pra você não regenerar cinco vezes o que se resolve na montagem.
- **Vídeo com IA não ganha sempre.** Em venda direta a frio, gravação a câmera pode converter
  melhor que avatar. Onde a IA ganha de lavada é no que não dá pra filmar: cenários impossíveis,
  sátira, metáfora física, volume. Se alguém disser que avatar vende sozinho, peça o número.
- **Cara ou voz de pessoa real só com permissão dela.** Nunca de terceiro. É o único limite das
  skills que não admite exceção.
- **Não invente prova.** Nem depoimento, nem resultado, nem número. Sem prova, demonstração com o
  que existe.

## 11. Origem e adaptação

O método vem de um minicurso em espanhol sobre anúncios com vídeo IA. Esta versão foi traduzida
e adaptada pro ecossistema INEMA:

- português do Brasil nos textos e nos prompts (com negativo contra deriva de sotaque);
- Biblioteca de Anúncios com país padrão BR;
- adaptador Agnes (custo zero) como provedor padrão, escrito a partir de medições reais da API;
- chaves carregadas em runtime, nunca copiadas;
- montagem de bruto gravado aponta pra `reel-edita-inema`;
- caminhos e fontes neutros (Linux, Mac, Windows);
- script de checagem de prompt escrito (o original citava um que não vinha no pacote);
- referências à fonte, anedotas datadas e números de conta alheia removidos; os valores que
  restaram são de referência, a validar com dados próprios.

Projeto de pesquisa e educação do INEMA.
