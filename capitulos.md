# Leer la *Odisea* en tiempos iletrados — guía de capítulos

Libro terminado en estructura y contenido: **24 capítulos que espejan los 24 cantos** de la *Odisea*. Pasada «revision-final» (branch homónima) completada para los 24 capítulos (agosto 2026). Ejes que atraviesan todo el libro:

- La traducción de la *Odisea* de Juan Manuel Rodríguez Tobal (Hiperión, 2026, edición bilingüe), citada como texto de referencia. Citas de Tobal **verbatim** (bueys, almodóvar, «obrando una recto»…): solo se arregla marcado LaTeX, nunca el texto.
- La *Nodisea* de Nolan (2026) como contrapunto: qué capta, qué simplifica, a qué le tiene miedo. Nolan es, en el fondo, excusa narrativa.
- La memoria personal y familiar del autor como hilo conductor (el padre, el primo Pedro, Quelo, Juan Carlos, Toni, el hijo Héctor, la hija Irene).
- Tono: erudición filológica + ironía coloquial deliberada (los coloquialismos son intencionados, no descuidos).

**Propósito central (motor narrativo):** humanizar a Ulises más allá de Homero. El anciano Ulises de *Abandonando Ítaca* deja de creer en los dioses; sin dioses no hay destino, y sin destino no hay coartada: sus crímenes fueron suyos. El Ulises de Homero *atribuye*; el del autor *asume* — y al final se le abre una posible redención. Hilo secundario que atraviesa el libro: **la voz de Circe** (XIII–XIV, sirenas en XVII, regreso final en XXIV).

**Estructura de archivos:** cada capítulo vive en `src/odiseaN_slug.tex` (N=1..20 más cuatro ficheros `_prime_` de particiones tardías), con cabecera `\odiseachapter{slug}{Título}\label{cap:slug}`. **Los labels no se cambian nunca** (las particiones los conservan); referencias cruzadas con `capítulo~\ref{cap:slug}`. Libro: `odisea_book.tex`, compilar **solo con lualatex** (`latexmk -lualatex`), ~172 páginas. `jdown/` = versiones JD congeladas con compilador propio (`compile_jd.py`); `edicion/` = documentos editoriales (informe de lectura, contraportada, portadillas, informe de referencias a Nolan); `capitulos.tex` = resumen de capítulos en limpio (PDF para la editorial).

---

## Los 24 capítulos

| # | Título | Archivo (label) |
|---|--------|-----------------|
| I | De libros y películas | `odisea1_intro.tex` |
| II | El cine teme a Homero | `odisea2_nolan.tex` |
| III | Una osada Odisea | `odisea3_tobal.tex` (cap:osada) |
| IV | Helena | `odisea4_helena.tex` (cap:helena) |
| V | Menelao | `odisea5_menelao.tex` |
| VI | Calipso | `odisea6_calipso.tex` |
| VII | Nausícaa | `odisea7_nausicaa.tex` |
| VIII | Esqueria | `odisea8_esqueria.tex` |
| IX | Bardos | `odisea8_prime_bardos.tex` |
| X | La Gran Guerra | `odisea9_guerra.tex` |
| XI | Cíclope | `odisea10_ciclope.tex` |
| XII | La bolsa de los vientos | `odisea11_eolo.tex` |
| XIII | La isla de la hechicera | `odisea12_circe.tex` (cap:circe) |
| XIV | La voz de Circe | `odisea12_prime_voz.tex` (cap:voz) |
| XV | Hades | `odisea13_hades.tex` (cap:hades) |
| XVI | Agamenón y Clitemnestra | `odisea14_agamenon.tex` (cap:agamenon) |
| XVII | Sirenas | `odisea15_sirenas.tex` |
| XVIII | El arco funesto | `odisea16_pretendientes.tex` (cap:pretendientes) |
| XIX | La matanza de los pretendientes | `odisea16_prime_matanza.tex` |
| XX | El asesinato de las niñas | `odisea17_ninas.tex` (cap:ninas) |
| XXI | Penélope | `odisea18_penelope.tex` |
| XXII | Laertes | `odisea19_laertes.tex` |
| XXIII | Homero | `odisea19_prime_homero.tex` |
| XXIV | Marcharse de Ítaca | `odisea20_marcharse.tex` |

