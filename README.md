# Absalon sitt Bergen

Ei GPS-vandring gjennom Bergen med dagboka til Absalon Pederssøn Beyer (1528–1575), laga for skuleklassar.

**Live:** <https://absalon.sneaas.no>

Elevane går mellom sju postar i sentrum. Når dei er framme, dukkar ein tekst frå dagboka opp, med originalteksten frå 1500-talet, ei omsetjing til moderne nynorsk, ei ordliste og ei oppgåve (film eller bilete) som skal løysast på staden.

| Post | Tema |
|---|---|
| Lepramuseet | St. Jørgens hospital og «Spitalen» |
| Domkyrkja | Domkyrkja og Latinskolen |
| Torget | Hamn og handel, Martinskyrkja |
| Strandkaien | Bybrannen i 1561 |
| Nykirken | Erkebispegarden og lagtinget |
| Bryggen | Gardane og smauga |
| Bergenhus | Håkonshallen og Rosenkrantztårnet |

## Teknisk

Alt ligg i éi fil, `index.html`, utan byggjesteg og avhengnader å installere.

- Kart: [Leaflet](https://leafletjs.com/) 1.9.4 frå cdnjs, med kartfliser frå OpenStreetMap
- Skrifter: Barlow, Barlow Semi Condensed og EB Garamond frå Google Fonts
- Posisjon: Geolocation-API-et i nettlesaren. Posisjonen blir verande på telefonen og blir ikkje sendt nokon stad.
- Lys og mørk modus følgjer innstillinga på eininga.

Sida må serverast over HTTPS (eller `localhost`) for at posisjonen skal fungere. Køyr ho lokalt med til dømes:

```sh
python3 -m http.server 8000
```

### Bilete

Dei historiske bileta (utsnitt av Scholeus-prospektet av Bergen, kring 1580) ligg i `bilete/`. Dei kan hentast på nytt frå Wikimedia Commons med:

```sh
./hent-bilete.sh
```

## Kjelder

- Absalon Pederssøn Beyer: dagboka (Bergens Kapitelsbog 1552–1572) og *Om Norgis Rige* (1567). [Heile dagboka hos Bokselskap](https://www.bokselskap.no/boker/absalonsdagbok/1552-2)
- [Om dagboka hos Bergen Byarkiv](https://www.bergenbyarkiv.no/oppslagsverket/2003/04/25/absalon-pedersson-beyers-dagbok/)
- [Bergen byleksikon](https://www.bergenbyarkiv.no/bergenbyleksikon/)

## Lisens

- **Kjeldekode:** MIT, sjå [LICENSE](LICENSE).
- **Eigne tekstar** (omsetjingar, ordlister, oppgåver og innleiing): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.no).
- **Absalon sine originaltekstar** og **Scholeus-prospektet** er falne i det fri (public domain).
- **Kartdata:** © OpenStreetMap-bidragsytarar, [ODbL](https://www.openstreetmap.org/copyright).
