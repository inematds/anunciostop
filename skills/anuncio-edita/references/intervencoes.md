# Menu de intervenções opcionais · critério de editor

> A regra mãe: **cada extra se PROPÕE com motivo e espera OK.** Se não há motivo que caiba numa
> frase («aqui X venderia Y»), não há extra. Um anúncio gerado aguenta MENOS camadas que um reel
> gravado: cada acréscimo artificial é mais uma pista de que é IA.

## Quase sempre SIM (propor por padrão)

| Intervenção | Quando | Como |
|---|---|---|
| **Trim de caudas** | A plataforma devolve segundos a mais (pede 28, dá 30) | Cortar contra o áudio, ~0,15 s de ar depois da última palavra |
| **Crossfade de ambiente nas costuras** | Sempre que se montam módulos | 0,15-0,25 s só na camada de ambiente; a voz nunca se cruza |
| **SRT sidecar** | Sempre que vai pra Meta | Além das queimadas: a Meta indexa as legendas nativas |

## Às vezes SIM (propor só se o material pede)

| Intervenção | Quando SIM | Quando NÃO |
|---|---|---|
| **SFX diegético pontual** | Uma ação visível ficou muda na geração (um golpe de carimbo, uma xícara pousando) e o silêncio se nota. Baixar via inemavox/dlp | Nunca whoosh, riser nem golpe de biblioteca «de anúncio». Se o ambiente já cobre, fora |
| **Realce do plano-assinatura** | O momento chave passa despercebido (ex.: a tela de agentes mal se lê por um instante) | Se o plano já funciona. O realce é sustentar o plano 0,3-0,5 s a mais (slow-hold leve), NÃO um zoom artificial |
| **Ênfase de texto grande** | UMA frase do anúncio inteiro merece letreiro grande (o dado que dói) | Mais de 1-2 momentos = reel carregado. Com legendas já há texto na tela |
| **Música** | O brief pedia e a geração não trouxe. Baixar via inemavox/dlp | O registro documental/UGC da casa costuma ir SEM música. Não acrescentar «porque fica pro» |
| **Correção de cor entre módulos** | Um módulo saiu visivelmente mais frio/escuro e a costura canta | Se tem que corrigir muito, o módulo está mal gerado: isso é regenerar, não colorir |
| **Time-stretch de uma frase** | Lip-sync derivado >2-3 frames em UM trecho a câmera | Jamais na pista inteira; `atempo` 0,97-1,03 no máximo |

## Quase sempre NÃO

- **Zooms/punch-ins artificiais** sobre vídeo gerado: o material já traz push-ins dirigidos do
  prompt; acrescentar zoom digital em cima duplica o gesto e amolece a imagem.
- **Transições** (varreduras, glitch, flash branco): o corte seco em silêncio é a casa.
- **Emojis, stickers, setas**: registro UGC-documental, não YouTube 2019.
- **Filtros de look** («cinematic teal&orange»): matam o realismo de celular que o prompt construiu.
- **Velocidade variável / speed ramps**: delatam edição sobre material que finge ser um plano real.

## O teste final do editor

Antes de entregar, três perguntas:

1. **A edição se nota?** Se um trecho chama atenção pra montagem, sobra algo.
2. **Cada acréscimo tem um porquê que cabe numa frase?** O que não tem, fora.
3. **Isso passaria por um vídeo gravado com celular por alguém de bom olho?** Essa é a régua: não
   «que bonito ficou», mas «não parece editado».
