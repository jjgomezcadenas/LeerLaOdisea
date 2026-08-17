# Leer la *Odisea* en tiempos iletrados — guía de capítulos

Libro en construcción. Cada capítulo se publica también como artículo (Jot Down), pero la unidad de referencia es el libro. Ejes que atraviesan todos los capítulos:

- La nueva traducción de la *Odisea* de Juan Manuel Rodríguez Tobal (Hiperión, 2026, edición bilingüe), citada como texto de referencia.
- La *Odisea* de Nolan (2026) como contrapunto: qué capta, qué simplifica, a qué le tiene miedo.
- La memoria personal y familiar del autor como hilo conductor (el padre, el primo Pedro, el hijo Héctor, la hija Irene).
- Tono: erudición filológica + ironía coloquial deliberada (los giros coloquiales son intencionados, no descuidos).

**Estructura de archivos (desde agosto de 2026):** el contenido de cada capítulo vive en `src/odiseaN_tema.tex`, encabezado con `\odiseachapter{N.ª parte}{Tema}`; el artículo JD se compila con el driver de dos líneas `odiseaNd_tema.tex` (que usa `odisea_single_driver.tex` + `odisea_common.tex`); el libro completo se ensambla en `odisea_book.tex` (clase book, `\odiseachapter` → `\chapter`). Los capítulos 1–10 fueron migrados por el autor; del 11 en adelante nacen ya en este formato.

**Propósito central del libro (motor narrativo):** humanizar a Ulises más allá de Homero. El anciano Ulises de *Abandonando Ítaca* deja de creer en los dioses; sin dioses no hay destino, y sin destino no hay coartada: sus crímenes fueron suyos. El Ulises de Homero *atribuye*; el del autor *asume* — y al final se le abre una posible redención. La crítica a Nolan es, en el fondo, una excusa narrativa más, no el asunto del libro.

---

## Capítulo 1 — El cine teme a Homero (`odisea.tex`)

**Estado:** publicado.

**Marco personal:** el padre marino regala al autor, a los 15 años, la *Ilíada* y la *Odisea* en la versión del Círculo de Lectores (1971, trad. en prosa de Segalá, 1910). Veranos de lectura voraz, el primo Pedro, el Mar Menor convertido en geografía homérica (sirenas en la isla del Barón, un cíclope en un yate). Primeras cuentas pendientes con Ulises: la matanza de los pretendientes, las esclavas ahorcadas, el enamoramiento de Circe — germen de *Abandonando Ítaca / Leaving Ithaca* (Eolas, trad. de Jenaro Talens).

**Tesis:** el cine le tiene miedo a Homero. La fidelidad al original vs. la aceptabilidad contemporánea (Escila y Caribdis del traductor).

**Argumentos / ejemplos:**
- La huida de Héctor ante Aquiles, suprimida en la *Troya* de Petersen (2004): el cliché sustituye a la humanidad del héroe.
- Aciertos de Nolan reconocidos: el bardo-rapero (Travis Scott), la elipsis de las sirenas, Lupita Nyong'o como Helena, la supresión inteligente de los dioses (salvo Atenea onírica).
- Miedos de Nolan: la cicatriz de Helena (contradice el texto: en la *Odisea* Helena aparece radiante; Menelao tira la espada al ver su pecho), el «perra de mí» (κυνῶπις) que muestra que Helena se castiga sola; las esclavas ahorcadas por Telémaco (el Telémaco real no es un boy-scout).
- El cíclope: en Nolan, un idiota mudo; en Homero, un anfitrión pérfido casi tan artero como Ulises. El engaño de Οὖτις (Nadie) sustituido por una flecha: la astucia reemplazada por la fuerza.
- La *xenía* como eje temático que la película proclama y desaprovecha (Polifemo anfitrión fallido; feacios y Nausícaa omitidos).

**Cierre:** el riesgo de que Nolan/Petersen se conviertan en el Canon en tiempos iletrados; anuncio de la traducción de Tobal.

**Función en el libro:** capítulo de apertura y pacto de lectura. Fija la voz autobiográfica, la oposición entre reinterpretar y simplificar y los principales asuntos que el libro desarrollará después: Helena, Polifemo, la *xenía*, los dioses y la traducción de Tobal.

---

## Capítulo 2 — Una osada Odisea (`odisea2.tex`)

**Estado:** publicado.

