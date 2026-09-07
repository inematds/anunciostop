# Anúncios Top com IA · Plano de curso

> **Base do plano:** o pacote de 4 skills + a página de apresentação recebidos em 2026-09-06.
> As aulas em vídeo da comunidade de origem não estavam acessíveis; o plano foi construído a partir
> do material escrito, que é onde o método está documentado por inteiro.
>
> **Referências removidas:** o plano não cita a academia, a comunidade, o autor, a marca do
> minicurso original nem a marca fictícia de exemplo. Números de conta alheia (custo por compra,
> custo por aquisição, planos contados em vídeos de terceiros) foram retirados ou marcados como
> *valor de referência a validar com dados próprios*. O método fica; a atribuição sai.

---

## 1 · Posicionamento

**Nome de trabalho:** Anúncios Top com IA
**Promessa:** sair com um sistema de quatro decisões que transforma uma ideia em um anúncio em vídeo
gerado por IA, pronto pra Meta, sem gastar crédito às cegas.
**Tese do curso:** o prompt não é o trabalho. O trabalho é decidir o ângulo, congelar a identidade,
dirigir o plano e auditar antes de publicar. Cada decisão tem dono, cada dono deixa um documento
escrito pro próximo. Por isso o sistema continua valendo quando o modelo da moda mudar.

**Público:** quem já anuncia (ou vai anunciar) na Meta e quer produzir criativos em vídeo com IA
sem virar editor de vídeo. Dono de negócio, gestor de tráfego, criador de conteúdo, freelancer de
marketing. Sabe o que vende e pra quem. Não precisa saber programar.

**O que o aluno leva:**
- 4 skills instaladas no Claude Code, em português, encadeadas.
- Uma ficha de marca preenchida (o ativo que faz os roteiros deixarem de soar genéricos).
- Uma ficha de apresentador com três referências de identidade (a mesma cara em todos os anúncios).
- Um anúncio completo produzido durante o curso: do espionagem ao master 1080×1920 com SRT.
- Um registro de experimentos com a primeira linha preenchida.

**Pré-requisitos e custos, ditos na primeira aula:**
| Item | Necessário pra | Custo |
|---|---|---|
| Claude Code | tudo | assinatura |
| ffmpeg + ffprobe | espionagem e montagem | grátis |
| Chave Groq (transcrição) | espionagem | centavos |
| Python + Pillow | legendas queimadas, se o ffmpeg não tiver libass | grátis |
| Conta na ferramenta de vídeo (Seedance, Dreamina ou similar) | gerar o vídeo | **pago por segundo gerado** |

As skills não gastam crédito sozinhas. O botão de gerar é sempre do aluno.

---

## 2 · A espinha do curso: a cadeia de quatro decisões

| # | Decisão | Skill | O que entra | O que sai (documento pro próximo) |
|---|---|---|---|---|
| 1 | De onde vem a ideia | `/espiona-ads` | uma conta que já anuncia | playbook: hooks literais, ritmo medido, esqueleto persuasivo |
| 2 | Dirigir, não pedir | `/video-ia` | uma ideia (ou o playbook) + uma foto | 10 roteiros; por escolhido, um dossiê com imagens a criar, ordem de upload e prompts prontos |
| 3 | O que se salva e o que se refaz | `/auditor-video-ia` | o MP4 gerado | uma decisão: conservar, editar local, estender, salvar na montagem ou regenerar |
| 4 | Deixar pronto | `/anuncio-edita` | os módulos aprovados | master 1080×1920 + SRT |

Duas se usam sempre: a que busca a ideia (1) e a que produz (2). As outras duas são opcionais e
existem pra economizar dinheiro quando já se está gerando: uma decide o que se salva (3), a outra
monta a peça final (4). O curso segue essa ordem porque é a ordem em que o dinheiro é gasto.

**Regra que atravessa tudo:** o documento é a memória. Cada skill escreve um markdown e atualiza no
lugar, nunca duplica. Renomear ou criar "v2" quebra a cadeia.

