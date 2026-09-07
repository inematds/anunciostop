# Hierarquia de reparação

## 1 · Conservar

Escolher quando não há bloqueantes, o mecanismo se entende e os defeitos cosméticos não mudam
confiança nem compreensão.

## 2 · Editar localmente

Escolher quando uma faixa isolada contém:

- objeto errado;
- figura ou clone de fundo;
- superfície, fumaça ou reflexo incorreto;
- produto ou texto substituível;
- artefato localizado.

Prompt base (em plataformas com edição localizada):

```text
Between [start-end], change only [target] to [desired state]. Preserve the exact identity, facial
performance, body motion, camera trajectory, framing, lighting, shadows, timing, dialogue, lip-sync,
ambient sound and every unaffected region from the source clip.
```

Na Agnes não há edição localizada: o equivalente é **regerar só o clipe afetado** com o mesmo
`seed` e os mesmos keyframes, ajustando uma dimensão do prompt, ou corrigir em pós (corner-pin de
tela, remendo de voz).

## 3 · Estender

Escolher quando:

- o clipe atual funciona como unidade;
- o final não está preto nem congelado;
- existe estado visível de continuidade;
- o que se acrescenta é um segundo movimento, não uma explicação do primeiro.

Repetir locks literais e usar o último frame como estado inicial.

## 4 · Salvar na montagem

Escolher quando há tomadas úteis e:

- o corte não falseia um resultado;
- não destrói continuidade de voz;
- pode eliminar uma cauda vazia;
- pode unir módulos já previstos;
- o produto e o claim continuam autênticos.

Não usar montagem pra fingir que o modelo executou uma demonstração que não executou.

## 5 · Regenerar

Obrigatório quando falha de forma global:

- identidade;
- lip-sync;
- mecanismo;
- cold open;
- continuidade na peça inteira;
- física essencial;
- CTA ou claim;
- produto real;
- consentimento ou disclosure.

Antes de regenerar, mudar só a causa provável. Registrar a hipótese.
