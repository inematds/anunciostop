# Top Ads with AI

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

A four-decision system for turning an idea into an AI-generated video ad, ready
for Meta, without spending credits blindly. Four skills for Claude Code, in Portuguese, linked together:
each one does **one** thing and leaves a document for the next.

```
/espiona-ads        →  what's working out there and why
/video-ia           →  from your idea to 10 scripts; from the chosen one to a character sheet, model, and prompts
/auditor-video-ia   →  should this be kept, saved in the edit, or regenerated?
/anuncio-edita      →  the final piece, edited and mastered for Meta
```

**The thesis:** the prompt isn't the work. The work is choosing the angle, locking the identity,
directing the shot, and auditing before publishing. That's why the system remains useful when the
latest model changes.

- User guide: `guia/index.html` (published at `https://inematds.github.io/anunciostop/guia/en/`)
- Download the skills: [`anuncios-top-skills.zip`](anuncios-top-skills.zip)
- Course plan: [`PLANO-CURSO.md`](PLANO-CURSO.md)

---

## Index

1. [Installation](#1-instalação)
2. [What else you need](#2-o-que-mais-você-precisa)
3. [The first thing to do: the brand sheet](#3-a-primeira-coisa-a-fazer-a-ficha-de-marca)
4. [The chain of four decisions](#4-a-cadeia-de-quatro-decisões)
5. [The skills, one by one](#5-as-skills-uma-a-uma)
6. [Providers and adapters](#6-provedores-e-adaptadores)
7. [Where the skills write](#7-onde-as-skills-escrevem)
8. [Repository structure](#8-estrutura-do-repositório)
9. [The course](#9-o-curso)
10. [Honest caveats](#10-avisos-honestos)
11. [Origin and adaptation](#11-origem-e-adaptação)

---

## 1. Installation

Two minutes, no programming.

1. Download and unzip [`anuncios-top-skills.zip`](anuncios-top-skills.zip) (or clone this repo).
2. Copy the four folders to your Claude Code skills folder:

```bash
cp -R skills/* ~/.claude/skills/
```

3. Open Claude Code and type `/video-ia`. If it asks five questions, it's installed.

> **Windows / another path:** use the folder your Claude Code installation uses for user
> skills. If you already have other skills, use the same folder where they are.

## 2. What else you need

| For | What you need | Required |
|---|---|---|
| Everything | Claude Code | Yes |
| `/espiona-ads` and `/anuncio-edita` | `ffmpeg` and `ffprobe` | Yes, for these two |
| `/espiona-ads` (transcription) | Groq key in `GROQ_API_KEY` | Yes, for this one |
| Generate images and videos at no cost | Agnes key in `AGNES_API_KEY` | Yes, if using the default provider |
| Burned-in captions | Python with Pillow, only if your ffmpeg doesn't have `libass` | Only in that case |
| Generate with Seedance, Dreamina, or similar | Platform account; used on the web | No; paid separately |

Set the keys as environment variables or in a `.env` file at your project root:

```bash
export GROQ_API_KEY="sua-chave"
export AGNES_API_KEY="sua-chave"
```

The scripts read keys at runtime and never print them or copy them elsewhere.

## 3. The first thing to do: the brand sheet

The skills work with **your** brand, and intentionally come with a blank brand sheet.

Copy `skills/video-ia/marcas/_modelo.md` to `anuncios/marcas/<sua-marca>.md` and fill it in:

- what you sell and what you ask viewers to do at the end of the video;
- who it's for, described as a person rather than a segment;
- the offer, with its exact wording;
- the proof you can show, with its source;
- the tone, with a real sentence from the brand;
- the prohibitions;
- visual identity (the accent color becomes the keyword color in the captions);
- available faces and voices;
- default generation platform.

There's a completed example in `_exemplo-oficina-do-bairro.md` (an invented brand). Fifteen minutes,
once. The skills work without the sheet, but ask more questions and the scripts sound generic.

## 4. The chain of four decisions

| # | Decision | Skill | Input | Output (document for the next step) |
|---|---|---|---|---|
| 1 | Where the idea comes from | `/espiona-ads` | an account that already advertises | playbook: verbatim hooks, measured pacing, persuasive outline |
| 2 | Direct, don't request | `/video-ia` | an idea (or the playbook) + a photo | 10 scripts; for the chosen one, a dossier with images to create, upload order, and ready-to-use prompts |
| 3 | What to keep and what to redo | `/auditor-video-ia` | the generated MP4 | a decision: keep, edit locally, extend, save in the edit, or regenerate |
| 4 | Get it ready | `/anuncio-edita` | approved modules | 1080×1920 master + SRT |

Two are always used: the one that finds the idea and the one that produces it. The other two are optional and exist
to save money once you're already generating.

**The rule that applies throughout:** the document is the memory. Each skill writes a Markdown file and updates it in place; it never duplicates it. Renaming it or creating a "v2" breaks the chain.

**Nothing is generated without you.** None of the four spends a cent on its own: `/video-ia` leaves
the prompts, and you're the one who presses the button.

## 5. The skills, one by one

### `/espiona-ads`: spy on who's already paying

Give it a URL from the Meta Ad Library (or a brand name) and get the formula broken down: verbatim hooks, measured cut pace, words per minute, a timed persuasive outline, and an evidence-based verdict on whether they're using AI.

Six phases: browser extraction (Meta blocks `curl`), ranking by days running and active variants (the Library doesn't publish spend or CTR), mechanical processing with ffmpeg and Whisper, frame analysis with subagents, funnel context (the landing page), synthesis.

The report ends with a required section: what can be adapted, what needs care, and what must NOT be copied. Copy the structure, never the lie.

Files: `skills/espiona-ads/SKILL.md`, `references/prompt-subagente.md`, `scripts/extrai.js`,
`scripts/processa.sh`.

### `/video-ia`: direct the video, don't request it

The heart of the system. Five steps, no skipping:

1. **Listen to the idea.** A vague sentence, a playbook, or a finished script.
2. **Five questions about the message, all at once.** What is being sold, who it's for, what the person
   should think when they finish watching, what proof exists, and what can't be said. Nothing technical yet.
3. **The menu of ten.** Ten concepts with ten different mechanisms, each with a scene in prose,
   cold open, mini-script with exact lines and timing, where the offer goes, pacing, and risk. Default:
   3 UGC, 3 mini-fiction, 2 demonstrations, 2 cinema. After the menu, STOP and ask which ones to develop.
4. **The technical details, only for the chosen concepts.** Duration, who appears (five identity paths), proposed pacing, platform, language, and what materials already exist.
5. **One Markdown file per video**, with four fixed sections: images to create beforehand, script to read aloud, what to upload and in what order, prompts to copy and paste.

What the skill knows, in its references:

| Reference | What it covers |
|---|---|
| `entrevista.md` | The two question blocks and why they aren't combined |
| `menu.md` | How to build the menu of ten and the seven rules |
| `modos.md` | Catalog of 21 modes (UGC, testimonial, demonstration, street interview, talking object, mascot, impossible scale, POV, absurdity, pure cinema, on-screen lettering…) and what to watch for in each |
| `cold-open.md` | The first three seconds: doctrine, six mechanisms, seven-question test, anti-patterns |
| `ritmo.md` | Pacing levels, word budget per track, interface limit, pacing patterns, architectures |
| `estilos.md` | Four texture blocks (phone-shot UGC, mini-fiction, cinema, stylized); choose one and paste it in full |
| `identidade-e-voz.md` | The five paths: invented character, real person with references, photo + audio, voiceover, record and transform |
| `apresentador.md` | Presenter sheet across seven dimensions: the same face in every ad |
| `referencias-de-identidade.md` | The three reference images of a real person and prompts to generate them |
| `gravar-e-transformar.md` | Fifteen seconds of phone footage become another scene while preserving face, gestures, and camera |
| `direcao-de-plano.md` | How to direct a shot: geography, observable performance, motivated camera, scale as a lock |
| `imagens.md` | What to bake into an image before video: text, logos, props, HTML interfaces |
| `assets.md` | Visual bible: neutral assets, location with a look, last frame as a bridge |
| `saida.md` | Exact output dossier format |
| `adapters/` | How the prompt is compiled for each platform (see Section 6) |

### `/auditor-video-ia`: audit before spending again

It receives the prompt (preflight) or the generated MP4 (postflight) and returns a single decision with its reason and exact time range:

```
DECISÃO: EDITAR LOCALMENTE
Porque: a identidade, o roteiro e o ritmo funcionam; só falha o produto entre 00:11–00:13.
Ação: substituir o produto nessa faixa e preservar câmera, atuação, luz e áudio.
Não tocar: hook, cara, timing, voz e CTA.
```

Repair hierarchy: keep → edit locally → extend → save in the edit →
regenerate. Don't regenerate everything because of one local issue. A blocker (unsupported claim, face without consent, product differs from the real one, missing CTA) prevents publication even with a high score elsewhere.

Includes a mechanical prompt checker:

```bash
python3 ~/.claude/skills/auditor-video-ia/scripts/checa-prompt.py prompt.txt --interface seedance25 --duracao 30
```

It catches unfilled brackets, prompts longer than the input box, timestamp gaps, shots without dialogue, the wrong accent, and grading terms that turn the image black and white.

Files: `references/preflight.md`, `postflight.md` (with a symptom → cause → fix table),
`hierarquia-de-reparacao.md`, `publicacao-e-transparencia.md`, `assets/modelo-auditoria-video-ia.md`,
`assets/registro-experimentos.csv`.

### `/anuncio-edita`: assemble the final piece

The doctrine: the best edit is the one you don't notice. The footage comes in already directed; here it's assembled,
cleaned up, and delivered. Always: assemble modules, voice track, restrained captions, closing title,
1080×1920 master with platform loudness. Everything else is optional and proposed before doing.

Captions: dark pill, 2 to 4 words per card, keyword in the brand color, chest level,
never covering a face. Two ways to burn them in: `ass=` directly when ffmpeg has libass, or PNG overlay (Pillow) as a fallback.

Scripts: `captions.py`, `jargon-fix.py`, `export-srt.py`, `master-audio.py`, `overlay-fallback/`.
Overlay configuration via variables: `CAPTION_FONT` (font) and `KEYWORD_COLOR` (accent color).

If the raw footage was **shot with a camera** instead of generated, editing is handled by another skill
(`reel-edita-inema`), not this one.

## 6. Providers and adapters

The method is provider-neutral; the final prompt changes depending on where you paste it. Three adapters in
`skills/video-ia/references/adapters/`:

| Adapter | Cost | How to use it | What it does |
|---|---|---|---|
| **Agnes via keyframes** (default) | zero | `AGNES_API_KEY` | Images (text2img and img2img) and video from a pair of keyframes A→B, up to 20 s per clip at 720p. Voiceover only (path D): the voice comes from inemavox or is recorded, then added in the edit |
| **Seedance 2.5 multishot** | paid | through the provider's website (TopView, Higgsfield, Magnific…) | Up to 30 s with cuts inside the prompt, image, video, and audio references, dialogue with lip sync |
| **Dreamina one-take / Seedance 2.0 modular** | paid | through the web | One continuous 30 s shot, or 15 s modules to assemble |

Only Agnes needs configuration. For the others, paste the prompt into their interface.

Each model's limits change quickly. The adapters are dated; when a number doesn't match
what you see on screen, update the adapter and move on.

## 7. Where the skills write

By default, in an `anuncios/` folder inside your project. You don't need to create it; it's created automatically.

```
anuncios/
├── marcas/                  your brand sheet
├── roteiros/                dossiers for each piece (one Markdown file per video)
├── criativos/               one folder per piece: modules, master, SRT
├── _apresentadores/         continuity sheets and the three identity reference images
└── referencias-criativas/   /espiona-ads reports
```

## 8. Repository structure

```
anunciostop/
├── README.md                    this documentation
├── PLANO-CURSO.md               complete course plan (7 modules, through-line project, adaptations)
├── anuncios-top-skills.zip      the 4 skills ready to download
├── skills/                      the 4 skills, source
│   ├── README.md                short installation guide (goes in the zip root)
│   ├── espiona-ads/
│   ├── video-ia/
│   ├── auditor-video-ia/
│   └── anuncio-edita/
├── guia/                        landing page + user guide (GitHub Pages)
├── fonte/                       source materials and module → file map (internal use)
└── FALHAS.md                    failure log (one line per failure)
```

## 9. The course

The complete plan is in [`PLANO-CURSO.md`](PLANO-CURSO.md). Summary:

| Module | Topic | Deliverable |
|---|---|---|
| 0 | Preparation: install the skills and fill out the brand sheet | `anuncios/marcas/<marca>.md` |
| 1 | Spy on who's already paying | spy report with a hook bank |
| 2 | Direct, part 1: from the idea to the menu of ten | menu with 2-3 selected concepts |
| 3 | Direct, part 2: from concept to prompt | complete dossier + three identity reference images |
| 4 | Generate and audit before spending again | completed audit + first log entry |
| 5 | Assemble the final piece | 1080×1920 master + SRT |
| 6 | Publish thoughtfully and learn from the fourth ad | log with the next hypothesis |

A single ad goes through Modules 1 to 6 (the through-line project). At the end, the student's `anuncios/` folder
is the course portfolio. Format: INEMA `/formato-curso-v2`. Demo provider: Agnes.

## 10. Honest caveats

- **Video generation costs money** outside Agnes, and you're charged by the second. `/auditor-video-ia` exists
  so you don't regenerate five times what could be fixed in the edit.
- **AI video doesn't always win.** In cold direct-response sales, camera footage may convert
  better than an avatar. AI wins by a mile where you can't film the scene: impossible settings,
  satire, physical metaphor, volume. If someone says avatars sell themselves, ask for the numbers.
- **Use a real person's face or voice only with their permission.** Never use a third party's. This is the one limit
  on the skills that has no exceptions.
- **Don't invent proof.** No testimonials, results, or numbers. If there's no proof, demonstrate
  what exists.

## 11. Origin and adaptation

The method comes from a mini-course in Spanish about AI video ads. This version was translated
and adapted for the INEMA ecosystem:

- Brazilian Portuguese in the text and prompts (with a negative prompt against accent drift);
- Ad Library with BR as the default country;
- Agnes adapter (zero cost) as the default provider, built from real API measurements;
- keys loaded at runtime, never copied;
- editing of recorded raw footage points to `reel-edita-inema`;
- neutral paths and fonts (Linux, Mac, Windows);
- a prompt checker script was written (the original mentioned one that wasn't included in the package);
- references to the source, dated anecdotes, and someone else's account numbers removed; the
  remaining values are reference values to validate with your own data.

INEMA research and education project.