**Marco personal:** compras con el hijo Héctor antes de su interrail; fotos desde Ítaca; el autor repite el gesto de su padre y compra la *Odisea* — la edición bilingüe de Tobal — que acaba quedándose él. Historia lectora intermedia: de Segalá a las reinterpretaciones (Graves *Hija de Homero* / tesis de Butler, Kazantzakis, Zachary Mason), Llach → Kavafis como «Homero particular».

**Tesis:** la traducción de Tobal consigue lo que «no se puede»: hexámetros castellanos con música (no metrónomo), rima, neologismos que reproducen los compuestos homéricos.

**Contenido técnico:**
- Análisis métrico del hexámetro castellano: apoyos/ictus, dáctilos, espondeo final, sinalefas audaces, cesura pentemímeris (con tablas escandiendo «Hija de Zeus…» y el verso inicial «De ese hombre, Musa, háblame milerrante…»).
- Fidelidad al orden de Homero: ἄνδρα primero («De ese hombre, Musa» vs. el «Háblame, Musa» de Segalá).
- πολύτροπος → «milerrante»; catálogo de neologismos con *poly-* (milardido, milmañas, milpalabrero…), con *eu-* (bienclariblanca, bellitrenzadas…), ἐνοσίχθων → territremante/territodatremendo, cabelleantes, miramundo, etc.
- Comparación con Pabón (también hexámetros): impecable pero metrónomo; Tobal pide ser declamado. Pasaje de Calipso comparado verso a verso.
- Notas personales: amistad con Tobal («Juanma»), correos, sonetos-ripios cruzados sobre una coma (en nota al pie), Jenaro Talens y la regla de Wilson (línea a línea) aplicada a *Leaving Ithaca*.
- (Comentado en el .tex: material sobre Emily Wilson, reservado.)

**Cierre:** «te he dejado con la miel en la boca» — promesa de seguir leyendo.

**Función en el libro:** presenta el texto de referencia para los capítulos siguientes y enseña al lector cómo escucharlo. Sirve de puente entre el ensayo autobiográfico y las lecturas detenidas de personajes y episodios homéricos.

---

## Capítulo 3 — Helena (`odisea3.tex`)

**Estado:** terminado; versión .docx preparada.

**Marco personal:** al nacer la hija mayor, dudas entre Irene y Helena; etimologías (Εἰρήνη paz / Helena «Señora de la Luz»); eligieron la paz. La guerra de Troya como la guerra que Helena desató… ¿o no?

**Tesis:** la Helena de Homero es una semidiosa impune, fría, hechicera y narradora no fiable — mucho más inquietante que la «mujer maltratada» con cicatriz de Nolan, que es cliché y falsa lectura.

**Recorrido:**
- ¿Fuga o rapto? ἁρπάζω en *Ilíada* III 443-446 (cita griega + traducción); Afrodita la empuja con amenazas al lecho de Paris.
- Juicio de Paris (mitógrafos posteriores, apenas en Homero): soborno de las olímpicas; la guerra como pelea de familia divina.
- Kavafis, «Deslealtad» (trad. J. M. Álvarez, Hiperión 1976): Apolo profetiza larga vida a Aquiles y luego lo mata — amoralidad divina.
- Crítica a Nolan: Atenea/Zendaya *new age*; sin dioses, la *Odisea* pierde su lectura de fondo (hombre vs. Poseidón; héroes como juguetes de deidades nefastas).
- El εἴδωλον de Estesícoro: la Helena falsa en Troya, la real en Egipto; Epicuro como buena noticia.
- Lectura del canto IV con Tobal (todas las citas de versos son de Tobal, pegadas literalmente):
  - Aparición de Helena «parhermana» de Ártemis (¡la diosa casta!); reina mimada, regalos de Egipto.
  - Reconoce a Telémaco («Odiseo grancorazón», μεγαλήτωρ); «perra de mí» (κυνῶπις) dicho tan campante.
  - Bromance Menelao–Odiseo; los aqueos llorones.
  - El filtro egipcio (nepenthes): Helena hechicera comparable a Circe; «si no ha envenenado a Menelao es porque no le ha dado la real gana».
  - Relato de Helena: Odiseo mendigo infiltrado en Troya (anticipo del mendigo de Ítaca y de «Nadie»); ella lo baña, jura y calla.
  - Réplica de Menelao: el caballo, Helena imitando las voces de las esposas de los aqueos, Odiseo tapándole la boca a Anticlo. Helena narradora no fiable; duelo de astucias Helena–Odiseo, ganado por la campana.
  - Después de que su marido la llame embustera: nada. Telémaco pide un catre; Helena «damisanta» (δῖα γυναικῶν) se acuesta con Menelao tan campante.
  - Proteo anuncia a Menelao el Elíseo «porque tienes a Helena»: la condición de yerno de Zeus le procura una excepción al destino común del Hades.
