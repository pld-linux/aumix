# NOTE:		Please keep in sync with aumix-gtk.
Summary:	curses based audio mixer
Summary(de.UTF-8):	Audio-Mixer auf curses-Basis
Summary(es.UTF-8):	Mezclador de audio basado en curses
Summary(fr.UTF-8):	Mixer audio basé sur curses
Summary(tr.UTF-8):	Metin ekranlı ses karıştırıcı
Summary(pl.UTF-8):	Mikser audio bazujący na curses
Summary(pt_BR.UTF-8):	Mixador de áudio baseado em curses
Summary(ru.UTF-8):	Аудио микшер на базе библиотеки curses
Summary(uk.UTF-8):	Аудіо мікшер, базований на біблиотеці curses
Name:		aumix
Version:	2.8
Release:	6
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://www.jpj.net/~trevor/aumix/%{name}-%{version}.tar.bz2
# Source0-md5:	dc3fc7209752207c23e7c94ab886b340
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}.desktop
Source4:	%{name}.png
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-x%{name}.patch
Patch2:		%{name}-ac250.patch
URL:		http://www.jpj.net/~trevor/aumix.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel >= 5.0
Obsoletes:	aumix-gtk
Obsoletes:	aumix-X11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program provides a tty-based, interactive method of controlling a
sound card's mixer. It lets you adjust the input levels from the CD,
microphone, and onboard synthesizers as well as the output volume.

%description -l de.UTF-8
Dieses Programm bietet eine interaktive Methode auf tty-Basis zur
Steuerung eines Soundkarten-Mixers. Sie können damit die Eingangspegel
der CD, des Mikrophons und von Synthesizer-Karten sowie auch die
Ausgabelautstärke regeln.

%description -l es.UTF-8
Este programa nos ofrece un método interactivo basado en tty de
control de mezclas de tarjetas de sonido. Deja que se ajuste los
niveles de entrada del CD, micrófono, y sintetizadores, así como el
volumen de salida.

%description -l fr.UTF-8
Ce programme offre une méthode intaractive en mode texte pour
contrôler le mixer des cartes son. Il permet d'ajuster les niveaux
d'entrée du CD, du micro et des synthétiseurs de la carte, tout comme
le volume de sortie.

%description -l pl.UTF-8
Ten pakiet dostarcza bazującą na tty, interaktywną metodę
kontrolowania miksera karty dźwiękowej. aumix pozwala zmieniać poziom
sygnału nadchodzącego z CD, mikrofonu i syntetyzerów, a także poziom
sygnału wyjściowego.

%description -l pt_BR.UTF-8
Este programa oferece um método interativo baseado em tty de controle
de mixagem de placas de som. Ele deixa você ajustar os níveis de
entrada do CD, microfone, e sintetizadores assim como o volume de
saída.

%description -l tr.UTF-8
Bu program metin ekranda, etkileşimli olarak ses kartı mixer denetimi
yapmanızı saglar. Çıktı sesinin yanısıra, CD, mikrofon ve panel
üzerindeki birleştiriciden girdi seviyelerini ayarlamanıza olanak
verir.

%description -l ru.UTF-8
Эта программа - консольный, интерактивный регулятор уровней микшера
звуковой карты. Она позволяет изменять как входные уровни сигналов с
CD, микрофона, синтезаторов на звуковой плате, так и выходной уровень.

%description -l uk.UTF-8
Ця програма - консольний, інтерактивний регулятор рівней мікшеру
звукової картки. Вона дозволяє змінювати як вхідні рівні сигналів з
CD, мікрофону, синтезаторів на звуковій платі, так і вихідний рівень.

%package preserve-settings
Summary:	Saves/restores mixer settings on system shutdown/startup
Summary(pl.UTF-8):	Zapisuje/odtwarza ustawienia przy zamknięciu/starcie systemu
Group:		Applications/Sound
Requires:	rc-scripts >= 0.2.0
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Obsoletes:	aumix-OSS-preserve-settings
Obsoletes:	rhsound
Conflicts:	alsa-utils-init

%description preserve-settings
This package contains script, which will save settings of sound card's
mixer on system shutdown and restore them on system startup.

%description preserve-settings -l pl.UTF-8
Ten pakiet zawiera skrypt, który zapisuje ustawienia miksera karty
dźwiękowej przy zamknięciu systemu i odtwarza je po uruchomieniu
systemu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
#%%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}

CPPFLAGS="-I/usr/include/ncurses"
%configure \
	--without-gtk \
	--without-gtk1

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/aumix
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/aumix
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}
rm -f $RPM_BUILD_ROOT%{_datadir}/aumix/aumix.xpm

:> $RPM_BUILD_ROOT%{_sysconfdir}/aumixrc

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post preserve-settings
/sbin/chkconfig --add aumix
if [ ! -f /var/lock/subsys/aumix ]; then
	echo "Run \"/sbin/service aumix start\" to initialize saving/restoring"
	echo "sound card mixer's settings on system shutdown/startup, and then"
	echo "setup sound volume."
fi

%preun preserve-settings
if [ "$1" = "0" ]; then
	%service aumix stop
	/sbin/chkconfig --del aumix
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/aumixrc

%attr(755,root,root) %{_bindir}/aumix
%{_mandir}/man1/*
%{_datadir}/aumix
%{_pixmapsdir}/*.png
%{_desktopdir}/aumix.desktop

%files preserve-settings
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/aumix
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/aumix
