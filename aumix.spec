Summary:	curses based audio mixer
Summary(fr):	Mixer audio basИ sur curses.
Summary(tr):	Metin ekranlЩ ses karЩЧtЩrЩcЩ
Summary(pl):	mikser audio bazuj╠cy na curses
Summary(ru):	Аудио микшер на базе библиотеки curses
Summary(ua):	Ауд╕о м╕кшер, базований на б╕блиотец╕ curses
Name:		aumix
Version:	1.18.4
Release:	1
Copyright:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D╪wiЙk
URL:            http://www.jpj.net/~trevor/aumix.html
Source:		http://www.jpj.net/~trevor/aumix/%{name}-%{version}.tar.gz
Patch0:		aumix.patch
BuildPrereq:	ncurses-devel
BuildPrereq:	gpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This program provides a tty-based, interactive method of controlling a 
sound card's mixer. It lets you adjust the input levels from the CD,
microphone, and onboard synthesizers as well as the output volume.

%description -l de
Dieses Programm bietet eine interaktive Methode auf tty-Basis zur 
Steuerung eines Soundkarten-Mixers. Sie kЖnnen damit die 
Eingangspegel der CD, des Mikrophons und von Synthesizer-Karten 
sowie auch die AusgabelautstДrke regeln. 

%description -l fr
Ce programme offre une mИthode intaractive en mode texte pour contrТler
le mixer des cartes son. Il permet d'ajuster les niveaux d'entrИe du CD,
du micro et des synthИtiseurs de la carte, tout comme le volume de sortie.

%description -l tr
Bu program metin ekranda, etkileЧimli olarak ses kartЩ mixer denetimi
yapmanЩzЩ saglar. гЩktЩ sesinin yanЩsЩra, CD, mikrofon ve panel Эzerindeki
birleЧtiriciden girdi seviyelerini ayarlamanЩza olanak verir.

%description -l pl
Ten program przynosi bazuj╠c╠ na tty, interaktywn╠ metodЙ kontrolowania
miksera karty d╪wiЙkowej. aumix pozwala zmieniaФ poziom sygnaЁu
nadchodz╠cego z CD, mikrofonu i syntetyzerСw tak samo jak poziom
sygnaЁu wyj╤ciowego.

%description -l ru
Эта программа - консольный, интерактивный регулятор уровней микшера
звуковой карты. Она позволяет изменять как входные уровни сигналов с
CD, микрофона, синтезаторов на звуковой плате, так и выходной уровень.

%description -l ua
Ця програма - консольний, ╕нтерактивний регулятор р╕вней м╕кшеру
звуково╖ картки. Вона дозволя╓ зм╕нювати як вх╕дн╕ р╕вн╕ сигнал╕в з
CD, м╕крофону, синтезатор╕в на звуков╕й плат╕, так ╕ вих╕дний р╕вень.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS -I%{_includedir}/ncurses" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=%{_prefix}

make

%install
rm -rf $RPM_BUILD_ROOT

make prefix="$RPM_BUILD_ROOT/usr" install

strip $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS BUGS ChangeLog NEWS README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,BUGS,ChangeLog,NEWS,README}.gz

%lang(de)    %{_datadir}/locale/de/LC_MESSAGES/aumix.mo
%lang(es)    %{_datadir}/locale/es/LC_MESSAGES/aumix.mo
%lang(pl)    %{_datadir}/locale/pl/LC_MESSAGES/aumix.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/aumix.mo
%lang(ru)    %{_datadir}/locale/ru/LC_MESSAGES/aumix.mo
%lang(ua)    %{_datadir}/locale/ua/LC_MESSAGES/aumix.mo

%attr(755,root,root) %{_bindir}/aumix
%{_mandir}/man1/*

%changelog
* Wed May  5 1999 Tomasz KЁoczko <kloczek@rudy.mif.pg.gda.pl>
  [1.18.3-1]
- translations from distributed in tar ball spec,
- spec rewritted by Arkadiusz Mi╤kiewicz <misiek@misiek.eu.org> and 
  Piotr CzerwiЯski <pius@pld.org.pl>.
