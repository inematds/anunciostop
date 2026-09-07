# Bíblia visual e manifesto de assets

## Princípio

Construir o set antes de gerar. Uma referência vinculada e aprovada controla melhor que uma longa
descrição. Mesmo assim, toda referência precisa de um binding que diga o que pegar e o que ignorar.

🔴 **E nunca regenere uma referência que funciona.** As especificações deste sistema são
**critérios de construção, não comportas de aceitação**. Um asset que chega pronto (do usuário, de
um cliente, de uma sessão anterior) se julga pela função: cumpre o trabalho dele? Se sim, **usa-se
como está**. Cada regeneração se afasta do original, e o que já funciona é a verdade.

## 🔴 A lei: os assets são neutros, a locação leva o look

Um asset de identidade é uma *especificação*, não um plano: fundo cinza médio, luz plana sem
sombra, zero grading. Uma locação é o contrário: **gera-se no look real da peça, porque o trabalho
dela é fornecer a luz.** O modelo casa as duas coisas: reilumina o personagem neutro dentro do
espaço já iluminado.

Ao contrário, o pipeline se envenena em silêncio: se você assa tungstênio quente na folha de
personagem na segunda-feira, **tudo que gerar naquele mês herda**, inclusive as cenas ao meio-dia
em exterior. E você não vai achar a causa, porque a folha parece perfeita separada.

Daí sai o mecanismo que faz plate e vídeo final estarem graduados igual: **o bloco de
textura/look se copia literal, a mesma frase, no prompt da locação e no do vídeo.** Uma frase,
usada duas vezes.

**E não confundir os dois diais:**

| Dial | O que é | Onde vai |
|---|---|---|
| **Look / grade** | Cor, luz, clima | Na locação e no prompt do vídeo. **Nunca** num asset de identidade |
| **Textura / estilo** | O meio: celular, mini-ficção, cinema, 3D, anime | Em **tudo**: cada asset, cada plate e o vídeo, com a mesma frase literal. É identidade, não clima |

Uma folha fotorrealista não pode virar um personagem de cel-shading: a textura viaja com tudo. O
grading não viaja com nada que seja identidade. → `estilos.md`

## Assets possíveis

| Asset | Quando | Gate |
|---|---|---|
| Três referências de identidade | Aparece uma pessoa real | Identidade provada em cinco segundos de movimento |
| Produto multiângulo | Produto reconhecível ou embalagem | Geometria e texto verificados |
| Locação vazia | Geografia ou continuidade relevante | Sem pessoas acidentais |
| Figurino | Peças importantes ou várias gerações | Materiais e cores fechados |
| Storyboard / animática | Blocking, ordem ou câmera complexa | Usa-se como guia, não como imagem visível |
| Movimento de câmera | Órbita, tracking, POV ou transição difícil | Binding só de trajetória |
| Primeiro frame | Cold open crítico | Aprovado no celular e sem preto |
| Último frame | Produto, CTA visual ou extensão | Estado final e movimento residual |
| Voz | Timbre, áudio final ou voz off | Consentimento e função declarada |

Na Agnes, **primeiro e último frame de cada clipe são obrigatórios**, não opcionais: são a unidade
de produção. → `adapters/agnes-keyframes.md`

## Referências de identidade

Se aparece uma pessoa real: **as três referências dela** (close, folha de personagem e rosto +
corpo inteiro) sempre juntas e declaradas como a mesma pessoa. Como se criam, em que ordem e como
entram no prompt → `referencias-de-identidade.md`. Se ela já tem e funcionam, usam-se como estão.

## Produto

Se existe fisicamente, usar imagens reais. Criar vistas limpas:

- frente;
- três quartos;
- lateral;
- costas/base se afeta a geometria;
- macro de material ou etiqueta.

Separar precisão de produto e estética publicitária. Se uma etiqueta tem que ser lida, verificar
letra por letra ou compor o produto real em pós.

## Locação

Gerar ou fotografar vazia. Descrever geometria com medidas aproximadas e âncoras inequívocas. A
imagem apoia o `Scene Lock`; não substitui.

