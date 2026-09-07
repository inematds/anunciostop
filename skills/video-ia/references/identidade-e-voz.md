# As cinco vias de identidade

> Se aparece uma pessoa real, primeiro as três referências dela: `referencias-de-identidade.md`. A
> descrição escrita complementa as imagens; não substitui.

**Quem aparece e de onde sai a voz.** Muda blocos inteiros do prompt, então **se pergunta, não se
supõe.**

| Via | Quem aparece | De onde sai a voz | Dificuldade |
|---|---|---|---|
| **A · Personagem inventado** | Atores gerados que não existem | O modelo gera | 🟡 Média |
| **B · Cara real com referências** | Uma pessoa real, com as três imagens de referência | O modelo gera, com amostra de timbre ou sem | 🔴 Alta |
| **C · Foto + áudio animados** | Uma foto fixa de uma pessoa real, animada | **O áudio que você sobe.** Esse áudio É a pista | 🟢 Baixa |
| **D · Voz off** | Quem você decidir, ou ninguém | Uma voz gravada ou clonada, em cima de imagem gerada | 🟢 A mais baixa |
| **E · Gravar e transformar** | **A pessoa de verdade**, gravada com o celular, dentro de uma cena gerada | **A própria voz dela, gravada.** Não há lip-sync gerado | 🟢 Baixa |

**Cada vídeo declara a via antes de ser escrito.** «Tudo se gera, ninguém se grava» não é regra:
a via E existe justamente porque quinze segundos de celular resolvem o problema de os anúncios
serem contados por um desconhecido.

> 🔴 **Permissão.** As vias B, C e E usam a cara de uma pessoa real. Usam-se **só se essa pessoa
> autorizou**, e jamais com a cara de terceiro. Não é formalidade: é o único limite desta skill que
> não admite exceção.

---

## VIA A · Personagem inventado

O normal pra UGC, depoimentos e entrevistas de rua. Sem trâmites e sem permissões.

**O problema único desta via: a deriva.** Entre um plano e outro, a cara muda. O que evita é um
`[Character Reference]` obsessivamente concreto, e é o bloco que mais se negligencia.

```
[Character Reference (100% consistent, no drift throughout)]
——CARLA: 34, Brazilian, shoulder-length dark brown hair with visible split ends, tied back loosely
with two strands escaping on the left side. Small dark mole 2 cm below the left corner of her mouth.
Slightly uneven eyebrows, the right one higher. Faint acne scarring on both cheeks. Wearing a washed
grey cotton sweatshirt, collar slightly stretched, and a thin silver chain that stays visible in
every shot. Tired but warm energy — she speaks like she is telling a friend something she has not
told anyone yet. Her hair, her mole, her eyebrows, her sweatshirt and her chain must be identical in
every single frame of this video.
```

**As regras desta via:**
- **Três traços irrepetíveis no mínimo** (uma pinta, uma cicatriz, uma assimetria, um objeto que
  usa). Um personagem descrito como «mulher de 34 anos, cabelo castanho» sai diferente em cada plano.
- **O figurino se descreve uma vez e se fecha.** «Wardrobe is identical in every shot.»
- **Guarda-se o bloco literal** e reutiliza-se igual se o personagem voltar em outro vídeo. Se
  reescrever com outras palavras, é outra pessoa.
- **No máximo dois personagens com falas por vídeo.** Com três, a identidade desmonta.

## VIA B · Cara real com referências

Sobem-se as três referências da pessoa (`referencias-de-identidade.md`) e o diálogo vai **no prompt**.

Dois blocos obrigatórios. O primeiro, a identidade:

```
[Character Reference (100% consistent, no drift throughout)]
——<NOME> is the person in @Image1, @Image2 and @Image3. The face must be identical to the
reference in every single frame — same bone structure, same hairline, same skin
texture, same asymmetries. Identity consistency has absolute priority over everything else in this
prompt: if a shot cannot hold the face, hold the face and lose the shot.
```

⚠️ **Essa última frase é a que decide.** Sem ela, quando o modelo tem que escolher entre um
movimento de câmera bonito e a sua cara, **escolhe o movimento**.

E o segundo, a voz como referência de **timbre**:

```
[Voice Reference (timbre only — the reference audio is NOT part of this video)]
——<NOME>: use [Audio 1] as the voice reference. Take from it the timbre, the accent, the cadence,
the breathing pattern and the speech rhythm. [Audio 1] is a sample of real speech recorded for this
purpose: its words, its subject and its background are NOT content of this video. Do not reproduce,
quote, transcribe or play any part of [Audio 1]. Only the lines written in this prompt are spoken,
and they are spoken in the voice of [Audio 1].
Backup description in case the reference fails to load: <idade, gênero, sotaque>.
```

E **cada linha de diálogo leva o mapeamento explícito**, nunca implícito:

```
Dialogue (<NOME>, voice reference [Audio 1]): 'a fala, no idioma em que deve soar'
```

Mais, nos negativos:
```
Do not play, quote or transcribe any content from [Audio 1] — timbre reference only, never source
audio. <NOME>'s voice must match [Audio 1] in timbre, accent and cadence in every single shot,
with no drift between shots and no shift towards a neutral, European or generic Portuguese accent.
```

⚠️ **A última frase não é enfeite.** A **deriva pra um português neutro ou europeu é a primeira
coisa que quebra** quando o modelo perde a referência entre planos. As duas primeiras frases do
negativo são reforço defensivo (o nome do bloco já deveria bastar), mas custam zero. A terceira
ataca uma falha conhecida.

**A amostra de voz:** uma tomada limpa de 20-40 s, uma só voz, sem música nem ruído, **no registro
que você quer que ele replique**. Se gravar lendo devagar, ele vai falar devagar.

### 🔴 B1 vs B2 · o áudio que você sobe não significa o mesmo em cada plataforma

Confundir as duas manda produzir a amostra errada. **Confirmar a plataforma antes de gravar.**

| | O que é o áudio que você sobe | Onde vai o diálogo |
|---|---|---|
| **B1 · timbre** (Seedance «Real Human» e similares) | **Referência de timbre.** O conteúdo dele **não soa** no vídeo | Escrito no prompt |
| **B2 · pista** (OmniHuman, Dreamina e similares) | **A pista de voz definitiva.** É o que soa, e o lip-sync se faz sobre ela | No áudio, não no prompt |

Todo o bloco `[Voice Reference]` acima é **de B1**. Em B2 não se escreve: sobe-se a voz já locutada.

### Se ele grava a locução inteira · o que melhor funciona

É a via que melhor tem funcionado: entender primeiro a emoção do roteiro, gravar, e dar ao modelo
essa gravação e esse roteiro. Regras:

1. **O que gravou É o roteiro.** Ao gravar mudam-se frases; o `Dialogue` do prompt se copia do que
   ele disse, não do roteiro escrito.
2. **A peça dura o que a locução dura.** Não se preenche: o preenchimento é tempo morto pago.
3. **Se tiver que partir em trechos de ≤30 s, o áudio se corta só onde a voz dele cala**, e cada
   pedaço começa e termina em frase completa.
4. **A gravação original se guarda inteira**: se o clone de timbre não convence, monta-se a voz
   real em cima na montagem.
5. Ao gravar: cada trecho separado · duas ou três leituras · um segundo de ar de cada lado ·
   máxima qualidade do celular (no iPhone: Gravador → «Sem perda»; no Android: gravador em WAV ou
   qualidade máxima).

⚠️ Numa superfície B1 (timbre), o que soa é **o clone lendo o roteiro escrito**: por isso o passo 2
não é opcional. Se o prompt leva o roteiro velho, o vídeo diz o roteiro velho.

**Pra vários personagens** o bloco é o mesmo mudando o número (`[Audio 2]`, `[Audio 3]`), e o
mapeamento de qual áudio é de quem vai **explícito**: o implícito confunde identidades.

## VIA C · Foto + áudio animados

Sobe-se uma **foto fixa** e um **áudio**, e o modelo anima a cara sobre esse áudio.

🔴 **A diferença que tem que estar claríssima:** aqui **o áudio que você sobe SIM é o que soa.** Não
é referência de timbre: é a pista definitiva, e o lip-sync se faz sobre ela.

Consequências pro prompt:
- **Não se escreve bloco de referência de voz.** Não existe nesta via.
- **O diálogo não vai no prompt.** Vai no áudio. O texto só dirige **gesto, olhar e câmera**.
- **A foto fixa o fundo, o figurino e o enquadramento.** Não dá pra pedir mudança de cenário: se
  precisa de outro fundo, é outra foto.