- **Conclusión:** impunidad escalofriante como núcleo del personaje; contra la moralina de Hollywood; en Homero los buenos perecen y la adúltera vuelve radiante a palacio.

**Función en el libro:** primera demostración extensa del rendimiento interpretativo de la traducción de Tobal. Retoma a Helena, presentada brevemente en el capítulo 1, y profundiza en ella mediante una lectura seguida del canto IV. A la vez abre líneas que el libro desarrollará más tarde: la intervención de los dioses, el Hades y las distintas formas de la astucia de Odiseo.

**Nota para la edición en libro:** la cicatriz de Nolan y *kynôpis* ya aparecen en el capítulo 1. La repetición es necesaria para que el artículo sea autónomo, pero al ensamblar el volumen convendrá convertirla explícitamente en reanudación («como vimos…») o abreviarla, para que se lea como desarrollo y no como nueva exposición.

**Material desplazado / anunciado para otros capítulos:**
- Clitemnestra, Egisto e Ifigenia (con el papel rastrero de Ulises) → capítulo propio.
- El cíclope y la omisión imperdonable de Nolan (Ulises no habla con Polifemo) → su capítulo.
- El Hades («del que hablaremos más adelante»).
- Más sobre la amoralidad de los dioses («ya hablaremos más del tema»).

---

## Capítulo 4 — Calipso (`odisea4_calipso.tex`)

**Estado:** terminado; versión .docx preparada.

**Tesis:** los dioses son un problema, narrativo y moral — y Calipso, paradójicamente, es la inmortal más humana y comprensible: enamorada y sola. De paso, el canto V revela otra cara del miedo de Hollywood a Homero: no atreverse con todas las dimensiones de Ulises, cruel y abnegado a la vez.

**Recorrido:**
- Apertura sobre los dioses como problema (enlaza con el final del cap. 3): el concilio del libro IV de la *Ilíada*, en **traducción propia del autor en endecasílabos** (con nota autoirónica: «para no tener que compararme con Tobal»): Zeus propone la paz; Hera solo se calmaría «devorando» a Príamo; hipocresía y falta de compasión divinas.
- El *deus ex machina* literal: los dioses destrozan cualquier argumento; por eso Baricco (reescritura de la *Ilíada*) y Nolan los suprimen o silencian.
- Canto V con Tobal: nuevo concilio; la hipócrita Atenea (ἐρυσίπτολις, «protectora» de la Troya que arruinó) pide soltar a Odiseo; Zeus dicta a Hermes el plan completo (veinte días, Esqueria, feacios, regalos) — arbitrariedad: los diez años de tumbos eran innecesarios.
- El vuelo de Hermes (imposible de filmar sin que parezca el Flash de DC), la gruta de Calipso como «hotel de cinco estrellas», y Odiseo llorando en el cantil.
- La rabieta de Calipso: doble moral de los olímpicos con las diosas que aman a mortales (Orión/Aurora, Jasión/Deméter); su soledad (que Nolan capta, con Charlize Theron); la ternura de la despedida; el último soborno: la inmortalidad.
- **Injerto de *Abandonando Ítaca*** (secciones I–VI, citadas por extenso): los fantasmas del viejo Ulises — Anticlea, Laertes, Penélope (más ambigua que la de Anne Hathaway), el niño arrojado de los muros, los pretendientes («¿realmente lo pasaste tan mal en casa de Calipso?»). Hollywood teme la crueldad de Odiseo; la *Odisea* muestra todas sus facetas sin reducirlo a monotema (el fallo fatal de Nolan: el arrepentimiento como clave única).
- Cierre: la respuesta caballerosa de Odiseo (rechaza la inmortalidad con diplomacia) y la última noche: «gozan amor y delicias el uno enredado en la otra».

**Función en el libro:** primer capítulo dedicado a los dioses como problema narrativo y primer retrato extenso de una «buena» inmortal. Introduce además la voz poética de *Abandonando Ítaca* dentro del libro: el autor dialoga con su propia reescritura. Anuncia Circe («de la que hablaremos pronto»).

**Notas para la edición en libro:**
- Queda comentado en el .tex el párrafo que enlazaba a Atenea con Helena como «narradoras no fiables» — decidir si se recupera.
- Los tres «sólo» con tilde en los poemas de *Abandonando Ítaca* son (presuntamente) grafía del libro impreso; cotejar.

