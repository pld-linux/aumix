Summary:	curses based audio mixer
Summary(fr):	Mixer audio basИ sur curses
Summary(tr):	Metin ekranlЩ ses karЩЧtЩrЩcЩ
Summary(pl):	mikser audio bazuj╠cy na curses
Summary(ru):	Аудио микшер на базе библиотеки curses
Summary(ua):	Ауд╕о м╕кшер, базований на б╕блиотец╕ curses
Name:		aumix
Version:	1.25
Release:	1
Copyright:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D╪wiЙk
URL:            http://www.jpj.net/~trevor/aumix.html
Source:		http://www.jpj.net/~trevor/aumix/%{name}-%{version}.tar.gz
BuildRequires:	ncurses-devel
BuildRequires:	gpm-devel
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

%description -l pl
Ten program przynosi bazuj╠c╠ na tty, interaktywn╠ metodЙ kontrolowania
miksera karty d╪wiЙkowej. aumix pozwala zmieniaФ poziom sygnaЁu
nadchodz╠cego z CD, mikrofonu i syntetyzerСw tak samo jak poziom
sygnaЁu wyj╤ciowego.

%description -l tr
Bu program metin ekranda, etkileЧimli olarak ses kartЩ mixer denetimi
yapmanЩzЩ saglar. гЩktЩ sesinin yanЩsЩra, CD, mikrofon ve panel Эzerindeki
birleЧtiriciden girdi seviyelerini ayarlamanЩza olanak verir.

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

%build
autoconf
gettextize --copy --force
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses"
LDFLAGS="-s"
export CFLAGS LDFLAGS
%configure 

make 

%install
rm -rf $RPM_BUILD_ROOT

make install-strip DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS BUGS ChangeLog NEWS README 

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,BUGS,ChangeLog,NEWS,README}.gz

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
