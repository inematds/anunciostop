# Preflight

## Gate comum

- [ ] Tese e público definidos.
- [ ] Roteiro e CTA aprovados.
- [ ] Claims com fonte ou marcador pendente.
- [ ] Consentimento de cara e voz.
- [ ] Modelo, provedor e interface declarados.
- [ ] Duração e formato compatíveis.
- [ ] Referências com `take/ignore`.
- [ ] Identidade, produto e cena travados.
- [ ] **Geografia declarada uma vez** (quem de que lado); se não, os contraplanos trocam de lado.
- [ ] **Escala ancorada em termos humanos e escrita como a interação**, se há algo que não mede
      como uma pessoa (criatura, veículo, várias cópias do mesmo ator).
- [ ] **Cores do look em positivo**, nunca «dessaturado» nem «monocromático».
- [ ] **Nenhum asset de identidade leva grading**, e a locação sim leva o look com o bloco de
      textura copiado literal.
- [ ] Uma ação principal por plano/fase.
- [ ] Diálogo e sotaque em formato correto (português do Brasil declarado, negativo contra deriva).
- [ ] **Trilho declarado e orçamento de palavras dentro da faixa** (cinema 126-160 ppm ·
      mini-ficção 150-190 · UGC/talking-head 200-240; pra 30 s: 63-80 / 75-95 / 100-120).
- [ ] **Teto de fala da interface conferido.** Se o trilho pede mais do que a superfície diz,
      resolvido subindo duração ou partindo em módulos, **não cortando roteiro**.
- [ ] Texto crítico decidido, e se há palavras que se renderizam, **ortografia verificada no
      storyboard ou na imagem assada**, não deixada pro render.
- [ ] Se há storyboard: gerado com a folha de personagem engatada, escala conferida painel a
      painel, e grade/rótulos excluídos nos negativos.
- [ ] Custo e tentativas calculados.
- [ ] Uma variável por teste.
- [ ] Disclosure previsto.
- [ ] **Zero colchetes sem preencher no prompt**: o gerador os renderiza literalmente.
- [ ] Declarado em duas linhas o que se decidiu pelo usuário e o que se inventou por falta de referência.
- [ ] Nenhum asset que já funcionava foi regenerado pra encaixar num modelo.

## Agnes por keyframes

- Via D declarada; nenhum plano pede boca falando; `no lip movement` nos negativos.
- Um par de keyframes (A e B) por clipe, ambos aprovados antes do vídeo.
- Prompts de imagem em inglês, ≤ 2 referências, sem pose frontal simétrica.
- `num_frames` = 8n+1 e dentro do teto do tier (481 em 720p = 20 s a 24 fps; 241 em 1080p).
- Fila de vídeo ≤ 5 req/min; retry nos 503.
- Voz (inemavox ou gravada) com roteiro no orçamento de voz off de cinema.
- Último frame do clipe anterior extraído do MP4 como A do seguinte.

## Seedance 2.5 multishot

- Duração ≤ 30 s por geração.
- Timestamps contíguos.
- Referências dentro dos limites expostos pela interface.
- Storyboard declarado como guia, não como asset visível.
- Final vivo se haverá extensão.
- Estilo derivado do brief, não prefixo fixo.
- Edição localizada separada de geração.
- Nenhum plano sem `Dialogue` escrito, salvo mudo por desenho.

## Dreamina one-take

- Prompt ≤ 3.990 bytes como margem na superfície medida.
- Primeiro trecho ≤ 2 s.
- Um único `P1:` quando há diálogo.
- Boca visível e voz desde o frame zero.
- Uma direção de câmera repetida por trecho.
- Sujeito com movimento motivado.
- Até quatro ações diferenciadas.
- Figurino peça por peça.
- Sotaque brasileiro declarado e números por extenso.

## Seedance 2.0 modular

- 15 s como capacidade base oficial.
- Locks literais repetidos entre módulos.
- Estados de entrada e saída compatíveis.
- Cada módulo acrescenta algo e não repete preenchimento.

## Bloqueantes de preflight

- claim crítico sem verificar;
- permissão ausente;
- prompt truncado;
- colchete de modelo sem preencher;
- CTA fora da duração;
- roteiro abaixo do orçamento do trilho sem justificativa: o vídeo vai sair com tempo morto e vai
  ter que ser cortado na montagem;
- produto não verificável;
- capacidade não disponível na interface;
- duas ou mais variáveis mudadas sem reconhecer.