---

## Capítulo 5 — Nausícaa (`odisea5_nausicaa.tex`)

**Estado:** terminado; .docx preparado.

**Marco personal:** el lector de quince años enamorado de la princesa de su misma edad (hamaca del Mar Menor, celos de los pretendientes, ganas de teletransportarse a Corfú); y el padre actual, con la nostalgia de las carantoñas de Irene antes de pedir «las llaves del coche». Motivo nuevo: los «misterios de la relatividad general» — leer a Tobal medio siglo antes de que la escribiera; Einstein y Homero.

**Recorrido (canto VI con Tobal):** la alcoba «milbienlabrada» (contraste con Segalá); el enredo de Atenea en el sueño; el «papá» (πάππα, único en toda la *Odisea*) — **defensa del «dad» de Nolan** frente a sus críticos; el lavadero y la pelota; el símil de Ártemis; el náufrago desnudo como león (y «casi en cuero picado»); la súplica a distancia del héroe convertido en pordiosero; la hospitalidad y el aplomo de Nausícaa; el cotilleo feacio («y eso que todavía no se habían inventado las redes sociales»); la plegaria final y Atenea que no acude por miedo al tío Poseidón.

**Crítica a Nolan:** suprimir a Nausícaa y los feacios es «pecado capital»: borra el contraejemplo de su propia tesis sobre la *xenía*.

**Injerto de *Abandonando Ítaca*:** tres fragmentos (la princesa desnuda y el mendigo; «¿La amabas?»; «¿convicción o cobardía?»).

**Cierre:** el amor imposible por partida doble (lo pierde el héroe y lo pierde el adolescente lector); el «dulce y lacerante filtro» (eco del nepenthes de Helena); «Todos seguimos amando a Nausícaa».

---

## Capítulo 6 — Esqueria (`odisea6_esqueria.tex`)

**Estado:** terminado; .docx preparado. **Primera pieza con secciones** (`\section*`), para alcanzar el tamaño JD: «El palacio de Alcínoo» (canto VII) y «Bardos» (canto VIII y arranque del IX). En el libro podrían ser capítulos separados.

**El palacio de Alcínoo:** Atenea celestina y la niebla; la ciudad de los navicélebres feacios — Esqueria como **paraíso perdido**; el palacio fabuloso (Ítaca y Esparta, «chozas cabreras»); la súplica a Arete: el saqueador reducido a mendigo «descubre ---¿o finge?--- la humildad» y se vuelve algo más humano; «Y Nolan la elimina de su historia» (párrafo de una línea); Equeneo y el huésped en las cenizas; la justificación formal de la *xenía* (los dioses comen a su mesa); el «impúdico estómago» y el «pobre infeliz»; la agudeza de Arete (las ropas); Alcínoo ofrece a su hija al vuelo; las naves mágicas sin timonel y la profecía de Poseidón (la recompensa por cumplir la *xenía* será el aislamiento eterno); cierre con el eco de Esparta: Alcínoo y Arete se encaman como Helena y Menelao.

**Bardos:** Demódoco (el papel que Travis Scott habría bordado); el canto del caballo; el llanto oculto de Odiseo con el símil de la cautiva (Homero le da al héroe las lágrimas de sus víctimas); el «dime tu nombre» tras un día entero de anonimato; «Soy Odiseo Laertiada». Salto a *Abandonando Ítaca*: la memoria del anciano que falla; el juramento de los pretendientes de Helena (del *Catálogo de las mujeres* atribuido a Hesíodo, s. VI a.C.); la codicia como verdadero motor de la guerra; el diálogo paródico Matt Damon/Penélope («rumbo al sol poniente»); los cícones en Homero (saqueo confesado «como quien dice que fue a buscar tabaco») y en el poema («un matón cruel y astuto que tuvo más suerte que los demás»). **Cierre en verso, deliberado:** «los hombres inventaron a los inmortales / para dar un sentido a sus propios errores» — el ateísmo del anciano le quita la coartada del pasado (núcleo del motor narrativo del libro).

**Función en el libro:** primera pieza plenamente al servicio del motor narrativo (Homero atribuye, el autor asume); deja enhebrados los relatos de los cantos IX–XII (Polifemo, Circe, Hades, sirenas) como «lo que contó a continuación».

---

## Capítulo 7 — Cíclope (`odisea7_ciclope.tex`)

**Estado:** terminado; .docx en el repo.

