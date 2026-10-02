# Absalon sitt Bergen

GPS-vandring for skuleklassar gjennom Bergen med dagboka til Absalon Pederssøn Beyer (1552–1572). Elevane går mellom postane. Når dei kjem innanfor 50 m, viser sida originaltekst, moderne nynorsk, ordliste og ei oppgåve.

- **Live:** https://absalon.sneaas.no. **Denne mappa ER produksjon.** nginx serverer ho direkte, så alt du lagrar i `index.html`, er straks ute hos brukarane.
- **Repo:** https://github.com/as-troska/absalon (offentleg). Greina heiter `main`. Commit-meldingane er på nynorsk (`feat:`, `docs:`, `chore:`). Git-identiteten er sett lokalt.
- **Språk:** Snakk nynorsk med brukaren. All tekst i appen er nynorsk.

## Filer

- `index.html`: heile appen (HTML, CSS og JS i éi fil, ingen byggjesteg). Leaflet 1.9.4 frå cdnjs, OSM-fliser og Google Fonts (Barlow, Barlow Semi Condensed, EB Garamond).
- `bilete/`: utsnitt av Scholeus-prospektet (kring 1580) frå Wikimedia Commons. Dei blir henta med `hent-bilete.sh`.
- `sjekk.py`: **køyr etter kvar endring av postane.** Han sjekkar JS-syntaks, obligatoriske felt, at bileta finst, at sitata står ordrett i dagboka, og at ingen postar ligg nærare enn 100 m.
- `kjelder/` (i .gitignore): `dagbok.txt` er heile dagboka som rein tekst og kan søkjast i. `NSL_Beyer_Dagbok_tekst.html` er originalfila frå Bokselskap (Ragnvald Iversen si utgåve, 1963). Lisensen er uavklart, så ho skal **ikkje** i git.

## Format for postane

`const POSTS = [...]` i `index.html`. Rekkjefølgja i lista er rekkjefølgja i oversikta.

```js
{
  id:"kors",                       // kort og unik, blir lagra i localStorage ("absalon-visited")
  task:{kind:"Bilete"|"Video", text:"...", read:"..."},  // read = originaltekst elevane les høgt (berre Video)
  img:["Commons-filnamn.jpg","lokalt.jpg","Biletekst."],  // valfritt
  links:[["Tittel","https://www.bergenbyarkiv.no/bergenbyleksikon/arkiv/<id>"]],  // valfritt
  name:"Korskyrkja", lat:60.394888, lon:5.327780,
  title:"Bråk i prestegarden",
  intro:"Bakgrunn som elevane treng.",
  orig:"Ordrett frå dagboka. Utelatne bitar skal merkjast med (…).",
  modern:"Omsetjing til moderne nynorsk, same struktur og (…) som orig.",
  date:"17. april 1563",
  gloss:[["gammalt ord","forklaring"], ...]   // 5–6 ord
},
```

## Slik lagar du ein ny post

1. Søk i `kjelder/dagbok.txt` etter stader som finst i dag. Skriv ut år og dato saman med treffa, for datoane står på eigne linjer (`[1563]`, `APRILIS 1563.`, `17. Slo …`).
2. Vel ein kort og levande episode som passar for elevar. Han skal knytast til ein stad dei kan stå på.
3. Byleksikon-lenkjer finn du med `curl -sL "https://www.bergenbyarkiv.no/bergenbyleksikon/?s=<søkjeord>"` og grep etter `bergenbyleksikon/arkiv/[0-9]+`.
4. Koordinatar hentar du frå Nominatim: `https://nominatim.openstreetmap.org/search?q=<stad>,Bergen&format=json`.
5. Bilete-oppgåver kan samanlikne med Scholeus-stikket. Bokstavane på stikket: A slottet, C Mariakyrkja, G Martinskyrkja, I Korskyrkja (to spisse tårn, brann 1582), K Domkyrkja og skulen, M Spitalen.
6. Oppdater talet på postar i `<meta name="description">`, `og:description` og README.md (tabellen og «… postar»).
7. Køyr `python3 sjekk.py`.

## Tekstane

Intro, omsetjingar, ordlister og oppgåver er **skrivne av Claude, ikkje av brukaren**. Dei er CC0, og README seier det. Ikkje tilskriv brukaren desse tekstane. Koden er MIT.

## Postane så langt

lepra (Lepramuseet), dom (Domkyrkja), kors (Korskyrkja, testpost lagd 2026-10-02), torget, brann (Strandkaien), nykirken, bryggen, bergenhus.

## Kjende opne saker

- nginx serverer `.git/` offentleg (`/.git/config` gjev 200). Brukaren må leggje til `location ~ /\.(?!well-known) { deny all; }` i `/etc/nginx/sites-available/absalon.sneaas.no`. Claude har ikkje sudo.
