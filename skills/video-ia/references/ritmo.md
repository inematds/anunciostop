# Ritmo e arquitetura temporal

## Princípio

Ritmo é frequência de informação, não número de cortes. Escolhe-se por conceito e compila-se
conforme a interface.

| Nível | Mudança significativa | Uso habitual |
|---|---:|---|
| Frenético | 1–1,5 s | Listas, acumulação, UGC de alta energia |
| Dinâmico | 2–3 s | Demonstração e explicação |
| Medido | 4–5 s | Intriga, diálogo, revelação |
| Contemplativo | 6–8 s | Produto, escala, ASMR, metáfora |

Uma mudança significativa pode ser ação, olhar, objeto, som, informação ou transição. Um corte sem
motivo não acrescenta ritmo.

## O orçamento de palavras

> 🔴 Esta tabela não se mexe sem uma geração real que a contradiga. Comprimir o roteiro «pra
> caber» é o que deixa um anúncio de 25 s pedidos com 13 s reais e o resto em silêncio.

### Orçamento editorial · quanto roteiro a peça pede

| Trilho | Palavras por minuto | Por quê |
|---|---|---|
| **Voz off de cinema** | **126-160 ppm** | A imagem tem que respirar. Metade de um talking-head |
| **Mini-ficção · diálogo a dois** | **150-190 ppm** | Turnos curtos com micro-pausas entre falas. A pausa é atuação, não buraco |
| **UGC · talking-head · confessional** | **200-240 ppm** | Não há nada pra olhar: a voz preenche tudo |
| **Demonstração com apresentador** | **150-160 ppm** | Um apresentador cercado de interface diegética e objetos **não é talking-head**: a imagem carrega o tempo e a voz desce a ritmo de cinema |
| **Entrevista de rua · listas · acumulação** | **220-250 ppm** | O mecanismo é a avalanche |

Em palavras absolutas, com o trilho já decidido:

| Duração | Voz off de cinema | Mini-ficção | UGC / talking-head |
|---|---:|---:|---:|
| **15 s** | 32-40 | 38-48 | 50-60 |
| **30 s** | 63-80 | 75-95 | **100-120** |
| **60 s** | 126-160 | 150-190 | 200-240 |

Pra **demonstração com apresentador**: 38-40 palavras em 15 s · **75-80 em 30 s** · 150-160 em 60 s.
E é uma estrutura longa por natureza: funciona melhor em 60-100 s do que em 30.

Esses valores são de referência. Cada trilho se recalibra com a primeira geração real da conta:
mede-se quanto sobrou ou faltou e ajusta-se a linha, não o roteiro.

### 🔴 Teto da interface ≠ orçamento editorial

São duas coisas diferentes e confundi-las é o erro mais caro:

| | O que é | Exemplo |
|---|---|---|
| **Orçamento editorial** | Quantas palavras a peça **precisa** pra não deixar buracos. Quem decide é o trilho, acima | UGC de 30 s → 100-120 palavras |
| **Teto da interface** | A que velocidade **fala de fato** essa superfície. Quem decide é o provedor | Dreamina: 2,5-3,2 palavras/s = 150-192 ppm → em 30 s cabem 75-96 palavras |

**Quando o trilho pede mais do que a interface consegue dizer, não se corta o roteiro.** Escolhe-se,
nesta ordem:

1. subir a duração pedida;
2. partir em dois módulos e montar;
3. descer de trilho conscientemente (de talking-head pra mini-ficção, com algo pra olhar nos buracos);
4. mudar de superfície.

Cortar palavras até caber é exatamente o que deixa a peça pela metade. O adaptador de cada
interface declara o teto dela; ver `adapters/`.

### Silêncio deliberado vs buraco

Buscar **zero tempo morto, não zero silêncio**. Uma pausa vale se sustenta atuação, prova, tensão
ou som.

Em **UGC, dinâmico e frenético não se metem pausas sem conteúdo**: o buraco se preenche com
diálogo, planos ou golpes de som. Em **cinema sim**, mesmo que o ritmo seja dinâmico: uma maré
subindo, um corredor infinito, objetos chegando um a um; falar em cima estraga.

| | |
|---|---|
| ✅ **Silêncio deliberado** | Há **algo pra olhar** que come o trecho inteiro e o ambiente segue soando por baixo. A imagem é o evento |
| ❌ **Buraco** | Não acontece nada na tela e não se ouve nada. É tempo pago a zero |

> **O critério de honestidade:** se ao montar sobra silêncio, o problema é a imagem, não o texto.
> Não preencha com palavras. Se o plano não aguenta cinco segundos sozinho, o silêncio não é elegância.

⚠️ Se ao gerar **um plano concreto** ele sai picado e o lip-sync desmonta, ali sobra texto pra
esse plano, não pro roteiro inteiro.

## Quantos planos cabem, e com que forma

O número de planos por 30 s **é uma propriedade da superfície, não do modelo**. Uma interface
que executa cortes de verdade aguenta uma faixa; uma que produz one-take, outra. O adaptador de
cada uma declara a faixa medida, e ela se atualiza quando uma geração real a contradiz.

**Faixa de partida pra superfícies que executam cortes: 14-18 planos em 30 s.** Abaixo de ~12 lê-se
pausado pra um feed; acima de ~20 dobra a superfície de falha (cada corte é outra oportunidade de
deriva e de a geografia virar) e os planos de menos de um segundo voltam moles. Em superfícies
one-take, seguir com ~7 eventos até medir de novo.