- É **talking-head**. Não se pedem metáforas, nem escala, nem multi-plano.
- ⚠️ Os catálogos de voz dessas ferramentas **costumam ter português do Brasil**, mas com poucas
  vozes e todas reconhecíveis. Conte com subir áudio próprio, gravado ou clonado (inemavox).

**Quando é a melhor via:** uma mensagem direta a câmera, com a cara real de alguém, quando o
roteiro importa mais que a imagem. É a mais barata de acertar e a que menos surpreende.

## VIA D · Voz off

**Não significa «não aparece ninguém»: significa quem narra.** Pode se combinar com as demais; de
fato é a combinação que melhor tem funcionado: **narração em voz off sobre imagem de cinema, e a
cara real aparecendo no arremate.**

Ninguém mexe a boca *nas falas da voz off*.

**É a via mais segura do catálogo e a mais subestimada.** Ao eliminar o lip-sync desaparece de
uma vez a falha número um do vídeo gerado, e toda a qualidade do modelo vai pra imagem.

**É a via da Agnes.** A Agnes gera clipes mudos por keyframes; a voz vem do inemavox (TTS com voz
clonada) ou gravada, e se monta em cima no `/anuncio-edita`.

- Zero diálogo falado no quadro. O texto do prompt dirige gesto, olhar e câmera.
- Nos negativos: `No character on screen ever moves their lips to these lines.`
- A voz sai do bloco de timbre, ou se grava/sintetiza e se monta em cima.
- **Se o usuário grava e se monta depois** (a via que melhor tem funcionado): o vídeo se gera
  **sem diálogo** (só ambiente e efeitos, e assim se diz no bloco [AUDIO]), o roteiro vai no bloco
  2 do arquivo pra ele ler, e o orçamento de palavras é o de **voz off de cinema (126-160 ppm)**.
- 🟢 **Combinável:** pode aparecer uma cara real no quadro sem falar. Declara-se **em que plano
  aparece e se olha pra lente**, porque esse olhar costuma ser o arremate do vídeo.
- **É a via natural** do cinema, da metáfora, do POV, do ASMR, da demonstração, do produto herói e
  do detalhe artesanal.

⚠️ Se o roteiro **precisa** que se veja alguém dizendo a câmera (depoimento, confessional), a voz
off sozinha não serve: precisa de B, C ou E.

## VIA E · Gravar e transformar

**Gravam-se dez ou quinze segundos com o celular e o modelo os converte em outra cena**, mantendo
a cara, os gestos e o movimento de câmera de quem gravou. Um só prompt.

Resolve o problema clássico dos lotes de avatar: produção boa e **zero reconhecimento**. Se o que
vende o negócio é que ensina uma pessoa concreta, o anúncio não pode ser contado por um ator de banco.

| | |
|---|---|
| **O que ganha** | É a pessoa de verdade, e **desaparece o lip-sync gerado**, que é a falha nº 1: a boca é a dela, gravada |
| **O que custa** | Quinze segundos e um celular |
| **O que não pode** | Dar gestos que não fez, movê-la pelo plano, nem alongar o clipe. A coreografia é a que se gravou |

**Tem arquivo próprio, porque o delicado é como se grava o bruto:**
→ 🔴 **`gravar-e-transformar.md`**

---

## Como escolher, numa tabela

| O que você quer | Via |
|---|---|
| UGC, depoimento, entrevista de rua com gente que não existe | **A** |
| Uma pessoa concreta num plano impossível: escala, clones, VFX | **B** |
| Uma pessoa concreta da equipe falando a câmera e ponto | **C** |
| 🟢 **Uma pessoa concreta da equipe, com a voz DELA, numa cena que não existe** | **E** |
| Cinema, metáfora, escala, POV, ASMR, objeto, mascote | **D**, e a cara real no arremate |
| Demonstração de produto | **D** |
| Máxima qualidade de imagem com o mínimo risco | **D** ou **E** |
| Custo zero, na Agnes | **D** (única via que a Agnes suporta) |

## E a regra que resume tudo

**Cada boca que se mexe GERADA é um ponto de falha.** Se o conceito funciona sem lip-sync gerado
(voz off, ou a boca gravada de verdade na via E) o vídeo melhora.

🔴 **E a regra que economiza gerações:** se o vídeo dá pra gravar e publicar como está, grava-se e
publica-se. **A geração se paga quando faz o impossível.**