**I — De libros y películas.** Pacto de lectura: en tiempos iletrados, el cine es para muchos el único acceso a los clásicos. La coincidencia Nolan/Tobal como origen del libro. Adrián (nombre también falso, como Alba) y el bullying escolar. Plan de lectura anunciado: Tobal + tres versiones modernas + Graves «en el penúltimo capítulo». Única URL del libro (Eolas) en nota, fundida con la precedencia de *Abandonando Ítaca* (escrito 2020–2023, publicado 2025, un año antes del estreno).

**II — El cine teme a Homero.** El cine de masas sustituye la ambigüedad de los héroes por clichés morales (Héctor en *Troya*). Balance de la *Nodisea*; la tesis de la *xenía* «se sostiene a duras penas» — el desmontaje se difiere («Como veremos») a Esqueria. Cierre del gato por liebre con referencias a Helena, Circe y Telémaco.

**III — Una osada Odisea.** La traducción de Tobal: hexámetro castellano con música, análisis métrico, acusativo de πολύτροπος, catálogo de compuestos en *poly-*, duelo con Pabón. «Me siento poeta y niño de nuevo». (Los sonetillos de Quique Ruiz salieron del libro → artículo JD en `jdown/odisea25_sonetillos.tex`.)

**IV — Helena.** La semidiosa impune, hechicera y narradora no fiable, más inquietante que la «mujer maltratada» de Nolan. Lectura del canto IV con Tobal; duelo de astucias Helena–Menelao–Odiseo; Anticlo. (El Kavafis de «Deslealtad» se cortó en la pasada final: Kavafis debuta ahora en XXIV con el *Viatge a Ítaca*.)

**V — Menelao.** El poema «Menelaus» de *Abandonando Ítaca*: otra versión del matrimonio. Reinterpretar no equivale a simplificar. Primera definición de *nóstos*.

**VI — Calipso.** Los dioses como problema narrativo y moral; el concilio del libro IV de la *Ilíada* en traducción propia. Calipso, la inmortal más humana: enamorada y sola.

**VII — Nausícaa.** El amor imposible por partida doble; defensa del «dad»/πάππα; primera aparición del Mar Menor. «Todos seguimos amando a Nausícaa».

**VIII — Esqueria.** Los feacios como cumplimiento supremo de la *xenía*; su supresión desmonta la tesis de la película («viola las leyes olímpicas que dictaminan cómo debe reinventarse un clásico»). Aquí vive —y solo aquí— el argumento de los troyanos violando la *xenía* al abusar de la hospitalidad de Menelao (crédito a Juanma Tobal).

**IX — Bardos.** Demódoco y su primer canto; el llanto de Odiseo con el símil de la cautiva; la confianza del Poeta en la inteligencia de su público.

**X — La Gran Guerra.** El anciano de *Abandonando Ítaca* recuerda causas, duración y coste de la guerra; la codicia como motor real.

**XI — Cíclope.** Abre con Οὖτις: «Ese Nadie que se lee también como "Todos" o "Cualquiera"». No se puede eliminar a Nadie sin arruinar al personaje. Polifemo (Πολύφημος, *Polýphēmos*, «milpalabrero» en Tobal) como anfitrión pérfido; el narrador no fiable. (La antigua apertura del «séptimo círculo» fue sustituida por la de Nadie en la pasada final.)

**XII — La bolsa de los vientos.** La necedad humana como tema: el odre abierto a la vista de Ítaca, los lestrigones. Resuena con la apertura de XI: «resignarse a ser solo otro hombre, Οὖτις, Nadie».

**XIII — La isla de la hechicera.** ¿Y si la gran pasión de Odiseo fue Circe? La Circe plana de Nolan contra la δεινή/«fascinadora» de Homero; las tejedoras (Candelas Gala); Hermes bajo forma humana y el abanico de lecturas de los dioses (¿narrador fiable?, ¿fábula?, ¿intuición atribuida?) — motor narrativo explícito.

**XIV — La voz de Circe.** El año en Eea; la condición del Hades; la muerte absurda de Elpénor; la partida con Circe invisible. Los poemas: Circe cantando en el entierro de Elpénor, la voz como espejo de los crímenes y la fórmula de la redención («todos los hombres, lo merezcan o no, pueden ser redimidos»). Las instrucciones rituales del viaje se movieron a XV en la pasada final.

**XV — Hades.** El canto XI: la vida tras la muerte como «horrible existir sin existir»; el examen que siempre se suspende (las vacas de Helios); Demócrito y Epicuro. Abre con las instrucciones de Circe (movidas desde XIV).