### A forma importa mais que o número

Um ritmo plano não se arruma cortando mais rápido. **O contraste é o que retém, não a frequência.**

- **2-3 planos rápidos nos primeiros 3 s.** Ali se decide o scroll.
- **Uma rajada** de 3-4 cortes de ~1 s na virada da história.
- **Um ou dois planos sustentados de 4-5 s** que ganhem a duração com movimento interno: uma
  aproximação, um giro, uma mudança de foco. Um plano que segue entregando informação retém melhor
  que dois planos curtos mortos.
- **Um plano-assinatura:** o que alguém rebobinaria. Se não há nenhum, o plano de planos não está
  terminado. Ali vai o movimento mais ousado: um que impacte ganha de cinco espalhados.

Se todos os planos duram o mesmo, a peça não tem pulso. Um plano sustentado de 6 s que quebra em
três cortes de 1 s bate mais forte que qualquer um dos dois separados. **E se dá pra reordenar os
planos e a cena se lê igual, a câmera ainda não está contando nada.**

**Quando precisam de mais planos, acrescentar insertos e planos de recurso**, não partir trechos:
resetam a atenção a custo zero de continuidade, porque ninguém se move dentro da geografia.

### Piso de cobertura

Toda cena com trechos, falada ou muda, cumpre: **pelo menos dois planos da família primeiro plano**
(primeiro plano, primeiríssimo ou inserto), **pelo menos um plano de recurso** e **pelo menos dois
movimentos reais de câmera**. Não é decoração: o primeiro plano é onde se lê o que está em jogo, e
o plano de recurso é o reset de atenção mais barato que existe. O one-take e a montagem solta estão
isentos por desenho.

**E todo movimento de câmera se escreve como o resultado visível, não com jargão.** O modelo pode
não saber o que é um travelling de recuo; sempre sabe renderizar «a câmera se afasta enquanto ele
mantém o mesmo tamanho no quadro».

## Arquiteturas

### Multishot nativo

Pedir cortes e transições dentro do prompt quando a interface os executa. Manter uma ação
principal por plano e timestamps contíguos.

### One-take

Desenhar uma progressão dentro de uma só situação. O ritmo vive em movimento de sujeito/câmera,
gestos, descobertas, voz e som. Não pedir cortes impossíveis à superfície.

### Modular e montagem

Gerar módulos separados quando:

- o modelo base trabalha em 15-20 s;
- a interface não executa cortes;
- quer-se testar ganchos baratos;
- um contraplano ou locação exige outra geração.

Planejar estados de entrada/saída e locks literais. A montagem é uma rota válida, não um fracasso.
**É a arquitetura natural da Agnes:** clipes de até 20 s por keyframes, voz off montada em cima.

**Critérios pra partir uma passada longa em módulos com frame-ponte:**

1. **Partir não encarece:** paga-se por segundo gerado, então três trechos de 30 s custam o mesmo
   que 90 s seguidos. O que economiza é que uma nova tentativa só repete o trecho que falhou.
2. **A costura só vai onde o roteiro já corta**: mudança de cena, de plano ou de quem fala. Nunca
   no meio de um movimento contínuo: ali o extend nativo ganha sempre.
3. **Com voz clonada por timbre, cada módulo é uma voz nova** (mesmo timbre, variação audível). A
   costura de voz se esconde numa mudança de registro (coro→solo, cena→cena); no meio de um
   monólogo se nota.
4. **O módulo que se isola é o de mais risco** (multidões, clones, texto, transformação): que
   tentar de novo o trecho difícil custe os segundos dele, não a passada inteira. Esse módulo
   substitui a prova curta: se sai, é material de produção.
5. Antes de partir por um erro pontual, lembrar dos arranjos mais baratos: **edição localizada** e
   o **banco de remendos de voz**. → `assets.md` §Último frame como ponte.

### Extensão

O clipe inicial tem que funcionar sozinho e terminar vivo. O segundo movimento reabre, traz algo
novo e fecha de novo. Não estender uma revelação esgotada só pra preencher duração.

## Áudio

- Ancorar efeitos a ações, não a timestamps impossíveis de sincronizar.
- Definir ambiente e hierarquia em relação à voz.
- Escolher música ou silêncio a partir do brief; não impor.
- Manter o CTA completo.
- Distinguir cauda recortável de buraco central.

## Gate

- [ ] Nível de ritmo justificado.
- [ ] Trilho declarado e contagem de palavras dentro do orçamento editorial.
- [ ] Teto de fala da interface conferido; se o trilho não cabe, resolvido por duração ou módulos, não cortando roteiro.
- [ ] Cada trecho muda informação ou tensão.
- [ ] Arquitetura compatível com a interface.
- [ ] Número de planos dentro da faixa DESSA superfície.
- [ ] Ritmo com forma: abertura rápida, uma rajada na virada, um ou dois planos sustentados com
      movimento interno. Não um metrônomo.
- [ ] Piso de cobertura: dois primeiros planos, um plano de recurso, dois movimentos de câmera.
- [ ] Há um plano-assinatura identificado.
- [ ] Cada movimento de câmera escrito como resultado visível, não como jargão.
- [ ] Ações não competem dentro do mesmo plano.
- [ ] Estados de entrada/saída definidos nos módulos.
- [ ] Áudio sustenta os trechos sem voz.
- [ ] Versão curta funciona sozinha.