**Gera-se COM o look da peça** (ver a lei, acima): o bloco de textura vai copiado literal, a mesma
frase do prompt do vídeo.

**Um plate por locação, não por plano.** Se a cena passa do corredor pro quarto, são dois. Se são
três ângulos do mesmo quarto, é **um**: o modelo acha os outros ângulos, e dar três plates
levemente diferentes do mesmo lugar é exatamente como se consegue um quarto que muda de forma
entre cortes.

**Enquadramento em três quartos, sobretudo em interiores.** Câmera em ou perto de um canto, olhando
em oblíquo pra que se vejam duas paredes e a profundidade. Um plate frontal e plano se lê como
cenário de fundo, e o modelo de vídeo o trata como tal.

**Vestir o plate como um diretor de arte.** É onde vive a riqueza do mundo, porque o prompt do
vídeo não tem orçamento de caracteres pra isso: desgaste nas superfícies, profundidade em camadas
(algo perto da câmera e algo longe), luzes práticas e objetos que digam quem vive ali. Um cômodo
nu se lê como set. **Pessoas nunca vão no plate.**

Binding:

`Take geometry, surfaces, practical light positions and the lighting mood; ignore framing and any
person.`

## Último frame como ponte entre gerações

Mecanismo titular pra encadear módulos, validado em produção. Em superfícies em que o «extend» da
interface não continua o seu próprio material (algumas oferecem um «remake viral» que clona o
estilo de vídeos alheios), o frame-ponte é a única opção. Onde uma superfície tem extend nativo
real, o extend continua ganhando. Na Agnes, o último frame de um clipe É o primeiro keyframe do
seguinte: a ponte é o próprio modo de trabalho.

1. **O frame se extrai do MP4, nunca com print do player** (compressão, resolução de tela,
   interface): `ffmpeg -sseof -0.05 -i video.mp4 -frames:v 1 -q:v 1 ultimo-frame.jpg`
2. **Frame limpo:** pose clara e estável, sem motion blur de um gesto pela metade. Por isso os
   finais se desenham «vivos mas estáveis».
3. **O frame não substitui os locks:** identidade, scene lock e textura se repetem idênticos.
   Binding: `start exactly from this frame — same subject position, same lighting, same framing`.
   A imagem ancora a composição; os locks ancoram o que fica fora do quadro.
   Variante: se o módulo seguinte NÃO deve arrancar nesse enquadramento, o binding muda pra
   continuidade de mundo, não de composição: `TAKE everything as literal continuity — this film
   continues seconds after this frame · IGNORE only that it is a still: do not freeze on it and do
   not reproduce its exact framing`.
4. **Áudio:** com frame-ponte, voz e ambiente arrancam do zero: a costura soa. Prever crossfade
   curto em pós e o banco de remendos de voz.
5. **O truque da silhueta:** se um figurante cruza a costura entre módulos, o módulo N o deixa
   **de costas ou em silhueta** (não há cara pra casar) e o módulo N+1 **abre revelando a cara dele
   pela primeira vez**. A costura deixa de ser risco de continuidade e vira revelação narrativa.
6. **A ordem de upload das referências É o binding.** Os `@ImageN` apontam por posição: se as
   imagens são subidas na plataforma em outra ordem que a do prompt, todo o binding aponta pra
   referência errada. O dossiê declara sempre a ordem de upload (1ª, 2ª, 3ª…) junto dos prompts.
7. **Reancorar o prompt ao render aprovado:** ao ativar a ponte, as descrições do módulo seguinte
   se reescrevem com o que a plataforma renderizou DE VERDADE (figurino, cenário, sala): a
   descrição genérica original já não é a fonte de verdade, o frame é.

## Se o usuário já tem vídeo real do processo

Diz-se no fechamento, não no arquivo: **o que já está gravado não se gera**. Esse material vai
como está pra montagem (`/anuncio-edita`), ou se usa como referência de movimento de câmera no
plano que precisar. A geração se paga quando faz o impossível.

## Movimento de câmera

Uma referência de vídeo pode fornecer só trajetória, aceleração e estabilidade. Pode ser gravada
com o celular em outra locação; o binding deve excluir sujeito, cenário, figurino, luz, cor e áudio.
