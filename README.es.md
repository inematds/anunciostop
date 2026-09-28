# Anuncios Top con IA

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

Sistema de cuatro decisiones para transformar una idea en un anuncio en video generado con IA, listo
para Meta, sin gastar créditos a ciegas. Cuatro skills para Claude Code, en portugués, encadenadas:
cada una hace **una** cosa y deja un documento escrito para la siguiente.

```
/espiona-ads        →  qué está funcionando allá afuera y por qué
/video-ia           →  de tu idea a 10 guiones; del elegido a la ficha del personaje, el modelo y los prompts
/auditor-video-ia   →  ¿esto se conserva, se salva en el montaje o se regenera?
/anuncio-edita      →  la pieza final montada y masterizada para Meta
```

**La tesis:** el prompt no es el trabajo. El trabajo es decidir el ángulo, fijar la identidad,
dirigir el plano y auditar antes de publicar. Por eso el sistema sigue siendo útil cuando cambie
el modelo de moda.

- Guía de uso: `guia/index.html` (publicada en `https://inematds.github.io/anunciostop/guia/es/`)
- Descarga de las skills: [`anuncios-top-skills.zip`](anuncios-top-skills.zip)
- Plan del curso: [`PLANO-CURSO.md`](PLANO-CURSO.md)

---

## Índice

