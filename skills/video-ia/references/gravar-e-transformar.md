# Gravar e transformar · a via que resolve «não aparece ninguém da casa»

**Você grava dez ou quinze segundos com o celular, e um modelo com edição de vídeo (Seedance 2.5 e
similares) converte em outra cena mantendo sua cara, seus gestos e seu movimento de câmera.** Um
só prompt.

É uma via de identidade, não um truque de edição. E resolve o problema clássico dos lotes de
avatar: **a produção era boa e não aparecia ninguém conhecido.** Se o que vende o negócio é que
ensina uma pessoa concreta, o anúncio não pode ser contado por um ator de banco.

| | |
|---|---|
| **O que ganha** | É você de verdade: sua cara, seus gestos, seu jeito de se mover. E **desaparece o lip-sync gerado**, que é a falha nº 1: a boca é a sua, gravada |
| **O que custa** | Quinze segundos do seu tempo e um celular |
| **O que não pode** | Te mudar de lugar dentro do plano, nem te dar gestos que não fez, nem alongar o clipe. A coreografia é a que você gravou |

⚠️ **Isso NÃO é `reel-edita-inema`.** Lá se pega um bruto e se **monta** num reel. Aqui se pega um
bruto e se **converte numa cena que não existe**. Se o trabalho é cortar, legendar e pôr B-roll, é
a outra skill.

⚠️ **A Agnes não tem esta via.** Ela gera por keyframes, não edita vídeo. Esta via exige uma
plataforma com `edit video`.

---

## O que você grava · as cinco regras do bruto

O bruto não é o vídeo: é o **esqueleto de movimento** sobre o qual a cena se constrói. Grava-se
pensando no que vai sobreviver à transformação (cara, gestos, câmera) e no que vai ser jogado fora
(fundo, objetos, luz).

1. **O gesto tem que ser legível e sustentado.** O que se conserva é o movimento: se você fica
   parado falando, a transformação não tem no que se agarrar. Um gesto claro por trecho: apontar,
   virar, pegar algo, levantar.
2. **Grave com o movimento de câmera que quer no resultado.** Se quer que a câmera orbite, orbite
   você com o celular. A trajetória se conserva. É isso que a torna potente e o que quase ninguém
   aproveita.
3. **Fundo trocável e vazio.** Uma parede lisa, um corredor, um cômodo sem coisas. Quanto menos
   houver pra substituir, mais limpo sai. Um fundo com muitos objetos deixa fantasmas.
4. **Objetos: um, e com a forma do que vai ser.** Se na cena final você tem que segurar uma
   lanterna, um controle remoto serve. Se é um caderno, algo do tamanho de um caderno. **A forma
   manda; o objeto real, não.**
5. **Luz plana e sem drama.** A luz do resultado quem põe é a cena nova. Uma luz muito marcada no
   bruto briga com a que se pede.

**E o que se grava de áudio: nada que importe.** O diálogo pode se conservar ou substituir, mas o
ambiente do bruto vai fora. Grave em silêncio se puder.

---

## A forma do prompt de transformação

**A primeira linha não é uma cena: é uma instrução.** É o que distingue este prompt de todos os
outros da skill.

```
Transform the uploaded footage into <a cena nova> while keeping the camera movement, the framing
and the performer's face, gestures and timing EXACTLY as filmed. The performance is not to be
re-animated: it is the footage.

[Replace the environment]
The <o que há> becomes <o que tem que haver>. <geometria, superfícies, luzes práticas visíveis>.
Everything that was <material velho> is now <material novo>.

[Replace the objects]
The <objeto que você segura> in his right hand becomes <objeto novo>, same size, same grip, same
position in frame. <detalhe concreto: um led verde, uma etiqueta, um desgaste>. When he <o que você
fez com o objeto>, <o que o objeto novo faz>.

[Keep untouched]
The performer's face, hair, skin texture and asymmetries are unchanged. His wardrobe is unchanged. The
camera path, its speed and every wobble are unchanged. His gestures, his head turns and the timing of
everything he does are unchanged.

[Add]
<figuras, elementos ou fenômenos que não estavam no bruto>

[Audio]  → ver ritmo.md: ambiente · hierarquia dinâmica · golpes de evento
[Dialogue Block — all lines in spoken order]  → ver adapters/seedance-25-multishot.md
[Negative Constraints]  → base + os do conceito
```

### Os quatro blocos que decidem o resultado

| Bloco | A regra |
|---|---|
| **A instrução de abertura** | Sem ela o modelo re-anima o personagem em vez de conservá-lo, e perde-se a única coisa que dava valor à via |
| **Replace the objects** | 🔴 **É onde tem que ser obsessivamente específico.** O detalhe pequeno é o que torna crível o objeto novo: não «uma lanterna», mas «uma lanterna com um led verde pequeno que segue aceso» |
| **Keep untouched** | Escreve-se **explícito**, não se dá por suposto. Cara, pele, assimetrias, figurino, trajetória de câmera, gestos e *timing*. Os seis |
| **Add** | O que não estava. É o mais barato de pedir e o que mais muda a cena |

---

## Quando esta via é a boa, e quando não

| Conceito | Via |
|---|---|
| O apresentador dizendo algo a câmera num lugar impossível | 🟢 **Gravar e transformar.** Sua cara, sua voz, sua boca |
| Um plano que precisa de oito cópias dele, ou escala impossível | Cara real com as três referências (via B). Aqui o bruto não pode te dar oito corpos |
| Cinema sem ninguém no quadro, com narração | Voz off. → `identidade-e-voz.md` |
| Um gesto ou coreografia que ele não vai gravar | Personagem inventado |
| Talking-head puro, sem cena que valha a pena mudar | **Nenhuma: que ele grave e publique.** Transformar um talking-head em outro talking-head é gastar uma geração à toa |

🔴 **A última linha é regra, não comentário.** Se dá pra gravar e publicar como está, grava-se e
publica-se. A geração se paga quando faz o impossível.

---

## Os riscos próprios desta via

- **Fantasmas do fundo velho.** Se o bruto tinha muitos objetos, ficam restos. Resolve gravando
  mais limpo, não com mais prompt.
- **O objeto substituído «flutua».** Quase sempre faltou descrever a pegada e a sombra de contato:
  que dedos seguram e onde apoia.
- **Os filtros de conteúdo.** Prompts de edição disparam com facilidade: caras tapadas, armas,
  menores no quadro. Se disparar, reescreve-se o prompt sem esse elemento, não se insiste.
- **Conserva-se o bom e o ruim.** Se no bruto você olhou pro celular ou travou, continua ali. O
  bruto se revisa antes de subir.

## Permissão

A cara de uma pessoa da equipe se usa **só se essa pessoa autorizou**. Caras de terceiros, nunca.
Não é formalidade: é o único limite desta skill que não admite exceção.