---

## 3 · Módulos

Duração total estimada: **7 h de aula** (430 min somados) + **4 a 6 h de prática** do aluno. Formato: vídeo-aula
curta por tópico (8 a 15 min) + exercício com entregável verificável.

### Módulo 0 · Preparação (45 min)

**Objetivo:** instalar as skills e criar o único ativo que o curso exige antes de começar: a ficha de marca.
**Conteúdo:**
- Instalação das 4 skills (copiar pastas, testar com `/video-ia`; se fizer cinco perguntas, funcionou).
- Dependências: ffmpeg, chave Groq (transcrição), chave Agnes (imagem e vídeo a custo zero),
  Python. Onde cada uma é usada e onde não é. As demais plataformas não precisam de chave: usam-se
  pela web.
- A pasta `anuncios/`: roteiros, criativos, apresentadores, referências. Se cria sozinha.
- **A ficha de marca:** o que se vende e o que se pede no fim do vídeo; o público descrito como uma
  pessoa e não como segmento; a oferta com redação exata; a prova que dá pra mostrar; o tom com uma
  frase real; as proibições; identidade visual; caras e vozes disponíveis.
- Dois avisos honestos: gerar vídeo custa dinheiro; os limites de cada modelo caducam rápido e os
  adaptadores têm data.
**Exercício:** preencher a ficha de marca da própria empresa (15 min, uma vez).
**Entregável:** `anuncios/marcas/<marca>.md` preenchido.

### Módulo 1 · Espionar quem já está pagando (60 min)

**Objetivo:** sair de uma conta concorrente com a fórmula desmontada, sem pagar nada e sem inventar.
**Conteúdo:**
- O que a Biblioteca de Anúncios da Meta mostra e o que esconde (não publica gasto, impressões nem CTR).
- As três proxies de "está funcionando": dias em circulação, número de variantes vivas, repetição de estrutura.
- As seis fases: extração no navegador, ranking, processamento mecânico (cortes, palavras por minuto,
  transcrição), análise de frames com subagentes, contexto do funil (a landing), síntese.
- Deduplicar por asset de vídeo antes de baixar: 16 anúncios podem ser 1 vídeo.
- O relatório: veredito "é IA ou não" com evidência visual, clusters de campanha, como iteram, ritmo
  medido, banco de hooks literais, fórmula do vencedor minutada, incoerências anúncio × landing.
- **O bloco obrigatório:** o que é transplantável, o que é com cuidado, o que NÃO se copia. Copia-se
  a estrutura, nunca a mentira.
- Erros que já foram cometidos: curl bloqueado, endpoint antigo retirado, API oficial só cobre
  anúncios políticos, o campo "mídia criada digitalmente" é declaração, não detector.
**Exercício:** rodar a skill em um concorrente real do aluno (país padrão BR).
**Entregável:** `anuncios/referencias-creativas/espionagem-<marca>-<data>.md` com banco de hooks.

### Módulo 2 · Dirigir o vídeo, parte 1: da ideia ao menu de dez (75 min)

**Objetivo:** entender por que a variedade real vem do mecanismo e não do cenário, e aprender a
escolher um conceito antes de escrever qualquer prompt.
**Conteúdo:**
- A entrevista em dois blocos e por que não se misturam: perguntar duração ou avatar antes das ideias
  transforma dez conceitos em dez talking-heads.
- As cinco perguntas sobre a mensagem: o que se vende e o que se pede; pra quem (duas frases, não um
  segmento); o que a pessoa tem que PENSAR ao terminar; que prova existe; o que NÃO se pode dizer.
- Sem prova, não se usa depoimento: usa-se demonstração com o que existe.
- **Mensagem → mecanismo → modo**, nessa ordem. Começar pelo modo é o erro caro: "vamos fazer um de
  cinema" produz um vídeo bonito sem mecanismo.