1. [Instalación](#1-instalación)
2. [Qué más necesitas](#2-qué-más-necesitas)
3. [Lo primero que debes hacer: la ficha de marca](#3-lo-primero-que-debes-hacer-la-ficha-de-marca)
4. [La cadena de cuatro decisiones](#4-la-cadena-de-cuatro-decisiones)
5. [Las skills, una por una](#5-las-skills-una-por-una)
6. [Proveedores y adaptadores](#6-proveedores-y-adaptadores)
7. [Dónde escriben las skills](#7-dónde-escriben-las-skills)
8. [Estructura del repositorio](#8-estructura-del-repositorio)
9. [El curso](#9-el-curso)
10. [Avisos honestos](#10-avisos-honestos)
11. [Origen y adaptación](#11-origen-y-adaptación)

---

## 1. Instalación

Dos minutos, sin programar.

1. Descarga y descomprime [`anuncios-top-skills.zip`](anuncios-top-skills.zip) (o clona este repo).
2. Copia las cuatro carpetas a tu carpeta de skills de Claude Code:

```bash
cp -R skills/* ~/.claude/skills/
```

3. Abre Claude Code y escribe `/video-ia`. Si hace cinco preguntas, está instalado.

> **Windows / otra ruta:** la carpeta es la que tu instalación de Claude Code usa para las skills de
> usuario. Si ya tienes otras skills, es la misma carpeta donde están.

## 2. Qué más necesitas

| Para qué | Qué necesitas | Obligatorio |
|---|---|---|
| Todo | Claude Code | Sí |
| `/espiona-ads` y `/anuncio-edita` | `ffmpeg` y `ffprobe` | Sí para estas dos |
| `/espiona-ads` (transcripción) | Clave de Groq en `GROQ_API_KEY` | Sí para esta |
| Generar imágenes y videos sin costo | Clave de Agnes en `AGNES_API_KEY` | Sí, si usas el proveedor predeterminado |
| Subtítulos incrustados | Python con Pillow, solo si tu ffmpeg no tiene `libass` | Solo en ese caso |
| Generar en Seedance, Dreamina o similar | Cuenta en la plataforma; se usa a través de la web | No; se paga por separado |

Las claves se configuran mediante una variable de entorno o en un `.env` en la raíz de tu proyecto:

```bash
export GROQ_API_KEY="sua-chave"
export AGNES_API_KEY="sua-chave"
```

Los scripts leen las claves en runtime y nunca las imprimen ni las copian a otro lugar.

## 3. Lo primero que debes hacer: la ficha de marca

Las skills trabajan con **tu** marca y vienen con la ficha en blanco a propósito.

Copia `skills/video-ia/marcas/_modelo.md` a `anuncios/marcas/<sua-marca>.md` y completa:

- qué se vende y qué se pide al final del video;
- para quién, descrito como una persona y no como un segmento;
- la oferta con la redacción exacta;
- la prueba que se puede mostrar, con su fuente;
- el tono, con una frase real de la marca;
- las prohibiciones;
- identidad visual (el color de acento se convierte en el color de la palabra clave en los subtítulos);
- caras y voces disponibles;
- plataforma de generación predeterminada.

Hay un ejemplo completado en `_exemplo-oficina-do-bairro.md` (marca inventada). Quince minutos,
una sola vez. Sin la ficha, las skills funcionan, pero hacen más preguntas y los guiones suenan genéricos.

## 4. La cadena de cuatro decisiones

| # | Decisión | Skill | Qué entra | Qué sale (documento para la siguiente) |
|---|---|---|---|---|
| 1 | De dónde viene la idea | `/espiona-ads` | una cuenta que ya anuncia | playbook: hooks literales, ritmo medido, estructura persuasiva |
| 2 | Dirigir, no pedir | `/video-ia` | una idea (o el playbook) + una foto | 10 guiones; por cada uno elegido, un dossier con imágenes por crear, orden de carga y prompts listos |
| 3 | Qué se conserva y qué se rehace | `/auditor-video-ia` | el MP4 generado | una decisión: conservar, editar localmente, extender, salvar en el montaje o regenerar |
| 4 | Dejarlo listo | `/anuncio-edita` | los módulos aprobados | master 1080×1920 + SRT |

Dos se usan siempre: la que busca la idea y la que produce. Las otras dos son opcionales y existen
para ahorrar dinero cuando ya estás generando.

**Regla que atraviesa todo:** el documento es la memoria. Cada skill escribe un markdown y lo actualiza
en el mismo lugar, nunca lo duplica. Renombrarlo o crear una "v2" rompe la cadena.

**Nada se genera sin ti.** Ninguna de las cuatro gasta un centavo por su cuenta: `/video-ia` deja
los prompts y tú eres quien pulsa el botón.

## 5. Las skills, una por una

### `/espiona-ads`: espiar a quienes ya están pagando

Das una URL de la Biblioteca de Anuncios de Meta (o el nombre de una marca) y obtienes la fórmula
desglosada: hooks literales, ritmo de cortes medido, palabras por minuto, estructura persuasiva
cronometrada y un veredicto con evidencia sobre si están usando IA.

Seis fases: extracción en el navegador (Meta bloquea `curl`), clasificación por días en circulación y
variantes activas (la Biblioteca no publica gasto ni CTR), procesamiento mecánico con ffmpeg y
Whisper, análisis de frames con subagentes, contexto del embudo (la landing), síntesis.

El informe termina con un bloque obligatorio: qué se puede adaptar, qué requiere cuidado y qué
NO se copia. Se copia la estructura, nunca la mentira.

Archivos: `skills/espiona-ads/SKILL.md`, `references/prompt-subagente.md`, `scripts/extrai.js`,
`scripts/processa.sh`.

### `/video-ia`: dirigir el video, no pedirlo

El corazón del sistema. Cinco pasos, sin saltarse ninguno:

1. **Escucha la idea.** Una frase vaga, un playbook o un guion cerrado.
2. **Cinco preguntas sobre el mensaje, todas de una vez.** Qué se vende, para quién, qué debe
   pensar la persona al terminar, qué pruebas existen, qué no se puede decir. Nada técnico todavía.
3. **El menú de diez.** Diez conceptos con diez mecanismos diferentes, cada uno con la escena en prosa,
   cold open, miniguion con frases literales y tiempos, dónde va la oferta, ritmo y riesgo. Predeterminado:
   3 UGC, 3 minificción, 2 demostración, 2 cine. Después del menú, SE DETIENE y pregunta cuáles desarrollar.
4. **Lo técnico, solo de los elegidos.** Duración, quién aparece (cinco vías de identidad), ritmo
   propuesto, plataforma, idioma y qué material ya existe.
5. **Un Markdown por video**, con cuatro bloques fijos: imágenes que se deben crear antes, guion para leer
   en voz alta, qué subir y en qué orden, prompts para copiar y pegar.

Lo que sabe la skill está en las referencias:

| Referencia | Qué cubre |
|---|---|
| `entrevista.md` | Los dos bloques de preguntas y por qué no se mezclan |
| `menu.md` | Cómo se construye el menú de diez y las siete reglas |
| `modos.md` | Catálogo de 21 modos (UGC, testimonio, demostración, entrevista callejera, objeto que habla, mascota, escala imposible, POV, absurdo, cine puro, letrero en escena…) y qué vigilar en cada uno |
| `cold-open.md` | Los primeros tres segundos: doctrina, seis mecanismos, prueba de siete preguntas, antipatrones |
| `ritmo.md` | Niveles de ritmo, presupuesto de palabras por pista, límite de la interfaz, forma del ritmo, arquitecturas |
| `estilos.md` | Cuatro bloques de textura (UGC de celular, minificción, cine, estilizado); elige uno y pégalo completo |
| `identidade-e-voz.md` | Las cinco vías: personaje inventado, persona real con referencias, foto + audio, voz en off, grabar y transformar |
| `apresentador.md` | Ficha de presentador en siete dimensiones: la misma cara en todos los anuncios |
| `referencias-de-identidade.md` | Las tres imágenes de referencia de una persona real y los prompts para generarlas |
| `gravar-e-transformar.md` | Quince segundos de celular se convierten en otra escena manteniendo la cara, los gestos y la cámara |
| `direcao-de-plano.md` | Cómo se dirige un plano: geografía, actuación observable, cámara con propósito, escala como lock |
| `imagens.md` | Qué se prepara como imagen antes del video: texto, logos, props, interfaces en HTML |
| `assets.md` | Biblia visual: assets neutros, locación con look, último frame como puente |
| `saida.md` | El formato exacto del dossier de salida |
| `adapters/` | Cómo se compila el prompt para cada plataforma (ver sección 6) |

### `/auditor-video-ia`: auditar antes de volver a gastar

Recibe el prompt (preflight) o el MP4 generado (postflight) y devuelve una sola decisión con motivo y
rango de tiempo exacto:

```
DECISIÓN: EDITAR LOCALMENTE
Porque: la identidad, el guion y el ritmo funcionan; solo falla el producto entre 00:11–00:13.
Acción: reemplazar el producto en ese rango y conservar la cámara, la actuación, la luz y el audio.
No tocar: hook, cara, timing, voz y CTA.
```

Jerarquía de reparación: conservar → editar localmente → extender → salvar en el montaje →
regenerar. Un objeto local no justifica regenerarlo todo. Un bloqueo (claim sin evidencia, cara sin
consentimiento, producto diferente del real, CTA ausente) impide publicar aunque el resto tenga una nota alta.

Incluye un verificador mecánico de prompts:

```bash
python3 ~/.claude/skills/auditor-video-ia/scripts/checa-prompt.py prompt.txt --interface seedance25 --duracao 30
```

Detecta corchetes sin completar, prompts más largos que el campo, marcas de tiempo con huecos, planos sin
diálogo, acento incorrecto y palabras de grading que devuelven blanco y negro.

Archivos: `references/preflight.md`, `postflight.md` (con tabla síntoma → causa → solución),
`hierarquia-de-reparacao.md`, `publicacao-e-transparencia.md`, `assets/modelo-auditoria-video-ia.md`,
`assets/registro-experimentos.csv`.

### `/anuncio-edita`: montar la pieza final

La doctrina: la mejor edición es la que no se nota. El material ya viene dirigido; aquí se monta,
se limpia y se entrega. Siempre: montar módulos, pista de voz, subtítulos sobrios, letrero de cierre,
master a 1080×1920 con loudness de plataforma. Todo lo demás es opcional y se propone antes de hacerlo.

Subtítulos: pastilla oscura, 2 a 4 palabras por página, palabra clave en el color de la marca, a la
altura del pecho, sin tapar ninguna cara. Dos maneras de incrustarlos: `ass=` directamente cuando
ffmpeg tiene libass, o superposición por PNG (Pillow) como alternativa.

Scripts: `captions.py`, `jargon-fix.py`, `export-srt.py`, `master-audio.py`, `overlay-fallback/`.
Configuración de la superposición mediante variables: `CAPTION_FONT` (fuente) y `KEYWORD_COLOR` (color de acento).

Si el material sin editar fue **grabado con cámara** en vez de generado, el montaje es otra skill
(`reel-edita-inema`), no esta.

## 6. Proveedores y adaptadores

El método es neutral; el prompt final cambia según dónde lo pegues. Tres adaptadores en
`skills/video-ia/references/adapters/`:

| Adaptador | Costo | Cómo se usa | Qué hace |
|---|---|---|---|
| **Agnes por keyframes** (predeterminado) | cero | `AGNES_API_KEY` | Imagen (text2img e img2img) y video por par de keyframes A→B, hasta 20 s por clip en 720p. Solo vía D (voz en off): la voz viene de inemavox o se graba y se monta después |
| **Seedance 2.5 multishot** | pago | por la web del proveedor (TopView, Higgsfield, Magnific…) | Hasta 30 s con cortes dentro del prompt, referencias de imagen, video y audio, diálogo con lip-sync |
| **Dreamina one-take / Seedance 2.0 modular** | pago | por la web | Una toma continua de 30 s o módulos de 15 s para montar |

Solo Agnes necesita configuración. Los demás funcionan pegando el prompt en su interfaz.

Los límites de cada modelo vencen rápido. Los adaptadores tienen fecha; cuando un número no coincida
con lo que ves en pantalla, corrige el adaptador y sigue.

## 7. Dónde escriben las skills

De forma predeterminada, en una carpeta `anuncios/` dentro de tu proyecto. No necesitas crearla:
se crea sola.

```
anuncios/
├── marcas/                  tu ficha de marca
├── roteiros/                los dossiers de cada pieza (un markdown por video)
├── criativos/               una carpeta por pieza: módulos, master, SRT
├── _apresentadores/         fichas de continuidad y las tres referencias de identidad
└── referencias-criativas/   los informes de /espiona-ads
```

## 8. Estructura del repositorio

```
anunciostop/
├── README.md                    esta documentación
├── PLANO-CURSO.md               plan completo del curso (7 módulos, proyecto-hilo, adaptaciones)
├── anuncios-top-skills.zip      las 4 skills listas para descargar
├── skills/                      las 4 skills, fuente
│   ├── README.md                instalación resumida (va en la raíz del zip)
│   ├── espiona-ads/
│   ├── video-ia/
│   ├── auditor-video-ia/
│   └── anuncio-edita/
├── guia/                        landing + guía de uso (GitHub Pages)
├── fonte/                       material de origen y mapa módulo → archivo (uso interno)
└── FALHAS.md                    registro de fallas (una línea por falla)
```

## 9. El curso

El plan completo está en [`PLANO-CURSO.md`](PLANO-CURSO.md). Resumen:

| Módulo | Tema | Entregable |
|---|---|---|
| 0 | Preparación: instalar las skills y completar la ficha de marca | `anuncios/marcas/<marca>.md` |
| 1 | Espiar a quienes ya están pagando | informe de espionaje con banco de hooks |
| 2 | Dirigir, parte 1: de la idea al menú de diez | menú con 2-3 conceptos elegidos |
| 3 | Dirigir, parte 2: del concepto al prompt | dossier completo + tres referencias de identidad |
| 4 | Generar y auditar antes de volver a gastar | auditoría completada + primera fila del registro |
| 5 | Montar la pieza final | master 1080×1920 + SRT |
| 6 | Publicar con criterio y aprender con el cuarto anuncio | registro con la siguiente hipótesis |

Un solo anuncio atraviesa los módulos 1 a 6 (el proyecto-hilo). Al final, la carpeta `anuncios/` del alumno
es el portafolio del curso. Formato: INEMA `/formato-curso-v2`. Proveedor de las demostraciones: Agnes.

## 10. Avisos honestos

- **Generar video cuesta dinero** fuera de Agnes, y se paga por segundo. `/auditor-video-ia` existe
  precisamente para que no regeneres cinco veces lo que se resuelve en el montaje.
- **El video con IA no siempre gana.** En venta directa en frío, una grabación con cámara puede convertir
  mejor que un avatar. Donde la IA gana por mucho es en lo que no se puede filmar: escenarios imposibles,
  sátira, metáfora física, volumen. Si alguien dice que un avatar vende por sí solo, pídele el número.
- **La cara o la voz de una persona real requieren su permiso.** Nunca uses las de un tercero. Es el único límite
  de las skills que no admite excepciones.
- **No inventes pruebas.** Ni testimonios, ni resultados ni números. Sin pruebas, haz una demostración con lo
  que existe.

## 11. Origen y adaptación

El método viene de un minicurso en español sobre anuncios con video IA. Esta versión fue traducida
y adaptada al ecosistema INEMA:

- portugués de Brasil en los textos y los prompts (con una instrucción negativa contra la deriva de acento);
- Biblioteca de Anuncios con BR como país predeterminado;
- adaptador Agnes (costo cero) como proveedor predeterminado, escrito a partir de mediciones reales de la API;
- claves cargadas en runtime, nunca copiadas;
- el montaje de material sin editar grabado apunta a `reel-edita-inema`;
- rutas y fuentes neutrales (Linux, Mac, Windows);
- script escrito para verificar prompts (el original mencionaba uno que no venía incluido en el paquete);
- se eliminaron las referencias a la fuente, las anécdotas con fecha y los números de cuentas ajenas; los valores que
  quedan son de referencia y deben validarse con datos propios.

Proyecto de investigación y educación de INEMA.
