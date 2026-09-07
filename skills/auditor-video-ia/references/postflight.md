# Postflight técnico e comercial

## Metadados

Usar `ffprobe` quando há arquivo local:

```bash
ffprobe -v error -show_entries format=duration,bit_rate -show_entries \
stream=index,codec_type,codec_name,width,height,r_frame_rate -of json VIDEO.mp4
```

Registrar o resultado real, não a promessa comercial da plataforma.

## Amostragem visual

Revisar no mínimo:

- primeiro frame;
- fim do cold open;
- começo e fim de cada unidade/corte;
- frame do meio de movimentos complexos;
- último frame;
- qualquer faixa que o usuário marcar.

Pra continuidade, alinhar primeiros frames de clipes ou planos. A deriva se detecta melhor
comparando do que olhando cada clipe separado.

## Gate visual

| Área | Falha se |
|---|---|
| Identidade | Mudam estrutura facial, idade, cabelo, marcas ou proporções |
| Figurino | Mudam peça, material, cor ou acessório sem motivo |
| Mãos | Dedos, pegada ou contato são impossíveis |
| Boca | Lip-sync globalmente quebrado, dentes mutam ou perfil esconde a voz |
| Produto | Geometria, etiqueta, cor ou escala não batem |
| Texto | Há uma letra, número ou palavra incorreta |
| Continuidade | Posição, objeto, luz ou estado se reiniciam |
| Física | Peso, contato, sombra ou trajetória não respondem à ação |
| Câmera | Para, muda de eixo ou executa outro movimento sem motivo |
| Fundo | Aparecem clones, figuras, objetos ou arquitetura mutante |

## Gate de áudio

- A voz começa quando foi prometido.
- O CTA está completo.
- O sotaque é o combinado.
- Nomes, números e marcas se pronunciam bem.
- Não há silêncios centrais sem função.
- A cauda pode ser cortada sem perder o fechamento.
- Ambiente, efeitos e música não competem com a voz.
- Não soa conteúdo de uma referência usada só como timbre.

## Gate comercial

- O cold open para por uma ação, objeto, contraste ou promessa concreta.
- O público reconhece a situação dele.
- O mecanismo se entende sem ler o brief.
- A prova aparece e se compreende.
- A marca não poderia ser trocada por qualquer outra.
- O CTA se ouve, se vê ou se infere corretamente.
- Ver sem som conserva a ideia com legendas ou imagem.
- Ver no celular mantém legibilidade e foco.

## Severidade

- **Bloqueante:** legal, claim, consentimento, identidade global, produto falso, CTA ausente.
- **Maior:** mecanismo confuso, lip-sync global, continuidade quebrada, cold open inerte.
- **Local:** objeto, frame, fundo ou texto reparável numa faixa.
- **Cosmético:** textura ou detalhe que não altera identidade, compreensão nem confiança.

Um bloqueante impede publicar mesmo que a peça tenha boa pontuação nos outros itens.

## Diagnóstico · sintoma → causa → conserto

O gate diz se algo falha; esta tabela diz **por quê** e o que se mexe. Ir ao sintoma antes de
regenerar: metade das falhas é uma linha que falta, não um prompt ruim.

| Sintoma | Causa provável | Conserto |
|---|---|---|
| O cinza de estúdio vaza pro plano | A linha do asset não leva exclusão | Acrescentar «não usar o fundo nem a luz plana da folha» a **cada** linha de identidade → `assets.md` |
| Tudo parece o projeto anterior | Look herdado, não derivado do assunto | Reescrever o bloco de textura a partir desta peça. O tungstênio âmbar com sombras profundas é a armadilha padrão |
| Volta em preto e branco | Vazaram palavras de grading | Nunca «dessaturado», «monocromático», «claro-escuro», «crushed blacks» a seco. **Cores em positivo:** «âmbar quente e marrom profundo» |
| A cara deriva a partir do plano 5 | Duas caras legíveis na mesma referência | Uma só cara legível por folha. No corpo inteiro, cabeça cortada → `referencias-de-identidade.md` |
| Falta um painel na folha | Não se declarou a contagem | Abrir com «esta imagem contém N vistas no total, todas devem estar». **Reforçar essa frase, nunca reestruturar o formato**: reestruturar perde o painel que você tinha |
| O cômodo muda de forma entre cortes | Vários plates do mesmo espaço | Um plate por locação, não por plano |
| Os objetos se teletransportam entre cortes | Sem estado final por trecho | Declarar o que é visivelmente verdade ao terminar cada trecho → `direcao-de-plano.md` |
| Os contraplanos trocam de lado | Sem âncora de geografia | Fixar uma vez: «ele à esquerda do quadro, ela à direita» |
| Uma criatura ou veículo enorme no plano geral e montável no seguinte | Sem âncora de escala | Declarar a escala uma vez em termos humanos e **escrita como a interação** |
| Corte com glitch | O plano seguinte abre no mesmo eixo | Abrir com ≥30° de mudança, outra classe de tamanho, ou um match on action |
| Luz morta e plana | O tremular não foi escrito | «Luz prática baixa que tremula de leve e nunca fica parada» |
| Movimento aleatório e espasmódico | Coreografia sem sequenciar | Numerar os movimentos um a um |
| Aparece algo que nunca chegou | Sem entrada na tela | Nada aparece do nada: se entra um objeto, vê-se entrar |
| O mundo se vê vazio e plano | Plate nu e encenação num só plano | Vestir o plate e escalonar em profundidade: primeiro plano, meio e fundo |
| A câmera lenta não renderiza | Pediu-se por jargão técnico (obturação lenta, step printing, fps baixos) | Não funcionam. Descrever **o resultado visível** |
| Surgem detalhes inventados numa superfície | A face oculta de um objeto não foi descrita | Qualquer vista que mostre uma superfície que a referência esconde precisa da própria descrição completa |
| Na Agnes: cabeça ou cauda dupla | Pose frontal simétrica | Perfil ou três-quartos; `exactly one head` em positivo |
| Na Agnes: personagem mudou entre clipes | Keyframe B gerado do zero, não de A | B por img2img com A como referência; mudar uma dimensão só |
| Na Agnes: morphing no meio do clipe | A e B diferentes demais, ou duas ações no prompt | Aproximar A e B; uma ação por clipe |

⚠️ **E a regra que economiza renders:** numa prova em baixa resolução **não se julga realismo nem
fidelidade de texto.** Isso são artefatos de resolução, não problemas de prompt, e persegui-los
ali queima gerações. Em 480p julga-se movimento, continuidade e lógica; nada mais.