- O catálogo de 21 modos (UGC selfie, depoimento, demonstração, entrevista de rua, confessional,
  documentário de dados, diálogo a dois, mini-drama, metáfora de escala impossível, objeto que fala,
  mascote, mundo alterado, ASMR, POV impossível, transformação impossível, absurdo, cinema puro,
  analogia literal, produto herói, detalhe artesanal, letreiro em cena) e o que vigiar em cada um.
- A distribuição padrão do menu: 3 UGC · 3 mini-ficção · 2 demonstração · 2 cinema, e por quê
  (as caras inventadas saem naturais; demonstração é o que mais converte; o caro de gerar não é o
  que mais vende). Quebra-se assim que o aluno pedir.
- A ficha de cada conceito: nome dizível em voz alta, a cena em prosa, cold open, onde vai a oferta,
  mini-roteiro com frases literais e tempo, por que morde, ritmo, "se alonga a 60 s por", risco.
- **O cold open como comporta:** nos três primeiros segundos tem que ACONTECER algo; ninguém abre
  com uma cara falando; áudio no frame zero; tem que se entender no mudo. Os seis mecanismos de
  gancho, o teste de sete perguntas, os cinco anti-padrões.
- Onde vai a oferta: padrão na primeira frase (o olho para no objeto, o ouvido para na oferta),
  opcional no fechamento. O que não muda é que ela exista.
- Depois do menu, PARA. "Quais desenvolvo?" Nunca se escreve prompt sem menu.
**Exercício:** rodar `/video-ia` com uma ideia própria até o menu de dez; tapar nome e cenário de
cada ficha e contar mecanismos distintos (menos de seis, reescreve).
**Entregável:** menu de dez com 2 ou 3 conceitos escolhidos e justificados.

### Módulo 3 · Dirigir o vídeo, parte 2: do conceito ao prompt (90 min)

**Objetivo:** produzir, por conceito escolhido, um dossiê com tudo que a ferramenta precisa e nada
que ela não precisa.
**Conteúdo:**
- O bloco técnico da entrevista: duração (sempre se pergunta; padrão 30 s), quem aparece, ritmo
  (proposto por conceito, não perguntado em aberto), plataforma, idioma, e a pergunta obrigatória:
  **que material já existe?**
- **As cinco vias de identidade** e o que cada uma muda no prompt:
  A personagem inventado (três traços irrepetíveis, figurino fechado, bloco literal guardado);
  B cara real com três referências (a frase de prioridade absoluta de identidade; áudio como
  referência de timbre versus áudio como pista definitiva, conforme a plataforma);
  C foto + áudio animados; D voz off (a via mais segura: sem lip-sync, toda a qualidade vai pra
  imagem); E gravar e transformar (quinze segundos de celular viram outra cena mantendo cara, gesto
  e câmera).
- A regra que resume: cada boca gerada é um ponto de falha. Se dá pra gravar e publicar, grava e
  publica. Geração se paga quando faz o impossível.
- **Permissão:** cara ou voz de pessoa real só com autorização dela. Nunca de terceiro. É o único
  limite sem exceção.
- A ficha de apresentador (sete dimensões) e as três referências de identidade: close, folha de
  personagem, rosto + corpo inteiro. A prova de cinco segundos antes de gastar na peça.
- **Ritmo:** frequência de informação, não número de cortes. Os quatro níveis (frenético, dinâmico,
  medido, contemplativo). Orçamento de palavras por trilha (voz off de cinema, mini-ficção, UGC,
  demonstração com apresentador, lista). Teto da interface ≠ orçamento editorial: quando não cabe,
  sobe a duração ou parte em módulos, nunca corta o roteiro.
- A forma do ritmo: abertura rápida, uma rajada na virada, um ou dois planos sustentados com
  movimento interno, um plano-assinatura. Metrônomo não retém.
- **Textura:** quatro blocos (UGC de celular, mini-ficção, cinema, estilizado). Escolhe um, cola
  inteiro, nunca mistura. O erro clássico: prefixo de cinema num UGC vira anúncio de carro.
  Cores nomeadas em positivo. Look derivado do assunto, não herdado do projeto anterior.