**XVI — Agamenón y Clitemnestra.** Egisto mata en Homero; Clitemnestra venga a Ifigenia en Esquilo/Eurípides/Nolan. Las tres caras de Ifigenia; «el sacrificio de un inocente no admite justificación alguna».

**XVII — Sirenas.** El juicio olímpico a Nolan y su absolución: la escena en que el cine supera a la palabra. Las sirenas «sabían cantar las canciones de los hombres / con la voz de Circe» — anudado a XIV. Entierro de Elpénor (canto XII).

**XVIII — El arco funesto.** Telémaco casi tensa el arco (casi tan fuerte y astuto como su padre); Penélope defiende al mendigo sin reconocerlo. Convertir al tigre de Bengala en gato de Angora «no es reinterpretarlo, sino empobrecerlo».

**XIX — La matanza de los pretendientes.** La μνηστηροφονία; Leodes degollado; el elogio de Tobal («zarpirrecorvos y piquirretuertos» contra los vocablos de WhatsApp); el lobo con piel de oveja y el riesgo de la caricatura.

**XX — El asesinato de las niñas.** El episodio que vuelve imperdonable a Odiseo. Aquiles/Héctor/Pentesilea y el amor fatal entre héroes; «Permíteme que insista»: en la versión del autor no cambian los hechos sino la motivación. «No es de extrañar que el cine tema a Homero».

**XXI — Penélope.** Dos extraños tras veinte años; la prueba del lecho de olivo; el final feliz deliberadamente falso. El poema del fantasma que vuelve «sin falta / a seguir tejiendo y destejiendo su sudario».

**XXII — Laertes.** El padre en la finca; las astucias innecesarias del hijo («¡Déjate de cuentos y abrázale!»); «Lecciones de conducir». Las protagonistas de la *Odisea* son mujeres; las esclavas no cuentan porque son esclavas. La enmienda del autor al canto XXIV empieza a gestarse.

**XXIII — Homero.** La cuestión homérica: Parry, bertsolaris, jazz. Butler y la muchacha de Trápani; **Graves ampliado en la pasada final**: la trama de *La hija de Homero* (Alfides, Laodamante, el golpe de Estado), el *nóstos* blasfemo de Demódoco (Penélope y los cincuenta pretendientes, el cinturón de Afrodita) y la crueldad conservada de la matanza. «El clásico existe para que las generaciones posteriores lo reescriban, lo reimaginen, lo reinterpreten, pero nunca para que lo adulteren».

**XXIV — Marcharse de Ítaca.** La enmienda del autor al canto XXIV. Las Ítacas del autor (Blanes y las golondrinas, Alba, el Mar Menor, la Ítaca industrial de los feacios); Kavafis/Llach; Quelo, Juan Carlos, Toni. El viejo Odiseo no acepta otra expiación: vuelve al mar a buscar a Circe. «Abandonar lo que más se ama, para poder seguir amando».

---

## Decisiones cerradas

- **24 = 24:** un capítulo por canto; las particiones (`_prime_`) conservaron los labels antiguos — ninguna `\ref` se rompió.
- ***Nodisea* / *Nodiseo*** siempre en cursiva (`\emph{}`).
- **Sistema de versos** (`odisea_common.tex`): `versocita` (cuerpo menor + sangría) para Tobal y todo poeta/traductor citado, **incluidas las traducciones propias del autor** («la traducción es mía» = cita); `versopropio` (cursiva, cuerpo normal) para los poemas del autor. `quote`/`quotation` en cuerpo menor.
- **Comillas:** parlamentos completos con «»; fragmentos partidos por prosa, sin comillas. Verso citado en prosa: «… / …».
- **Ortografía de 1910** en las citas de Segalá («vió», «á la patria»): se conserva.
- **«a. C.»** con espacio (forma RAE) en todo el libro.
- **Una sola URL** en todo el libro (Eolas, nota del cap. I).
- **«Calchas»**, «bueys», «obrando una recto», etc.: verbatim deliberado.
- **«El asesinato de las niñas»:** «niñas» es elección literaria, no afirmación filológica.
- Los **sonetillos de Quique Ruiz** están fuera del libro (artículo JD propio).

## Pendientes

- Merge de `revision-final` → `final` → `main` cuando el autor lo decida.
- Versión Word / entrega editorial de la edición final.
- `capitulos.tex` (resumen para la editorial) debe mantenerse sincronizado con esta guía.
