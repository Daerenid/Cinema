from app.models import Film, Cinema


c1 = Cinema(name="Helios")
c2 = Cinema(name="Ballada")
c3 = Cinema(name="Zorza")

c1.add_cinema()
c2.add_cinema()
c3.add_cinema()

f1 = Film(
    name="Król Lew", 
    year = 2019,
    description="W wyniku podstępu Skazy prawowity władca afrykańskiej sawanny, Simba, zostaje wygnany. Razem z dwójką przyjaciół zamierza odzyskać tron.",
    vote_count = 0,
    posterurl = "https://m.media-amazon.com/images/I/61sJaBqGxZL._AC_SL1184_.jpg",
    movieurl = "https://www.youtube.com/watch?v=lFzVJEksoDY&ab_channel=DisneyPlus",
    cinema_id = 1
    )
f2 = Film(
    name="Eragon", 
    year = 2006,
    description="Eragon – młody, wiejski chłopak znajduje niebieski kamień i przynosi go do domu. Ale zanim udaje mu się sprzedać go handlarzowi, z kamienia wykluwa się szafirowy smok, Saphira. Smoka próbuje ukraść zły Urgals, który brutalnie morduje wuja Eragona. Chłopcu i smoczycy w ostatniej chwili udaje się uciec. Od tej chwili Eragon poprzysięga zemstę mordercy wuja i wyrusza na wyprawę, by uratować świat i stać się ostatnim legendarnym Jeźdźcem Smoków.",
    vote_count = 0,
    posterurl = "https://fwcdn.pl/fpo/60/74/196074/7537948.3.jpg",
    movieurl = "https://www.filmweb.pl/video/Zwiastun/Eragon+Zwiastun+nr+1-17962",
    cinema_id = 1
    )
f3 = Film(
    name="Milczenie owiec", 
    year = 1991,
    description="Seryjny morderca i inteligentna agentka łączą siły, by znaleźć przestępcę obdzierającego ze skóry swoje ofiary.",
    vote_count = 0,
    posterurl = "https://fwcdn.pl/fpo/10/47/1047/7714177.3.jpg",
    movieurl = "https://www.youtube.com/watch?v=pz1HaKMXltI",
    cinema_id = 1
    )
f4 = Film(
    name="Mordercza opona", 
    year = 2010,
    description="Posiadająca zdolności parapsychologiczne opona samochodowa obsesyjnie podąża za kobietą, pozbawiając życia każdego, kto stanie jej na drodze.",
    vote_count = 0,
    posterurl = "https://www.kinoluna.pl/sites/default/files/tresc/film/2018/mordercza_opona/poster/mordercza_opona.jpg",
    movieurl = "https://www.filmweb.pl/video/Zwiastun/Mordercza+opona+Zwiastun+nr+1+polski-24067",
    cinema_id = 2
    )
f5 = Film(
    name="2012", 
    year = 2009,
    description="Jackson Curtis próbuje ocalić najbliższych przed niszczącymi Ziemię kataklizmami.",
    vote_count = 0,
    posterurl = "https://m.media-amazon.com/images/M/MV5BMTY0MjEyODQzMF5BMl5BanBnXkFtZTcwMTczMjQ4Mg@@._V1_FMjpg_UX1000_.jpg",
    movieurl = "https://www.youtube.com/watch?v=ce0N3TEcFw0&ab_channel=SonyPicturesEntertainment",
    cinema_id = 2
    )
f6 = Film(
    name="PITBULL. NIEBEZPIECZNE KOBIETY", 
    year = 2016,
    description="Młode policjantki, Zuza i Jadźka dołączają do Pitbulla. Dziewczyny oprócz zmagań w życiu prywatnym muszą stawić czoła przestępczemu światu.",
    vote_count = 0,
    posterurl = "https://m.media-amazon.com/images/M/MV5BMTY0MjEyODQzMF5BMl5BanBnXkFtZTcwMTczMjQ4Mg@@._V1_FMjpg_UX1000_.jpg",
    movieurl = "https://www.youtube.com/watch?v=xZyiL8NgENo&ab_channel=KinoSwiatPL",
    cinema_id = 2
    )
f7 = Film(
    name="PITBULL. NIEBEZPIECZNE KOBIETY", 
    year = 2016,
    description="Młode policjantki, Zuza i Jadźka dołączają do Pitbulla. Dziewczyny oprócz zmagań w życiu prywatnym muszą stawić czoła przestępczemu światu.",
    vote_count = 0,
    posterurl = "https://m.media-amazon.com/images/M/MV5BMTY0MjEyODQzMF5BMl5BanBnXkFtZTcwMTczMjQ4Mg@@._V1_FMjpg_UX1000_.jpg",
    movieurl = "https://www.youtube.com/watch?v=xZyiL8NgENo&ab_channel=KinoSwiatPL",
    cinema_id = 3
    )
f8 = Film(
    name="Eragon", 
    year = 2006,
    description="Eragon – młody, wiejski chłopak znajduje niebieski kamień i przynosi go do domu. Ale zanim udaje mu się sprzedać go handlarzowi, z kamienia wykluwa się szafirowy smok, Saphira. Smoka próbuje ukraść zły Urgals, który brutalnie morduje wuja Eragona. Chłopcu i smoczycy w ostatniej chwili udaje się uciec. Od tej chwili Eragon poprzysięga zemstę mordercy wuja i wyrusza na wyprawę, by uratować świat i stać się ostatnim legendarnym Jeźdźcem Smoków.",
    vote_count = 0,
    posterurl = "https://fwcdn.pl/fpo/60/74/196074/7537948.3.jpg",
    movieurl = "https://www.filmweb.pl/video/Zwiastun/Eragon+Zwiastun+nr+1-17962",
    cinema_id = 3
    )
f9 = Film(
    name="Król Lew", 
    year = 2019,
    description="W wyniku podstępu Skazy prawowity władca afrykańskiej sawanny, Simba, zostaje wygnany. Razem z dwójką przyjaciół zamierza odzyskać tron.",
    vote_count = 0,
    posterurl = "https://m.media-amazon.com/images/I/61sJaBqGxZL._AC_SL1184_.jpg",
    movieurl = "https://www.youtube.com/watch?v=lFzVJEksoDY&ab_channel=DisneyPlus",
    cinema_id = 3
    )
f10 = Film(
    name="Dzień Niepodległośc", 
    year = 2019,
    description="Przedstawiciele pozaziemskiej cywilizacji przypuszczają atak na największe metropolie.",
    vote_count = 0,
    posterurl = "https://cdn1.naekranie.pl/media/cache/amp/2014/11/p7254203.5.jpg",
    movieurl = "https://www.youtube.com/watch?v=qMSA4EaljHU&ab_channel=FilmPlanetPolska",
    cinema_id = 3
    )
c1.add_film(f1)
c1.add_film(f2)
c1.add_film(f3)
c2.add_film(f4)
c2.add_film(f5)
c2.add_film(f6)
c3.add_film(f7)
c3.add_film(f8)
c3.add_film(f9)
c3.add_film(f10)