- Dirigir o plano: geografia declarada, atuação traduzida em ação observável, câmera com motivo,
  movimento escrito como resultado visível e não como jargão, escala como lock.
- **O que se assa em imagem:** todo texto legível, logo, tela ou cartaz vira imagem de referência
  aprovada letra a letra antes do vídeo. Interfaces fictícias se maquetam em HTML e se capturam.
  Produto real usa a imagem real. Uma referência de estado final não produz sequência.
- Adaptadores por plataforma: **Agnes por keyframes (padrão do curso, custo zero)**: só via D,
  par de imagens A e B por clipe de até 20 s em 720p, voz sintetizada ou gravada montada depois;
  multishot de até 30 s (faixa de planos, timestamps contíguos, toda a locução escrita plano a
  plano, final vivo pra estender); one-take (um cenário, um vetor de câmera, até quatro ações,
  diálogo contínuo); modular de 15 s (locks literais, estados de entrada e saída).
- O dossiê de saída: quatro blocos fixos, sempre presentes. Imagens a criar antes; roteiro pra ler em
  voz alta; o que subir e em que ordem (a ordem de upload É o binding); prompts pra copiar e colar,
  um por trecho de até 30 s.
- Nunca entregar um colchete: o gerador renderiza literal.
**Exercício:** desenvolver um dos conceitos escolhidos até o dossiê completo; criar as três
referências de identidade se o aluno vai aparecer.
**Entregável:** `anuncios/roteiros/<data>-<conceito>.md` com os quatro blocos preenchidos + as três
referências em `anuncios/_presentadores/<nome>/`.

### Módulo 4 · Gerar e auditar antes de gastar de novo (60 min)

**Objetivo:** transformar "ficou estranho" numa decisão única, com motivo e faixa de tempo exata.
**Conteúdo:**
- Gerar o primeiro trecho na plataforma escolhida (aula demonstrada ao vivo, com o custo dito na tela).
- Preflight: reconstruir o contrato do dossiê; checar roteiro, claim, CTA, duração, consentimento,
  bindings, bytes, timeline, continuidade, texto crítico, custo, variável de teste, disclosure.
  Só o perfil da interface declarada; regras de uma não se aplicam a outra.
- Postflight técnico: metadados reais com ffprobe; amostragem visual (primeiro frame, fim do cold
  open, cada corte, último frame); gates de identidade, mãos, boca, figurino, produto, texto,
  continuidade, física, câmera, fundo; gate de áudio.
- Postflight comercial: ver no mudo e em tamanho de celular. O público se reconhece? O mecanismo se
  entende sem ler o brief? A prova aparece? A marca é trocável por qualquer outra?
- Severidade: bloqueante, maior, local, cosmético. Um bloqueante impede publicar mesmo com nota alta
  no resto.
- **A hierarquia de cinco decisões:** conservar → editar localmente → estender → salvar na montagem
  → regenerar. Não se regenera tudo por um objeto local. Não se salva na montagem um mecanismo que
  não se entende.
- Diagnóstico sintoma → causa → arranjo: cinza de estúdio no plano, tudo igual ao projeto anterior,
  volta em preto e branco, cara deriva do plano 5 em diante, sala muda de forma entre cortes,
  objetos teleportam, contraplanos trocam de lado, luz morta.
- Em prova de baixa resolução não se julga realismo nem texto: só movimento, continuidade e lógica.
- Uma variável por teste. Se mudou duas, o aprendizado ficou contaminado e isso se registra.
**Exercício:** auditar o próprio trecho gerado e emitir o veredito no formato
`DECISÃO / Porque / Ação / Não tocar`.
**Entregável:** auditoria preenchida + primeira linha do registro de experimentos.

### Módulo 5 · Montar a peça final (60 min)

**Objetivo:** juntar os módulos sem que as costuras apareçam e entregar o master pra Meta.
**Conteúdo:**
- A doutrina: a melhor edição é a que não se nota. O material já entra dirigido; aqui se monta,
  limpa e entrega. Motion graphics em cima de vídeo gerado delatam a geração.
