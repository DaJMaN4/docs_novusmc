# Media slots for the docs: page -> heading -> list of (asset file, caption, what to capture).
# Asset files live in .gitbook/assets/<file>; .gif = animation, .png = screenshot.
# Run tools/media.py after editing this list.

PLAN = {
    # ------------------------------------------------------------------ start
    "README.md": {
        "# 👋 Witaj": [
            ("ogolne/baner.png", "Survival NovusMC", "Szeroki baner: spawn albo ładny widok świata z logo serwera"),
        ],
        "## Wymiary": [
            ("ogolne/wymiary.png", "Świat Główny, Nether i Kres", "Kolaż trzech wymiarów (po jednym widoku)"),
        ],
    },
    "jak-grac/getting-started.md": {
        "## 1. Znajdź swoje miejsce": [
            ("start/rtp.gif", "Losowa teleportacja /rtp", "Gracz wpisuje /rtp i ląduje w losowym miejscu"),
        ],
        "## 2. Załóż działkę": [
            ("start/dzialka-menu.png", "Menu działek", "Otwarte menu /dzialki"),
        ],
        "## 3. Ustaw dom": [
            ("start/sethome.png", "Ustawianie domu", "Czat po /sethome i /home"),
        ],
        "## 4. Rozwijaj postać": [
            ("start/staty.png", "Menu umiejętności", "Otwarte menu /staty"),
        ],
        "## 5. Zarabiaj": [
            ("start/aukcje.png", "Aukcje graczy", "Otwarte menu /aukcje"),
        ],
    },
    "jak-grac/your-first-project.md": {
        "## Plecak": [("start/plecak.png", "Plecak /plecak", "Otwarty plecak z kilkoma przedmiotami")],
        "## Skrzynie i klucze": [("start/skrzynie.gif", "Otwieranie skrzyni kluczem", "Otwieranie skrzyni na /skrzynie z animacją losowania")],
        "## Piniata": [("start/piniata.gif", "Piniata", "Gracze rozbijają piniatę")],
        "## Strefa AFK": [("start/strefa-afk.png", "Strefa AFK", "Widok strefy AFK")],
        "## Dzienne nagrody": [("start/dzienne-nagrody.png", "Dzienne nagrody", "Menu dziennych nagród")],
    },
    # ------------------------------------------------------------------ informacje
    "informacje/dzialki.md": {
        "## Zakładanie działki": [("informacje/dzialki-granice.gif", "Granice działki", "Podgląd granic działki (cząsteczki) i zakładanie działki")],
        "### Blok Przejęcia": [("informacje/blok-przejecia.png", "Blok Przejęcia", "Postawiony Blok Przejęcia przy granicy działki")],
        "## Budowanie razem": [("informacje/dzialki-zaufani.png", "Zaufani gracze", "Menu zaufanych graczy działki")],
    },
    "informacje/zadania.md": {
        "## Gildie": [("informacje/gildie.png", "Menu zadań gildii", "Otwarte menu /zadania z trzema gildiami")],
        "## Misje": [("informacje/misje.png", "Misje", "Lista misji")],
        "## Runy": [("informacje/runy.png", "Runy", "Kilka run w ekwipunku z opisem")],
    },
    "informacje/umiejetnosci.md": {
        "## Lista umiejętności": [("informacje/umiejetnosci.png", "Menu umiejętności", "Menu /staty z listą 11 umiejętności")],
        "## Zdolności many": [("informacje/zdolnosc-many.gif", "Zdolność many w akcji", "Użycie dowolnej zdolności many")],
    },
    "informacje/sklepy-i-skupy.md": {
        "## Skup": [("informacje/skup.png", "Skup", "Menu skupu")],
        "## Aukcje": [("informacje/aukcje.png", "Aukcje", "Menu aukcji z wystawionymi przedmiotami")],
        "## Sklepy na działce": [("informacje/sklep-skrzynkowy.gif", "Zakładanie sklepu skrzynkowego", "Tworzenie sklepu na skrzyni i zakup przez innego gracza")],
    },
    "informacje/rangi/README.md": {
        "## Porównanie": [("informacje/rangi.png", "Rangi", "Menu /rangi")],
    },
    # ------------------------------------------------------------------ przedmioty
    "dodatki/przedmioty.md": {
        "## Menu przedmiotów": [
            ("przedmioty/menu-przedmiotow.png", "Menu przedmiotów /nova items", "Menu /nova items z zakładkami"),
            ("przedmioty/receptura.gif", "Podgląd receptury", "Klik na przedmiot -> receptura, PPM -> do czego służy"),
        ],
        "## Lucky Block": [("przedmioty/lucky-block.gif", "Lucky Block", "Niszczenie Lucky Blocka i to, co z niego wypada")],
    },
    "dodatki/ekwipunek/README.md": {
        "# ⚔️ Ekwipunek": [("ekwipunek/wszystkie-zestawy.png", "Zestawy zbroi", "Stojaki na zbroję ze wszystkimi zestawami obok siebie")],
        "## Gwiezdny ekwipunek": [("ekwipunek/gwiezdny.png", "Gwiezdny ekwipunek", "Gracz w gwiezdnej zbroi z gwiezdnymi narzędziami")],
    },
    "dodatki/ekwipunek/zestawy-rud.md": {
        "## Przegląd": [("ekwipunek/rudy.png", "Rzadkie rudy", "Rudy: magma, wulkanit, duszmit, topaz, voidium, perłyt, enderyt obok siebie")],
        "## Magmowy": [("ekwipunek/magmowy.png", "Zestaw magmowy", "Stojak z magmową zbroją + narzędzia")],
        "## Shulkera": [
            ("ekwipunek/shulkera.png", "Zestaw shulkera", "Stojak z zbroją shulkera + narzędzia"),
            ("ekwipunek/lewitacja.gif", "Zdolność Lewitacja", "Uderzenie mieczem shulkera unosi moba"),
        ],
        "## Wulkanitowy": [
            ("ekwipunek/wulkanitowy.png", "Zestaw wulkanitowy", "Stojak z wulkanitową zbroją + narzędzia"),
            ("ekwipunek/autosmelt.gif", "Przetapianie rud kilofem", "Kopanie rudy żelaza wulkanitowym kilofem — wypada sztabka"),
        ],
        "## Kresowy (voidium)": [("ekwipunek/kresowy.png", "Zestaw kresowy", "Stojak z kresową zbroją + narzędzia")],
        "## Duszmitowy": [("ekwipunek/duszmitowy.png", "Zestaw duszmitowy", "Stojak z duszmitową zbroją + narzędzia")],
        "## Topazowy": [("ekwipunek/topazowy.png", "Zestaw topazowy", "Stojak z topazową zbroją + narzędzia")],
        "## Perłytowy": [
            ("ekwipunek/perlytowy.png", "Zestaw perłytowy", "Stojak z perłytową zbroją + narzędzia"),
            ("ekwipunek/unik-kresu.gif", "Unik Kresu", "Gracz w pełnym zestawie dostaje cios i teleportuje się"),
        ],
        "## Enderytowy": [
            ("ekwipunek/enderytowy.png", "Zestaw enderytowy", "Stojak z enderytową zbroją + narzędzia"),
            ("ekwipunek/mrugniecie.gif", "Mrugnięcie", "Shift + PPM enderytowym mieczem — teleport do przodu"),
        ],
    },
    "dodatki/ekwipunek/zbroje.md": {
        "## Zbroje z umiejętnościami": [
            ("ekwipunek/immersive-armors.png", "Zbroje z umiejętnościami", "10 stojaków: kościana, drewniana, witherowa, szlamowa, szata maga, wojownika, steampunkowa, boska, ciężka, pryzmarynowa"),
            ("ekwipunek/szlamowa-odbicie.gif", "Szlamowa zbroja — Odbicie", "Mob uderza gracza w szlamowej zbroi i zostaje odrzucony"),
        ],
        "## Zbroja z promethium": [
            ("ekwipunek/promethium.png", "Zbroja z promethium", "Stojak ze zbroją z promethium"),
            ("ekwipunek/chodzenie-po-lawie.gif", "Chodzenie po lawie", "Gracz w butach z promethium chodzi po lawie"),
        ],
        "## Zestawy z Netheru (BetterNether)": [("ekwipunek/betternether-zestawy.png", "Cincinnasite i Nether Ruby", "Stojaki z zestawem cincinnasite i nether ruby + broń")],
    },
    "dodatki/ekwipunek/bron.md": {
        "## Noże": [("ekwipunek/noze.png", "Noże", "5 noży w ramkach na przedmioty")],
        "## Proce": [("ekwipunek/proca.gif", "Strzał z procy", "Napinanie procy i strzał kulką z promethium (wybuch odłamków)")],
        "## Bumerangi": [("ekwipunek/bumerang.gif", "Bumerang", "Rzut bumerangiem, który wraca")],
        "## Trójzęby": [("ekwipunek/trojzab-lojalnosc.gif", "Trójząb z Lojalnością", "Zabicie moba trójzębem — łupy lecą prosto do gracza")],
    },
    "dodatki/ekwipunek/totemy.md": {
        "# 🗿 Totemy": [
            ("ekwipunek/totemy.png", "Totemy", "7 nowych totemów w ramkach na przedmioty"),
            ("ekwipunek/totem-zadlacy.gif", "Żądlący totem", "Gracz ginie z żądlącym totemem — pojawiają się pszczoły"),
            ("ekwipunek/totem-wybuchowy.gif", "Wybuchowy totem", "Gracz ginie z wybuchowym totemem — wybuch wokół niego"),
        ],
    },
    # ------------------------------------------------------------------ maszyny
    "dodatki/maszyny/README.md": {
        "# ⚙️ Maszyny": [("maszyny/fabryka.png", "Przykładowa fabryka", "Szeroki widok gotowej fabryki: generatory, kable, maszyny")],
        "## Menu maszyny": [
            ("maszyny/menu-maszyny.png", "Menu maszyny", "Menu dowolnej maszyny z zaznaczonym paskiem energii, slotami i ulepszeniami"),
            ("maszyny/konfiguracja-stron.png", "Konfiguracja stron", "Ekran konfiguracji stron maszyny"),
        ],
        "## Ramy maszyn i podzespoły": [("maszyny/ramy.png", "Ramy maszyn", "4 ramy maszyn + płytki i koła zębate w ramkach")],
        "## Gwiezdne odłamki": [("maszyny/ruda-gwiezdna.png", "Ruda gwiezdnych odłamków", "Ruda gwiezdnych odłamków w górach")],
        "## Ulepszenia maszyn": [("maszyny/ulepszenia.png", "Ulepszenia maszyn", "5 rodzajów ulepszeń + menu ulepszeń maszyny")],
        "## Klucz": [("maszyny/klucz-kabel.gif", "Ustawianie kabla kluczem", "PPM kluczem w kabel przy maszynie -> menu ustawień połączenia")],
    },
    "dodatki/maszyny/generatory.md": {
        "# ⚡ Generatory": [("maszyny/generatory.png", "Generatory", "Wszystkie generatory obok siebie")],
        "## Generator pieca": [("maszyny/generator-pieca.png", "Generator pieca", "Generator pieca z menu (paliwo, energia)")],
        "## Panel słoneczny": [("maszyny/panele.png", "Panele słoneczne", "Pole paneli słonecznych na dachu")],
        "## Turbina wiatrowa": [("maszyny/turbina.gif", "Turbina wiatrowa", "Kręcąca się turbina wiatrowa")],
        "## Generator Lawy": [("maszyny/generator-lawy.png", "Generator lawy", "Generator lawy podłączony do pompy")],
        "## Wymiennik piorunów": [("maszyny/wymiennik-piorunow.gif", "Wymiennik piorunów", "Piorun uderza w wymiennik w czasie burzy")],
    },
    "dodatki/maszyny/przetwarzanie.md": {
        "## Prasa mechaniczna": [("maszyny/prasa.gif", "Prasa mechaniczna", "Prasa robi płytki z żelaza (menu z postępem)")],
        "## Rozpryskiwacz": [("maszyny/rozdrabniacz.gif", "Rozdrabnianie rud", "Ruda -> 2 pyły w menu rozdrabniacza")],
        "## Piec Elektryczny": [("maszyny/piec-elektryczny.png", "Piec elektryczny", "Menu pieca elektrycznego")],
        "## Crystallizer": [("maszyny/krystalizator.png", "Krystalizator", "Krystalizator z blokiem gwiezdnego pyłu")],
        "## Zamrażarka": [("maszyny/zamrazarka.png", "Zamrażarka", "Menu zamrażarki z wyborem lodu")],
        "## Generator Bruku": [("maszyny/generator-bruku.gif", "Generator bruku", "Generator bruku + niszczyciel bloków / kabel do skrzyni")],
        "## Zaparzacz do płynów": [("maszyny/zaparzacz.png", "Zaparzacz do płynów", "Menu zaparzacza (wiadro -> wiadro wody)")],
        "## Elektryczny stojak do parzenia piwa": [("maszyny/stojak-mikstur.png", "Elektryczny stojak do parzenia", "Menu wyboru efektów mikstury")],
        "## Auto Crafter": [("maszyny/auto-crafter.gif", "Auto Crafter", "Ustawianie receptury i automatyczne craftowanie")],
        "## Ładowarka i Ładowarka bezprzewodowa": [("maszyny/ladowarka.png", "Ładowarka", "Ładowarka z ładującym się jetpackiem")],
    },
    "dodatki/maszyny/farmy.md": {
        "# 🌾 Farmy": [("maszyny/farma-automatyczna.png", "Automatyczna farma", "Pole uprawne z sadzarką, żniwiarką, zraszaczem i użyźniaczem")],
        "## Sadzarka": [("maszyny/sadzarka.gif", "Sadzarka", "Sadzarka sadzi nasiona na pustym polu")],
        "## Żniwiarka": [("maszyny/zniwiarka.gif", "Żniwiarka", "Żniwiarka zbiera dojrzałą pszenicę")],
        "## Użyźniacz gleby": [("maszyny/uzyzniacz.gif", "Użyźniacz gleby", "Rośliny rosną po mączce z użyźniacza")],
        "## Zraszacz": [("maszyny/zraszacz.gif", "Zraszacz", "Zraszacz nawadnia pole")],
        "## Fabryka Drzew": [("maszyny/fabryka-drzew.gif", "Fabryka drzew", "Drzewo rośnie w fabryce drzew")],
        "## Hodowca": [("maszyny/hodowca.png", "Hodowca", "Hodowca w zagrodzie z krowami")],
        "## Zabójca mobów": [("maszyny/zabojca-mobow.gif", "Zabójca mobów", "Farma mobów: zabójca + skrzynia próżniowa")],
        "## Zbieracz mobów i Duplikator mobów": [("maszyny/duplikator.gif", "Duplikator mobów", "Łapanie moba zbieraczem i duplikator tworzący kopie")],
        "## Automatyczna rybiarka": [("maszyny/rybiarka.png", "Automatyczna rybiarka", "Rybiarka nad wodą z menu")],
    },
    "dodatki/maszyny/wydobycie.md": {
        "## Kamieniołom": [
            ("maszyny/kamieniolom.gif", "Kamieniołom w pracy", "Kamieniołom z rusztowaniem kopiący obszar (przyspieszone nagranie)"),
            ("maszyny/kamieniolom-menu.png", "Ustawienia kamieniołomu", "Menu kamieniołomu z rozmiarem obszaru"),
        ],
        "## Niszczyciel Bloków": [("maszyny/niszczyciel.gif", "Niszczyciel bloków", "Niszczyciel bloków przy generatorze bruku")],
        "## Stawiacz bloków": [("maszyny/stawiacz.gif", "Stawiacz bloków", "Stawiacz stawiający bloki")],
        "## Pompa": [("maszyny/pompa.gif", "Pompa", "Pompa wypompowuje jezioro lawy")],
        "## Ładowarka chunków": [("maszyny/ladowarka-chunkow.png", "Ładowarka chunków", "Ładowarka chunków z podglądem zasięgu")],
        "## Star Collector": [("maszyny/star-collector.gif", "Star Collector", "Zbieranie gwiezdnego pyłu nocą")],
    },
    "dodatki/maszyny/logistyka.md": {
        "## Kable": [("maszyny/kable.png", "Kable", "4 rodzaje kabli łączące maszyny")],
        "## Ogniwa zasilające": [("maszyny/ogniwo-wykres.png", "Ogniwo zasilające", "Menu ogniwa z wykresem energii")],
        "## Zbiorniki płynów": [("maszyny/zbiorniki.png", "Zbiorniki płynów", "Zbiorniki z wodą i lawą")],
        "## Filtry przedmiotów": [("maszyny/filtr.png", "Filtr przedmiotów", "Menu filtra (biała / czarna lista)")],
        "## Jednostki magazynowe": [("maszyny/jednostka-magazynowa.png", "Jednostka magazynowa", "Jednostka magazynowa z tysiącami bruku")],
        "## Skrzynia próżniowa": [("maszyny/skrzynia-prozniowa.gif", "Skrzynia próżniowa", "Skrzynia wciąga leżące przedmioty")],
    },
    # ------------------------------------------------------------------ inne dodatki
    "dodatki/przechowywanie.md": {
        "## Skrzynie metalowe": [
            ("przechowywanie/skrzynie.png", "Skrzynie metalowe", "Wszystkie skrzynie metalowe obok siebie"),
            ("przechowywanie/krysztalowa.png", "Kryształowa skrzynia", "Kryształowa skrzynia pokazująca przedmioty na wierzchu"),
        ],
        "### Ulepszanie skrzyń": [("przechowywanie/ulepszanie-skrzyni.gif", "Ulepszanie skrzyni", "Klik ulepszeniem w skrzynię — zmienia się, zawartość zostaje")],
        "## Szuflady": [("przechowywanie/szuflady.png", "Szuflady", "Ściana szuflad z przedmiotami i liczbami")],
        "### Jak używać": [("przechowywanie/szuflady-uzycie.gif", "Wkładanie do szuflad", "Wkładanie i wyjmowanie przedmiotów z szuflady, dwuklik")],
        "### Klucz i kontroler": [("przechowywanie/kontroler.gif", "Kontroler szuflad", "Wkładanie stosu do kontrolera — rozchodzi się do szuflad")],
        "## Kosz na śmieci": [("przechowywanie/kosz.png", "Kosz na śmieci", "Menu kosza z górnym rzędem i filtrem")],
        "## Plecaki podróżnika": [
            ("przechowywanie/plecaki.png", "Plecaki podróżnika", "Kilkanaście postawionych plecaków różnych wzorów"),
            ("przechowywanie/plecak-menu.png", "Menu plecaka", "Otwarty plecak ze zbiornikami i slotem ulepszenia"),
        ],
    },
    "dodatki/piece.md": {
        "# 🔥 Piece": [("piece/piece.png", "Piece", "Wszystkie piece obok siebie")],
        "## Ulepszanie pieca": [("piece/ulepszanie.gif", "Ulepszanie pieca", "Klik ulepszeniem pieca w działający piec")],
        "## Dodatki do pieca": [("piece/dodatki.png", "Dodatki do pieca", "Menu pieca z włożonymi dodatkami")],
        "## Automatyzacja": [("piece/automatyzacja.png", "Automatyczne przetapianie", "Piec z lejkami: góra, bok, dół")],
    },
    "dodatki/narzedzia.md": {
        "## Młoty": [
            ("narzedzia/mloty.png", "Młoty", "Wszystkie młoty w ramkach na przedmioty"),
            ("narzedzia/mlot-3x3.gif", "Kopanie młotem", "Kopanie tunelu 3x3 młotem"),
        ],
        "## Stół nasycania zaklęć": [
            ("narzedzia/stol-nasycania.png", "Stół nasycania zaklęć", "Stół otoczony biblioteczkami"),
            ("narzedzia/stol-nasycania-menu.gif", "Wybieranie zaklęć", "Wybór zaklęć LPM/PPM i zaczarowanie przedmiotu"),
        ],
    },
    "dodatki/wedkarstwo.md": {
        "# 🎣 Wędkarstwo": [("wedkarstwo/ryby.png", "Nowe ryby", "Kolekcja złowionych ryb w ramkach / akwarium")],
        "## Wędki": [("wedkarstwo/wedki.png", "Wędki", "Wszystkie wędki w ramkach")],
        "## Skrzynie z łowienia": [("wedkarstwo/skrzynia.gif", "Skrzynia z łowienia", "Wyłowienie i otwarcie skrzyni")],
        "## Łowienie w lawie": [
            ("wedkarstwo/lowienie-w-lawie.gif", "Łowienie w lawie", "Spławik na lawie, branie i wyciągnięcie ryby"),
            ("wedkarstwo/skarb-prometeusza.gif", "Skarb Prometeusza", "Otwieranie Skarbu Prometeusza"),
        ],
        "## Pułapka na ryby": [
            ("wedkarstwo/pulapka.png", "Pułapka na ryby", "Pułapka postawiona w wodzie przy plaży"),
            ("wedkarstwo/pulapka-menu.png", "Menu pułapki", "Menu pułapki z przynętą i złowionymi rybami"),
        ],
    },
    "dodatki/pojazdy.md": {
        "## Jetpacki": [
            ("podroze/jetpack.gif", "Lot jetpackiem", "Lot jetpackiem nad bazą"),
            ("podroze/jetpacki.png", "Jetpacki", "Wszystkie jetpacki (zwykłe i opancerzone) na stojakach"),
        ],
        "## Lotnie": [("podroze/lotnia.gif", "Lotnia", "Szybowanie lotnią z góry")],
        "## Windy": [("podroze/winda.gif", "Winda", "Skok w górę i kucnięcie w dół między windami")],
        "## Kamienie podróży": [
            ("podroze/kamien-podrozy.png", "Kamień podróży", "Postawiony kamień podróży"),
            ("podroze/kamien-podrozy-menu.png", "Menu kamieni podróży", "Lista kamieni do teleportu"),
        ],
        "## Łączniki refrenu": [("podroze/lacznik-refrenu.gif", "Łącznik refrenu", "Zjedzenie owocu refrenu i teleport na łącznik")],
        "## Przekaźnik Kresu": [("podroze/przekaznik-kresu.gif", "Przekaźnik Kresu", "Ładowanie przekaźnika kryształem i teleport")],
        "## Łodzie": [("podroze/lodzie.png", "Nowe łodzie", "Kilka łodzi z nowych drewien na wodzie")],
    },
    "dodatki/groby.md": {
        "# 🪦 Groby": [("groby/grob.png", "Grób gracza", "Grób z imieniem, datą i głową gracza")],
        "## Jak odzyskać przedmioty": [("groby/odbieranie.gif", "Odbieranie przedmiotów", "PPM na grób — przedmioty wracają do ekwipunku")],
        "## Niszczenie grobów": [("groby/stopnie.png", "Stopnie zniszczenia", "Grób cały, wyszczerbiony i zniszczony obok siebie")],
    },
    "dodatki/bloki-budowlane.md": {
        "# 🧱 Bloki budowlane": [("bloki/budowla.png", "Budowla z nowych bloków", "Ładna budowla z nowych bloków (np. dom z dachówkami)")],
        "## Blockus — kamienie, cegły i dekoracje": [
            ("bloki/blockus-kamienie.png", "Kamienie i cegły", "Ściana próbek kamieni i cegieł Blockus"),
            ("bloki/blockus-kolorowe.png", "Kolorowe bloki", "Kolorowe kafelki, neony, lampy"),
        ],
        "## Dawn of Time — tradycyjne budownictwo": [("bloki/dawn-of-time.png", "Tradycyjne budownictwo", "Dom z szachulca z dachówkami i pergolą")],
        "## Pionowe płyty": [("bloki/pionowe-plyty.png", "Pionowe płyty", "Przykład użycia pionowych płyt")],
        "### Świat Główny": [("bloki/drewno-swiat.png", "Nowe drewno", "Deski i kłody wszystkich nowych drzew")],
        "### Nether": [("bloki/drewno-nether.png", "Drewno z Netheru", "Deski, meble i szkło z Netheru")],
    },
    "dodatki/meble.md": {
        "# 🪑 Meble": [("meble/pokoj.png", "Urządzony pokój", "Pokój urządzony meblami z serwera")],
        "## Rodzaje mebli": [
            ("meble/kuchnia.png", "Kuchnia", "Kuchnia z szafkami i kuchenką"),
            ("meble/salon.png", "Salon", "Salon z sofą, lampami i stołem"),
            ("meble/ploty.png", "Płoty i mury", "Różne płoty, mury i żywopłoty"),
        ],
        "## Jak używać mebli": [("meble/siadanie.gif", "Siadanie na meblach", "Siadanie na krześle i otwieranie szafki")],
    },
    "dodatki/gotowanie.md": {
        "# 🧑‍🍳 Gotowanie": [("gotowanie/kuchnia.png", "Kuchnia", "Kuchnia z kuchenką, garnkiem i deską do krojenia")],
        "## Nowe uprawy": [("gotowanie/uprawy.png", "Nowe uprawy", "Pole z kapustą, pomidorami, cebulą i ryżem")],
        "## Wyposażenie kuchni": [("gotowanie/garnek.gif", "Gotowanie w garnku", "Gotowanie zupy w garnku na kuchence")],
        "## Potrawy": [("gotowanie/potrawy.png", "Potrawy", "Stół zastawiony dużymi daniami")],
        "## Mięso z dzikich zwierząt": [("gotowanie/mieso.png", "Mięso z dzikich zwierząt", "Surowe i pieczone mięsa w ramkach")],
        "## Wystawianie jedzenia": [("gotowanie/talerze.gif", "Wystawianie jedzenia", "Kładzenie jedzenia na talerzu")],
    },
    "dodatki/insekty.md": {
        "## Siatka na owady": [("insekty/lapanie.gif", "Łapanie owadów", "Łapanie motyla siatką")],
        "## Terraria": [("insekty/terraria.png", "Terraria", "Półka z terrariami pełnymi owadów")],
    },
    # ------------------------------------------------------------------ wymiary
    "wymiary/swiat-glowny/README.md": {
        "# 🌍 Świat Główny": [("swiat/panorama.png", "Świat Główny", "Panorama świata z nowymi biomami")],
        "## Rudy": [("swiat/topaz.png", "Ruda topazu", "Ruda topazu w łupku")],
    },
    "wymiary/swiat-glowny/biomy.md": {
        "## Lasy": [
            ("biomy/sekwoje.png", "Redwoods", "Las sekwojowy"),
            ("biomy/klony.png", "Autumnal Maple Forest", "Jesienny las klonowy"),
            ("biomy/glicynie.png", "Wisteria Grove", "Gaj glicynii"),
        ],
        "## Równiny i łąki": [("biomy/pola-kwiatow.png", "Flower Fields", "Pola kwiatów")],
        "## Pustynie i sawanny": [
            ("biomy/saguaro.png", "Saguaro Desert", "Pustynia z kaktusami saguaro"),
            ("biomy/baobaby.png", "Baobab Savanna", "Sawanna z baobabami"),
        ],
        "## Bagna i rzeki": [("biomy/bayou.png", "Bayou", "Cyprysowe bagno")],
        "## Góry i klify": [("biomy/kredowe-klify.png", "Chalk Cliffs", "Kredowe klify nad morzem")],
        "## Wybrzeża i oceany": [("biomy/hyacinth-deeps.png", "Hyacinth Deeps", "Podwodne kwiaty w głębinach")],
        "## Jaskinie": [
            ("biomy/bioshroom.png", "Bioshroom Caves", "Świecące grzyby w jaskini"),
            ("biomy/prismachasm.png", "Prismachasm", "Kolorowe kryształy w jaskini"),
        ],
    },
    "wymiary/swiat-glowny/struktury.md": {
        "## Odnowione struktury": [("struktury/starozytne-miasto.png", "Starożytne miasto", "Odnowione starożytne miasto")],
        "## Nowe struktury": [
            ("struktury/tawerna.png", "Tawerna", "Tawerna z zewnątrz"),
            ("struktury/katakumby.png", "Katakumby", "Wnętrze katakumb"),
            ("struktury/wieza.png", "Wieża obserwacyjna", "Wieża obserwacyjna w lesie"),
        ],
    },
    "wymiary/swiat-glowny/potwory.md": {
        "## Szkielety": [("potwory/szkielety.png", "Szkielety", "Odmiany szkieletów obok siebie")],
        "## Inne potwory": [("potwory/inne.png", "Nowe potwory", "Kobold, salamandra, lodowy zombie")],
        "## Bossowie": [("potwory/boss.gif", "Walka z bossem", "Fragment walki z bossem")],
    },
    "wymiary/swiat-glowny/zwierzeta.md": {
        "# 🐄 Zwierzęta": [("zwierzeta/zoo.png", "Nowe zwierzęta", "Kolaż kilku zwierząt (niedźwiedź, słoń, tukan, orka)")],
        "## Lasy i tajgi": [("zwierzeta/grizzly.png", "Niedźwiedź Grizzly", "Niedźwiedź grizzly w lesie")],
        "## Sawanny, pustynie i badlandy": [("zwierzeta/slon.png", "Słoń", "Słonie na sawannie")],
        "## Dżungle": [("zwierzeta/goryl.png", "Goryl", "Goryle w dżungli")],
        "## Bagna i rzeki": [("zwierzeta/krokodyl.png", "Krokodyl", "Krokodyl przy rzece")],
        "## Plaże i morza": [("zwierzeta/orka.gif", "Orka", "Pływająca orka")],
        "## Jaskinie": [("zwierzeta/trzepotnik.png", "Trzepotnik", "Trzepotnik w bujnej jaskini")],
    },
    "wymiary/nether/README.md": {
        "# 🔥 Nether": [("nether/panorama.png", "Nether", "Panorama Netheru z nowymi biomami")],
    },
    "wymiary/nether/biomy.md": {
        "## Lasy": [
            ("nether/dzungla.png", "Nether Jungle", "Netherowa dżungla"),
            ("nether/grzybowy-las.png", "Nether Mushroom Forest", "Las ogromnych grzybów"),
            ("nether/odwrocony-las.png", "Upside Down Forest", "Odwrócony las"),
        ],
        "## Bagna i równiny": [("nether/mokradla.png", "Nether Swampland", "Netherowe mokradła")],
        "## Pustkowia": [("nether/koscista-rafa.png", "Bone Reef", "Kościana rafa")],
    },
    "wymiary/nether/struktury.md": {
        "## Nowe struktury": [
            ("nether/port.png", "Port Netheru", "Port Netheru"),
            ("nether/swiatynia.png", "Świątynia w dżungli", "Świątynia w netherowej dżungli"),
        ],
    },
    "wymiary/nether/potwory.md": {
        "## Potwory": [("nether/naga.png", "Naga", "Naga w Netherze")],
        "## Stworzenia": [("nether/lewiatan.gif", "Lewiatan", "Lewiatan na jeziorze lawy")],
    },
    "wymiary/nether/przedmioty.md": {
        "## Rudy": [("nether/rudy.png", "Rudy Netheru", "Rudy: magma, wulkanit, duszmit, cincinnasite, rubin")],
    },
    "wymiary/kres/README.md": {
        "# 👾 Kres": [("kres/panorama.png", "Kres", "Panorama wysp Kresu")],
    },
    "wymiary/kres/biomy.md": {
        "# 🌌 Biomy": [("kres/biomy.png", "Biomy Kresu", "Kryształowe szczyty / krainy cieni")],
    },
    "wymiary/kres/struktury.md": {
        "# 🌆 Struktury": [("kres/zamek.png", "Zamek Kresu", "Zamek Kresu")],
    },
    "wymiary/kres/potwory.md": {
        "# 😈 Potwory": [("kres/enderling.png", "Enderling", "Enderling i Ender Watchman")],
        "## Stworzenia Kresu": [("kres/zjawa.gif", "Zjawa", "Latająca zjawa nad wyspami")],
    },
    "wymiary/kres/przedmioty.md": {
        "## Rudy": [("kres/rudy.png", "Rudy Kresu", "Voidium, perłyt i enderyt w kamieniu Kresu")],
    },
}
