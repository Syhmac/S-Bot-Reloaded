## -- Uniwersalne zwroty --
genericMember = "użytkownik"
genericReason = "powód"
genericChoice = "wybór"
genericAmount = "ilość"
## -- Komunikaty błędów --
errorNoPermission = "Nie masz uprawnień do użycia tej komendy."
errorForbidden = "Nie mam uprawnień do wykonania tej akcji."
errorUnexpected = "Wystąpił nieoczekiwany błąd podczas wykonywania tej komendy."
errorCooldown = "Nie możesz użyć tej komendy w tej chwili. Spróbuj ponownie za {time}s."
errorInsufficientBalance = "Nie masz wystarczająco monet, aby wykonać tę akcję. Potrzebujesz {amount_needed} :coin:, a masz tylko {amount_got} :coin:."
## -- Komendy użytkowe --
# ping
pingCommandName = "ping"
pingCommandDescription = "Sprawdza opóźnienie bota"
pingCommandResponse = "Pong! Opóźnienie bota wynosi {latency} ms."
## -- Komendy ekonomii --
# economy commons
economyCommonWin = "Wygrałeś/aś!"
economyCommonLoss = "Przegrałeś/aś!"
# balance
balanceCommandName = "balans"
balanceCommandDescription = "Sprawdza twój aktualny balans"
balanceCommandResponse = "Twój aktualny balans wynosi {balance} :coin:."
# bal top
balTopCommandName = "bal_top"
balTopCommandDescription = "Sprawdza ranking bogactwa na serwerze"
balTopCommandEmbedTitle = "Ranking bogactwa"
balTopCommandResponse = "10 najbogatszych użytkowników serwera:\n"
balTopCommandNoData = "Żaden użytkownik tego serwera nie ma jeszcze żadnych monet."
# bal stats
balStatsCommandName = "bal_stats"
balStatsCommandDescription = "Sprawdza twoje statystyki ekonomiczne"
balStatsEmbedTitle = "Twoje statystyki ekonomiczne"
balStatsEmbedFiledBalanceName = "Balans"
balStatsEmbedFiledJobsName = "Wykonane prace"
balStatsEmbedFiledJobMultName = "Mnożnik zarobków z prac"
balStatsEmbedFiledGamblingWinsName = "Wygrane w kasynie"
balStatsEmbedFiledGamblingLossesName = "Przegrane w kasynie"
balStatsEmbedFiledFishCaughtName = "Złapane ryby"
balStatsEmbedFiledFishMultName = "Mnożnik wartości ryb"
balStatsEmbedFieldCrimesName = "Popełnione przestępstwa"
balStatsCommandNoData = "Brak danych do pokazania."
# job
jobCommandName = "pracuj"
jobCommandDescription = "Zarabiaj pieniądze wykonując różne prace."
jobList = {
    1: "Użytkownik `{user}` poszedł do pracy do McDonald's i zarobił {earnings} :coin:.",
    2: "Użytkownik `{user}` poszedł na kasę do Biedronki i zarobił {earnings} :coin:.",
    3: "Użytkownik `{user}` pracował jako barista w lokalnej kawiarni i zarobił {earnings} :coin:. Dostał również {tips} :coin: napiwku!",
    4: "Użytkownik `{user}` rozwoził jedzenie w Pyszne.pl i zarobił {earnings} :coin:. Dostał również {tips} :coin: napiwku za szybką dostawę!",
    5: "Użytkownik `{user}` wziął zlecenie programistyczne i zarobił {earnings} :coin:.",
    6: "Użytkownik `{user}` został kanarem i zarobił {earnings} :coin: za łapanie pasażerów na gapę.",
    7: "Użytkownik `{user}` skosił trawnik sąsiadowi i zarobił {earnings} :coin: z dodatkowym {tips} :coin: napiwku za świetną robotę!",
    8: "Użytkownik `{user}` wyprowadził psa na godzinny spacer i zarobił {earnings} :coin:. Właściciel psa dał mu {tips} :coin: napiwku za utrzymanie psa w dobrym humorze!",
    9: "Użytkownik `{user}` wytrzymał cały dzień pilnując czyjeś dziecko i zarobił {earnings} :coin:. Dostał również {tips} :coin: napiwku za to, że dziecko się nie nudziło!",
    10: "Użytkownik `{user}` posprzątał czyjś dom i zarobił {earnings} :coin:. Dostał również {tips} :coin: napiwku za starcie kurzu z wysokich półek!",
    11: "Użytkownik `{user}` umył samochód i zarobił {earnings} :coin:. Dostał również {tips} :coin: napiwku za to, że samochód aż błyszczy!",
    12: "Użytkownik `{user}` naprawił komputer i zarobił {earnings} :coin:.",
    13: "Użytkownik `{user}` udzielił korepetycji uczniowi i zarobił {earnings} :coin:. Dostał również {tips} :coin: napiwku po tym, jak uczeń zdał test z oceną 6!",
    14: "Użytkownik `{user}` poszedł pracować w biurze i zarobił {earnings} :coin:.",
    15: "Użytkownik `{user}` pracował jako barman i zarobił {earnings} :coin: z dodatkowym {tips} :coin: napiwku za robienie świetnych koktajli!",
    16: "Użytkownik `{user}` pracował jako kelner i zarobił {earnings} :coin: z dodatkowym {tips} :coin: napiwku za świetną obsługę!",
    17: "Użytkownik `{user}` pracował jako ochroniarz i zarobił {earnings} :coin:.",
    18: "Użytkownik `{user}` pomógł zorganizować wydarzenie i zarobił {earnings} :coin:.",
    19: "Użytkownik `{user}` pracował jako śmieciarz. To była brudna robota, ale przynajmniej zarobił {earnings} :coin:.",
    20: "Użytkownik `{user}` przetłumaczył ważny dokument i zarobił {earnings} :coin:.",
    21: "Użytkownik `{user}` pracował jako kierowca Bolta i zarobił {earnings} :coin:. Dostał również {tips} :coin: napiwku za płynną jazdę!",
    22: "Użytkownik `{user}` pracował w Żabce i zarobił {earnings} :coin:.",
    23: "Użytkownik `{user}` wziął zlecenie na zrobienie rysunku i zarobił {earnings} :coin:.",
    24: "Użytkownik `{user}` napisał post na bloga i zarobił {earnings} :coin:.",
    25: "Użytkownik `{user}` pracował w call center i zarobił {earnings} :coin:.",
    26: "Użytkownik `{user}` wykonał prace ogrodnicze i zarobił {earnings} :coin:. Dostał również {tips} :coin: napiwku za sprawienie, że kwiaty wyglądają lepiej niż kiedykolwiek!",
    27: "Użytkownik `{user}` wydrukował model 3D dla klienta i zarobił {earnings} :coin:.",
    28: "Użytkownik `{user}` zrobił sesję zdjęciową i zarobił {earnings} :coin:.",
    29: "Użytkownik `{user}` pracował jako kucharz w restauracji i zarobił {earnings} :coin:.",
    30: "Użytkownik `{user}` zrobił film na YouTube i zarobił {earnings} :coin: z reklam.",
    31: "Użytkownik `{user}` zrobił livestream na Twitch i zarobił {earnings} :coin: z donacji i subskrypcji.",
    32: "Użytkownik `{user}` pracował jako policjant i zarobił {earnings} :coin: za wystawienie wystarczającej liczby mandatów parkingowych.",
    33: "Użytkownik `{user}` pracował jako strażak i zarobił {earnings} :coin: za ugaszenie pożaru.",
    34: "Użytkownik `{user}` pracował jako ratownik medyczny i zarobił {earnings} :coin: za uratowanie życia.",
    35: "Użytkownik `{user}` pracował jako nauczyciel i zarobił {earnings} :coin: za przekazanie swojej wiedzy uczniom.",
    36: "Użytkownik `{user}` pracował jako kierowca autobusu i zarobił {earnings} :coin:.",
    37: "Użytkownik `{user}` pracował jako konduktor i zarobił {earnings} :coin: za sprawdzanie biletów pasażerów.",
    38: "Użytkownik `{user}` pracował jako maszynista pociągu i zarobił {earnings} :coin:",
    39: "Użytkownik `{user}` pracował jako pilot i zarobił {earnings} :coin:.",
    40: "Użytkownik `{user}` poleciał w kosmos jako astronauta i zarobił {earnings} :coin:.",
    41: "Użytkownik `{user}` pracował jako motorniczy tramwaju i zarobił {earnings} :coin:.",
    42: "Użytkownik `{user}` kupił kilka produktów na AliExpress i odsprzedał je na Allegro z zyskiem, zarabiając {earnings} :coin:.",
    43: "Użytkownik `{user}` pracował jako weterynarz i zarobił {earnings} :coin: za leczenie chorych zwierząt.",
    44: "Użytkownik `{user}` pracował jako wolontariusz w schronisku dla zwierząt. Nie zarobił żadnych pieniędzy, ale przynajmniej pomógł kilku uroczym zwierzakom! Miejmy tylko nadzieję, że to nie było schronisko DIOZu.",
    45: "Użytkownik `{user}` pracował jako kierowca ciężarówki i zarobił {earnings} :coin: za dostarczenie świeżych bułek i wędlin.",
    46: "Użytkownik `{user}` połączył kilka kabli i naprawił elektryczność w domu, zarabiając {earnings} :coin:.",
    47: "Użytkownik `{user}` naprawił cieknący kran i zarobił {earnings} :coin:.",
    48: "Użytkownik `{user}` zbudował ładny stolik kawowy i zarobił {earnings} :coin:.",
    49: "Użytkownik `{user}` chodził od drzwi do drzwi sprzedając odkurzacze Zelmera i zarobił {earnings} :coin:.",
    50: "Użytkownik `{user}` wziął swoją gitarę na ulicę i zagrał trochę muzyki, zarabiając {earnings} :coin: w datkach od przechodniów.",
    51: "Użytkownik `{user}` zebrał plony na swojej farmie i sprzedał je na ryneczku za {earnings} :coin:.",
    52: "Użytkownik `{user}` zrobił ręcznie bransoletkę i sprzedał ją online za {earnings} :coin:.",
    53: "Użytkownik `{user}` wynajął swój samochód za {earnings} :coin:.",
    54: "Użytkownik `{user}` pomógł komuś przeprowadzić się do nowego domu i zarobił {earnings} :coin:.",
    55: "Użytkownik `{user}` wziął udział w testach beta nowej aplikacji i zarobił {earnings} :coin: za udzielanie opinii i zgłaszanie błędów.",
    56: "Użytkownik `{user}` wypełnił kilka płatnych ankiet i zarobił {earnings} :coin: za podzielenie się swoją opinią.",
    57: "Użytkownik `{user}` pracował jako opiekun zoo i zarobił {earnings} :coin: za opiekę nad zwierzętami.",
    58: "Użytkownik `{user}` pracował jako przewodnik w muzeum i zarobił {earnings} :coin: za oprowadzanie turystów po wystawach.",
    59: "Użytkownik `{user}` zrobił fandub popularnego filmu i zarobił {earnings} :coin: z reklam i sponsorów.",
    60: "Użytkownik `{user}` podłożył głos do reklamy i zarobił {earnings} :coin:.",
    61: "Użytkownik `{user}` pracował w budce z hot dogami i zarobił {earnings} :coin:.",
    62: "Użytkownik `{user}` jeździł po okolicy samochodem z lodami i zarobił {earnings} :coin:.",
    63: "Użytkownik `{user}` pracował jako recepcjonista hotelowy i zarobił {earnings} :coin:.",
    64: "Użytkownik `{user}` pracował jako ratownik na basenie i zarobił {earnings} :coin:.",
    65: "Użytkownik `{user}` pracował jako osobista pokojówka i zarobił {earnings} :coin:. Tak, musiał przez cały czas nosić strój pokojówki."
}
# coinflip
coinflipCommandName = "coinflip"
coinflipCommandDescription = "Pozwala postawić twoje monety na orła lub reszkę"
coinflipCommandChoiceDescription = "Wybierz orła lub reszkę"
coinflipCommandChoiceHeads = "Orzeł"
coinflipCommandChoiceTails = "Reszka"
coinflipCommandAmountDescription = "Ilość monet do obstawienia"
coinflipCommandEmbedHeadsCorrect = "Postawiłeś/aś {amount} :coin: na orła i wygrałeś/aś!"
coinflipCommandEmbedHeadsIncorrect = "Obstawiłeś/aś orła, a wyleciała reszka. Przegrałeś/aś {amount} :coin:."
coinflipCommandEmbedTailsCorrect = "Reszka to był prawidłowy wybór! Wygrałeś/aś {amount} :coin:!"
coinflipCommandEmbedTailsIncorrect = "Obstawiłeś/aś reszkę, ale wyleciał orzeł. Przegrałeś/aś {amount} :coin:."
## -- Komendy administracyjne --
# kick
kickCommandName = "wyrzuć"
kickCommandDescription = "Wyrzuca użytkownika z serwera"
kickCommandMemberDescription = "Użytkownik do wyrzucenia"
kickCommandReasonDescription = "Powód wyrzucenia użytkownika"
kickCommandResponse = "{member} został/a wyrzucony z serwera. Powód: {reason}"
kickCommandResponseNoReason = "{member} został/a wyrzucony z serwera."
# ban
banCommandName = "ban"
banCommandDescription = "Wysyła użytkownika na banicję"
banCommandMemberDescription = "Użytkownik do zbanowania"
banCommandReasonDescription = "Powód zbanowania użytkownika"
banCommandResponse = "{member} został/a zesłany na banicję. Powód: {reason}"
banCommandResponseNoReason = "{member} został/a zesłany na banicję"
banCommandTime = "usuwanie_wiadomości"
banCommandTimeDescription = "Ile wiadomości usunąć na podstawie czasu."
banCommandTimeNone = "Nie usuwaj wiadomości"
banCommandTime1hr = "Ostatnia godzina"
banCommandTime6hr = "Ostatnie 6 godzin"
banCommandTime12hr = "Ostatnie 12 godzin"
banCommandTime24hr = "Ostatnie 24 godziny"
banCommandTime3d = "Ostatnie 3 dni"
banCommandTime7d = "Ostatnie 7 dni"
# unban
unbanCommandName = "unban"
unbanCommandDescription = "Odbanowuje użytkownika z serwera"
unbanCommandMemberDescription = "Użytkownik do odbanowania"
unbanCommandResponse = "{member} został/a odbanowany z serwera."
# timeout
timeoutCommandName = "wycisz"
timeoutCommandDescription = "Wycisza użytkownika na określony czas"
timeoutCommandMemberDescription = "Użytkownik do wyciszenia"
timeoutCommandReasonDescription = "Powód wyciszenia"
timeoutCommandResponse = "{member} został/a wyciszony/a na `{time}`. Powód: {reason}"
timeoutCommandResponseNoReason = "{member} został/a wyciszony/a na `{time}`."
timeoutCommandTime = "długość_wyciszenia"
timeoutCommandTimeDescription = "Długość wyciszenia."
timeoutCommandTime10m = "10 minut"
timeoutCommandTime30m = "30 minut"
timeoutCommandTime1hr = "1 godzina"
timeoutCommandTime3hr = "3 godziny"
timeoutCommandTime6hr = "6 godzin"
timeoutCommandTime12hr = "12 godzin"
timeoutCommandTime24hr = "24 godziny"
timeoutCommandTime3d = "3 dni"
timeoutCommandTime7d = "7 dni"