- Ingestão e diagnóstico: ffprobe de cada arquivo, transcrição, frames, localizar o dossiê,
  perguntar só o que falta (pista de voz, letreiro de fechamento, substituições).
- Montagem: ordenar pelo roteiro (a transcrição diz qual módulo é qual, não o nome do arquivo),
  cortar caudas contra o áudio, uniformizar, corte seco na costura, crossfade só no ambiente.
- Pista de voz: clone do vídeo (padrão), remendo de uma palavra, ou gravação original alinhada por
  timing de palavra.
- Legendas: sempre, e sóbrias. Pastilha escura, 2 a 4 palavras por página, palavra-chave na cor da
  marca. Nível do peito, nunca no terço inferior, nunca tapando uma cara. Ler o arquivo de legendas
  inteiro antes de queimar: um erro de transcrição na tela é um anúncio queimado.
- Letreiro de fechamento sobre o vídeo vivo, sem end card preta, sem freeze. Corner-pin de tela
  quando o render sujou uma tela assada.
- Master: loudness de plataforma social, H.264, 1080×1920, fps do material.
- O menu de intervenções opcionais e o critério: quase sempre sim (trim de caudas, crossfade de
  ambiente, SRT); às vezes (SFX diegético, realce do plano-assinatura, música só se o brief pediu);
  quase nunca (zoom digital, transições, emojis, filtros de look, speed ramp).
- O teste final do editor: a edição se nota? cada acréscimo tem um porquê de uma frase? passaria por
  vídeo gravado com celular por alguém de bom olho?
**Exercício:** montar o anúncio do curso a partir dos módulos aprovados.
**Entregável:** `anuncios/creativos/<slug>/<nome>.mp4` + SRT ao lado + registro no dossiê.

### Módulo 6 · Publicar com cabeça e aprender com o quarto anúncio (40 min)

**Objetivo:** fechar o ciclo: transparência, registro e o que faz o quarto anúncio funcionar melhor
que o primeiro.
**Conteúdo:**
- Gate de verdade: não inventar depoimento, cliente, evento, número. Não apresentar avatar como
  membro real. Não mostrar função que o produto não tem. Não trocar o produto real por versão diferente.
- Consentimento separado pra cara, voz, contexto, campanha e reuso. Foto pública não é consentimento.
- Transparência: quando a peça realista pode ser confundida com gravação autêntica, usar disclosure
  claro, ativar as opções de IA da plataforma, não desenhar o aviso pra passar despercebido.
  Verificar a regra vigente no país e a configuração da Meta antes de publicar. Não substitui
  assessoria jurídica.
- O registro de experimentos: decisão, custo, tentativa, variável mudada, resultado. Sem isso não se
  aprende, se repete.
- **Aviso honesto do curso:** vídeo com IA não ganha sempre. Em venda direta a frio, gravação a câmera
  pode converter melhor que avatar. Onde a IA ganha de lavada é no que não dá pra filmar: cenários
  impossíveis, sátira, metáfora física, volume. Se alguém disser que avatar vende sozinho, peça o
  número. O aluno vai medir com o próprio anúncio.
- O que fazer com o segundo anúncio: mesma cara, outra cena; mesmo mecanismo, outro gancho; uma
  variável por vez.
**Exercício:** preencher o registro com o anúncio do curso e planejar a variável do segundo.
**Entregável:** registro de experimentos com duas linhas: a peça feita e a próxima hipótese.

---

## 4 · Projeto-fio

Um único anúncio atravessa os módulos 1 a 6. O aluno escolhe a marca no módulo 0, espiona um
concorrente no 1, gera o menu no 2, fecha o dossiê no 3, gera e audita no 4, monta no 5 e registra
no 6. Cada módulo termina com um arquivo que o seguinte lê. No fim, a pasta `anuncios/` do aluno é
o portfólio do curso.