**Tesis:** el episodio de Polifemo es el laboratorio del narrador no fiable: la más célebre astucia de Odiseo es también su mentira mejor contada, y la fama del héroe se funda en agrandar al monstruo.

**Recorrido:** tregua inicial con Nolan (lo que salva: Esparta, Nyong'o, Bernthal; lo que condena: eliminar el architruco — «séptimo círculo del infierno» con Michael Bay, Emmerich y Santiago Segura). Lotófagos vía poema propio (la belleza como peligro; «Tal vez nunca creíste en dioses» — siembra del ateísmo del anciano). Los cíclopes «altivos sin ley» que viven de los dioses; la isla de las cabras; la avaricia como motivo real del desembarco (el vino de Marón como plan premeditado). Paralelismo Calipso/Polifemo (ambos en cuevas = seres sobrenaturales, no rudos); nota: Homero nunca dice que tenga un solo ojo (eso es Hesíodo, *Teogonía*) — detalle clave para el poema propio (cataratas). La cueva del tesoro y la imprudencia arrogante. La *xenía* invertida: comparación fórmula ritual de Néstor («huéspedes», tras dar de comer) vs. el cíclope («extraños», antes) — Tobal traduciendo ὦ ξεῖνοι de dos maneras. **Tesis anti-Nolan central:** en la *Odisea* la *xenía* se respeta casi siempre (Néstor, Menelao, Calipso, feacios); sus dos violaciones racionales son los pretendientes y Polifemo — justo lo que la película ignora. Duelo de arteros (pregunta por las naves / mentira del naufragio); Οὖτις; la borrachera; la estaca (Flaubert); «Con artería y no a fuerza Ninguno, queridos, me mata»; la bravuconada final que deshace la treta (dos necios). Narrador no fiable: el cíclope demasiado listo y demasiado tonto, demasiado malo (come hombres) y demasiado bueno (mima ovejas). Poema: los nietos pidiendo el cuento, la verdad disuelta «como la sal en el agua», los cíclopes como hijos rechazados del Olimpo, «ese pobre y gentil muchacho algo retrasado», el oro escondido como motivo, «Nadie lo hizo» y los gritos que aún persiguen. Nota al pie: *Abandonando Ítaca* precede en dos años a la película. **Cierre en verso:** el vencedor «debe estar diciendo seguramente la verdad».

---

## Capítulo 8 — Circe (`odisea8_circe.tex`)

**Estado:** terminado; .docx en el repo.

**Tesis:** ¿y si la gran pasión de Odiseo no fue Penélope sino Circe, y el regreso a Ítaca una fuga de una cárcel de amor? Aflora la historia de amor secreta del libro (sembrada desde el cap. 1 y en «Menelaus»).

**Recorrido:** crítica a la Circe plana de Nolan (ingeniería plástica «a mano» en vez de fondo psicológico). Rampa del canto X: Eolia (la bolsa de los vientos como Pandora; la ingratitud de la tripulación; Sísifo; «Por necedad, todo por necedad… la estupidez humana como tema central» — el motor narrativo en aforismo), la expulsión de Eolo, los lestrigones. Eea: filología de δεινή/«fascinadora» y αὐδήεσσα/«vocihumana» (todo el capítulo se construye, como la Circe del autor, a partir de la voz); las fieras mansas; la diosa que canta y teje; **simetría de las tejedoras** Penélope/Circe con dos citas del epílogo de Candelas Gala a *Abandonando Ítaca* (tercera voz del libro); la transformación en cerdos (filtro que hace olvidar ↔ filtro de Helena); Hermes y el antídoto (veneno/antídoto, varita/espada, cama con condiciones); el juramento y el «bienhermosísimo lecho»; el año de juergas; la condición tremenda: el Hades para hablar con Tiresias; instrucciones del rito; muerte absurda de Elpénor; Circe invisible en la despedida. Narrador no fiable: la diosa «demasiado» asustada. Poema: el funeral de Elpénor con Circe cantando (invención cronológicamente impecable — el entierro es del canto XII), «Y sin embargo, él también, una vez, estuvo vivo», la voz como espejo de los crímenes y **la fórmula de la redención**: «monstruo o no, eres solo un hombre, y todos los hombres, / lo merezcan o no, / pueden ser redimidos» — primera formulación explícita de la tesis del libro, en boca de Circe (por eso el viejo la ama: fue la única que vio al monstruo completo y ofreció perdón).

---

## Capítulo 9 — Hades (`odisea9_hades.tex`)

**Estado:** terminado; .docx en el repo.

**Tesis:** el canto XI como prueba definitiva de que, para los griegos, la vida tras la muerte no era vida sino «un horrible existir sin existir» — y de ahí que la muerte pueda ser redención (Demócrito, Epicuro). El capítulo más oscuro del libro.

**Recorrido:** elogio a Nolan (la excursión al Hades, junto con las sirenas, está «a la altura de la historia que cuenta»). Especulación propia: Cimeria como ¿noche polar? El umbral del Hades (sin Estigia ni Caronte: nadie ha muerto aún); el rito de la sangre y «la horrible democracia de la muerte» (ninguna película de zombis lo supera); Elpénor primero — la primera compasión genuina del héroe, que nos reconcilia con él; Anticlea y el triple abrazo imposible («el canto más triste… hasta que Primo Levi escribiera *Si esto es un hombre*»); Tiresias: la profecía, y las vacas de Helios como **el examen que a priori puede aprobarse pero siempre se suspende** (Orfeo, la bolsa de los vientos, Perséfone y la granada, Ícaro — el libre albedrío solo en teoría; la lectura condenatoria de Nolan «no es descabellada»); el último viaje del remo y el aviento (nota: la *Telegonía* de Eugamón — Tesprotia, Calídice, Polipetes, y Telégono matando a su padre con el aguijón de raya). Adelanto del desfile heroico: Aquiles («Preferiría doblarme en la tierra para otro y ser siervo… a ser el rey entre toda esta plebe acabada de muertos»), Neoptólemo, Áyax rencoroso hasta en la muerte (nota: el juicio de las armas, ὅπλων κρίσις), Sísifo (eco del cap. 8), y el εἴδωλον de Heracles — **conectado explícitamente con el de Helena** (los dioses fabrican dobles para el trabajo sucio). **Agamenón queda anunciado para el próximo capítulo** (→ Ifigenia/Clitemnestra).

**Poema:** la duda del anciano — ¿fue real el Hades o «una pesadilla invocada por los filtros de Circe»?; «morir y no ser, disolverse en la nada»; el primer beso entre naranjos, las muchachas desnudas en la playa (Nausícaa), los ojos del hijo — «la última redención».

**Cierre en prosa** (el primero desde Nausícaa): la meditación epicúrea — contra nuestra obsesión moderna con la vida eterna, la muerte como liberación definitiva del Hades.

---

## Capítulo 10 — Agamenón y Clitemnestra (`odisea10_agamenon.tex`)

**Estado:** terminado; .docx en el repo. Pieza de cámara (~2.200 palabras): extensión deliberadamente contenida.

**Tesis:** el matrimonio fallido por excelencia, y el sacrificio de Ifigenia como el crimen que no admite justificación alguna — con Odiseo «casi tan culpable como Agamenón»: la boda-trampa con Aquiles fue invención suya. El capítulo donde el motor narrativo toca su punto más criminal.

**Recorrido:** elogio matizado a Nolan (el atuendo Darth Vader, la Clitemnestra vengadora — que es Esquilo/Eurípides, no Homero, como ya anotaba la nota del cap. 3). En la *Odisea* es **Egisto** quien mata, en emboscada, «tal buey que uno mata en el arrendadero»; la matanza del banquete como boda roja *avant la lettre* (guiño a *Juego de tronos*). Casandra degollada por Clitemnestra sobre el cuerpo del rey. **κυνῶπις otra vez** (eco de Helena, cap. 3): a Agamenón le molesta más la desvergüenza de la asesina que el propio crimen. La misoginia póstuma del Atrida («secreto, siempre secreto… yo ya en mujeres no creo») desmontada con su propio historial: Criseida, la comparación pública con Clitemnestra, Briseida, Casandra — «Menuda familia». El elogio de Penélope en boca del fantasma. Lupita Nyong'o doblando Helena/Clitemnestra (medio hermanas). Poema de *Abandonando Ítaca*: la conspiración de Calchas (¿dioses, cuentas pendientes o dinero? — «los dioses solo existen en la imaginación de los hombres»), Odiseo el más insistente, y **las tres caras de Ifigenia** (la que irrumpe radiante, la que pregunta por qué, la muerta que sigue preguntando). Cierre en prosa: «el sacrificio de un inocente no admite justificación alguna… basta seguir las noticias durante cinco minutos».

**Nota:** la grafía «Calchas» (y «bueys», «aun obrando una recto» en Tobal) es deliberada/verbatim.

---

## Capítulo 11 — Sirenas (`src/odisea11_sirenas.tex`)

**Estado:** terminado; .docx en el repo. Primera pieza nacida en la estructura nueva (driver `odisea11d_sirenas.tex`; incluida en `odisea_book.tex`).

**Tesis:** el juicio a Nolan — y su absolución. La escena de las sirenas como el momento en que «el cine es capaz de superar la palabra escrita»; y el canto de las sirenas como **lo sagrado que no necesita dioses** — la cara luminosa del motor narrativo.

**Recorrido:** marco cómico: concilio olímpico juzgando a Nolan (Atenea la psiquiatra *new age*, Apolo, Circe, Calipso ofreciéndose a quedárselo, Zeus consultando a Ulises — que está en el Olimpo, con «el último modelo de εἴδωλον, animado por IA» ocupando su plaza en el Hades: triple eco de la casa). Pastiche en verso de las ofensas (Matt elprota, Penélope-Julieta, el pretendiente-vampiro, los feacios eliminados). Veredicto: el Elíseo, por las sirenas. Canto XII con Tobal: regreso a Eea y **entierro de Elpénor** (promesa del cap. 9 cumplida); instrucciones de Circe (cera, mástil, «lazada y nueva lazada»); la despedida sospechosa («¿dejaste ir, sin más, a Odiseo? ¿O el mientisagaz nos está ocultando algo?» — semilla explícita: «Ya veremos más adelante»); el canto de las Sirenas (el cebo es el *conocimiento*: «todo sabemos las dos…») y el silencio de Homero sobre lo que sintió el héroe — la cuenta pendiente que salda el poema propio. Poema de *Abandonando Ítaca*: el sentido de lo sagrado (los hombres cantando de noche «sobre lo que han perdido»), las sirenas como «canciones de los hombres con acordes más puros», y el catálogo de las cosas sencillas — la risa de Penélope, el bebé dormido, las aceitunas, pan y vino — «todas vacías de dioses, pero llenas de gracia». **Cierre en verso:** «tiempo, tiempo que fluye, / huyendo».

---

## Capítulo 12 — La matanza de los pretendientes (`src/odisea12_pretendientes.tex`)

**Estado:** terminado; .docx en el repo; incluido en el libro.

**Tesis:** la μνηστηροφονία revela al Odiseo que Nolan no se atreve a mostrar: no un héroe arrepentido que concede clemencia, sino un vengador implacable que ha decidido exterminar a los ciento ocho pretendientes. La domesticación cinematográfica convierte al tigre de Bengala en gato de angora y reduce también a Telémaco, guerrero y cómplice de su padre, a muchacho torpe y pasivo.

**Recorrido:** la palabra griega que contiene por sí sola «la matanza de los pretendientes»; crítica de la batalla de Nolan y de su Telémaco. Canto XXI: Penélope propone la prueba; Telémaco está a punto de tensar el arco al cuarto intento; Leodes, el único galán contrario a los excesos, fracasa y profetiza el desastre; Eurímaco teme la deshonra; Antínoo aplaza su intento; Penélope defiende al mendigo sin haber reconocido a su marido y conserva así su agencia; Telémaco aparta a su madre y entrega el arco. El arco canta «como voz de vencejo». Canto XXII: Antínoo muere mientras bebe; Eurímaco ofrece reparación y Odiseo rechaza cualquier perdón; los pretendientes, armados, se defienden; Telémaco mata a Anfínomo y combate junto a su padre, Eumeo y Filetio; Melantio abastece de armas a los galanes; Atenea interviene primero como Méntor y después desvía las lanzas. Dos lecturas de la victoria: intervención divina o fortuna del héroe. Poema de *Abandonando Ítaca*: el anciano se reconoce como «un matón cruel y astuto / que tuvo más suerte que los demás». Odiseo degüella al inocente Leodes y revisa la sala para que nadie escape. Euriclea encuentra al bebé que amamantó convertido en un león cubierto de sangre.

**Cierre:** «Parece que la masacre ha terminado, ¿no?». El capítulo se detiene justo antes del episodio más infame y entrega el relato directamente al siguiente.

---

## Capítulo 13 — El asesinato de las niñas (`src/odisea13_ninas.tex`)

**Estado:** terminado; .docx en el repo; incluido en el libro. «Niñas» es una elección literaria deliberada, no una afirmación filológica sobre la edad que les atribuye Homero.

**Tesis:** el asesinato de las doce esclavas es el episodio que vuelve imperdonable a Odiseo y explica de verdad por qué el cine teme a Homero. El contraste con Aquiles demuestra que la brutalidad del héroe antiguo todavía puede humanizarse mediante la compasión; Odiseo y Telémaco, en cambio, niegan esa compasión a las muchachas.

**Recorrido:** memoria personal de la lectura a los quince años y del asco que aplazó durante meses el reencuentro con Penélope; Euriclea señala a doce esclavas; Odiseo las obliga a retirar los cadáveres y limpiar la sangre antes de ordenar que las maten; Telémaco rechaza la espada como muerte demasiado limpia y las ahorca; Melantio es mutilado; las esclavas fieles abrazan después al vencedor. El golpe se compara con el final de la *Ilíada*. Injerto amplio de *Abandonando Ítaca*: Patroclo, Pentesilea y Héctor; la interpretación del amor fatal entre héroes; Aquiles arrastra el cadáver de Héctor para ocultar su corazón roto y termina llorando con Príamo antes de devolverle el cuerpo de su hijo.

**Cierre:** Aquiles puede entrar en el cine porque su compasión final lo vuelve humano. La iniquidad de Odiseo resulta, por el contrario, demasiado moderna: campos de concentración, purgas, Gran Salto Adelante y mujeres ahorcadas por los ayatolás. Repetición circular y sentenciosa: «No es de extrañar que el cine tema a Homero».

---

## Capítulo 14 — Penélope (`src/odisea14_penelope.tex`)

**Estado:** terminado; .docx en el repo; incluido en el libro.

**Tesis:** el reencuentro de Penélope y Odiseo no es la reconciliación sentimental que ofrece Nolan, sino el encuentro cauteloso de dos extraños después de veinte años. Penélope conserva voz, voluntad y astucia propias: la prueba del arco fue otra treta para no casarse y ni la cicatriz basta para vencer su desconfianza; solo la seña íntima del lecho de olivo permite el reconocimiento.

**Recorrido:** Euriclea despierta a Penélope y le anuncia el regreso; la reina atribuye la matanza a un dios antes que exponerse de nuevo a la esperanza; la cicatriz la ablanda, pero no la convence; descenso a la sala y silencio entre los esposos; impaciencia de Telémaco y defensa de las señas privadas. Reflexión sobre la muchacha que apenas convivió con Odiseo antes de pasar dos décadas sola y casi cuatro años resistiendo a los pretendientes: quizás lo que deseaba era que la dejaran en paz. Odiseo, más preocupado por la reacción del pueblo, organiza una boda falsa para ocultar la matanza; las comadres y los compadres condenan inmediatamente a Penélope. Atenea remocea al héroe; Penélope ordena sacar el lecho y provoca la indignada descripción del olivo vivo convertido en pie de cama. En su rendición rompe además una lanza por Helena, empujada al «malhacer deshonesto» por un dios. Odiseo revela el viaje del remo que aún le debe a Tiresias y, después del lecho, le contará también a su esposa todo cuanto vivió con Circe y Calipso.

**Cierre:** final feliz deliberadamente falso: a Penélope no solo le toca escuchar las aventuras y las infidelidades de su marido, sino aprender a convivir con un extraño.

---

## Hilos pendientes del libro

1. El final del canto XII: Escila y Caribdis en detalle, las vacas de Helios y el naufragio — y la vuelta del relato a la corte de Alcinoo. Semilla sembrada en el cap. 11: qué oculta la despedida de Circe («Ya veremos más adelante»).
2. El borrador `ifigenia.tex`: comprobar si queda superado por el cap. 10 (Agamenón y Clitemnestra) o guarda material aprovechable (Orestes, la *Orestíada*).
3. Vetas apuntadas y no cobradas (para capítulos futuros): el *nostos* de Agamenón como espejo oscuro del de Ulises (su «secreto, siempre secreto» dicta el disfraz de mendigo en Ítaca); Penélope como contrafigura de Clitemnestra.
4. El destino de los feacios (la profecía de Poseidón citada en el cap. 6 se cumple en el canto XIII).
5. Posible capítulo final: el material personal de Kavafis/Llach, Blanes, Quelo y la Siseta, retirado del cap. 8 y guardado en `itaca_blanes.tex`.
6. Poema «Menelaus» (`menelao.tex` / `menelao_es.tex`): ubicación pendiente (¿capítulo de la vejez de los héroes?).
4. Posible recuperación del material de Emily Wilson (comentado en `odisea2.tex`).
5. Decisiones de libro: numeración/títulos de capítulos, unificar las referencias cruzadas («como vimos en…») cuando se ensamble el volumen.