Pra demonstração nas aulas, o curso precisa de **exemplos próprios**: uma marca de exemplo
preenchida, um menu de dez real, um dossiê completo, três referências de identidade, ao menos dois
trechos gerados (um bom, um com falha auditável) e o master final. Os vídeos de demonstração da
fonte não vieram no pacote; todos os exemplos serão produzidos pra este curso.

---

## 5 · Adaptação Brasil / INEMA

Mudanças explícitas em relação ao material de origem:

| Origem | Neste curso |
|---|---|
| Espanhol, sotaque castelhano nos prompts | Português do Brasil; linha de negativo contra deriva de sotaque (neutro, lusitano) |
| Biblioteca de Anúncios país padrão ES | País padrão BR |
| Regulação europeia citada por artigo | "Verificar regras locais vigentes e opções de IA da plataforma"; sem citar lei específica |
| Chave de transcrição em `.env.local` | Carregada em runtime do `.env` central do usuário, nunca copiada |
| Montagem de material gravado a câmera aponta pra skill externa | Aponta pra `reel-edita-inema` |
| Caminhos e instalação só pra Mac (brew, fontes do sistema) | Instruções neutras Linux/Mac/Windows; fonte da marca embarcada |
| Cor de destaque das legendas fixa | Cor de acento da marca do aluno, vinda da ficha |
| Nomes de skill em espanhol | Nomes em português: `/espiona-ads`, `/video-ia`, `/auditor-video-ia`, `/anuncio-edita` (dois já servem) |
| Pasta `anuncios/guiones` | `anuncios/roteiros` |
| Ficha de marca dentro da pasta da skill | `anuncios/marcas/<marca>.md`, junto dos outros documentos do aluno |
| Só adaptadores pagos (Seedance, Dreamina) | Adaptador **Agnes por keyframes** como padrão (custo zero, via D); os pagos continuam como complemento |
| Legendas com ffmpeg sem libass (só overlay por PNG) | Dois caminhos: `ass=` direto quando o ffmpeg tem libass, overlay por PNG como fallback |
| Script de checagem de prompt citado mas ausente | `auditor-video-ia/scripts/checa-prompt.py` escrito: colchetes, bytes, timestamps, planos mudos, sotaque, grading |

---

## 6 · Lacunas e decisões em aberto

**Lacunas do material recebido (o curso precisa cobrir por conta própria):**
- As aulas em vídeo originais não estavam acessíveis. Se ficarem, servem só pra conferir ênfase;
  o conteúdo escrito já é completo.
- Os MP4s de demonstração não vieram. Exemplos serão produzidos.
- O auditor cita um script de checagem de prompt que não está no pacote. Ou se escreve, ou se tira
  a referência.
- A skill de espionagem depende de um navegador integrado ao agente; no INEMA, mapear pra
  `agent-browser` ou pra extensão do Chrome.
- A skill de montagem foi feita pra um ffmpeg sem libass; conferir o ffmpeg do aluno e oferecer os
  dois caminhos.

**Decisões tomadas (2026-09-06):**
- Formato do curso: `/formato-curso-v2` (dark âmbar + camada de aprendizagem).
- Nome: "Anúncios Top com IA"; repo `inematds/anunciostop`.
- As 4 skills traduzidas entram como material de download (`anuncios-top-skills.zip`) e como
  instalação guiada no módulo 0.
- Provedor padrão das demonstrações: **Agnes** (custo zero, via D por keyframes), configurada via
  `AGNES_API_KEY`. Seedance 2.5 e Dreamina ficam como adaptadores de aula complementar, usados pela
  web do provedor, sem nada configurado no `.env`.

**Próximos passos, em ordem:**
1. Traduzir e adaptar as 4 skills pra PT-BR (é o material do módulo 0 e a base das demos). As
   frases de doutrina do texto de origem são reescritas na voz INEMA, não só traduzidas.
2. Produzir os exemplos do projeto-fio.
3. Montar o curso no formato escolhido.
4. Guia do projeto (`guia/index.html`) e publicação no portal.
