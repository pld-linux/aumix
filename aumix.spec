# NOTE:		Please keep in sync with aumix-gtk.
Summary:	curses based audio mixer
Summary(de):	Audio-Mixer auf curses-Basis
Summary(es):	Mezclador de audio basado en curses
Summary(fr):	Mixer audio basé sur curses
Summary(tr):	Metin ekranlý ses karýþtýrýcý
Summary(pl):	Mikser audio bazuj±cy na curses
Summary(pt_BR):	Mixador de áudio baseado em curses
Summary(ru):	áÕÄÉÏ ÍÉËÛÅÒ ÎÁ ÂÁÚÅ ÂÉÂÌÉÏÔÅËÉ curses
Summary(uk):	áÕÄ¦Ï Í¦ËÛÅÒ, ÂÁÚÏ×ÁÎÉÊ ÎÁ Â¦ÂÌÉÏÔÅÃ¦ curses
Name:		aumix
Version:	2.7
Release:	15
License:	GPL
Group:		Applications/Sound
Source0:	http://www.jpj.net/~trevor/aumix/%{name}-%{version}.tar.gz
# Source0-md5: 84ecc331bf6d86d3ac925590fee83af7
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	aumix-gtk
Obsoletes:	aumix-X11

%description
This program provides a tty-based, interactive method of controlling a
sound card's mixer. It lets you adjust the input levels from the CD,
microphone, and onboard synthesizers as well as the output volume.

%description -l de
Dieses Programm bietet eine interaktive Methode auf tty-Basis zur
Steuerung eines Soundkarten-Mixers. Sie können damit die Eingangspegel
der CD, des Mikrophons und von Synthesizer-Karten sowie auch die
Ausgabelautstärke regeln.

%description -l es
Este programa nos ofrece un método interactivo basado en tty de
control de mezclas de tarjetas de sonido. Deja que se ajuste los
niveles de entrada del CD, micrófono, y sintetizadores, así como el
volumen de salida.

%description -l fr
Ce programme offre une méthode intaractive en mode texte pour
contrôler le mixer des cartes son. Il permet d'ajuster les niveaux
d'entrée du CD, du micro et des synthétiseurs de la carte, tout comme
le volume de sortie.

%description -l pl
Ten pakiet dostarcza bazuj±c± na tty, interaktywn± metodê
kontrolowania miksera karty d¼wiêkowej. aumix pozwala zmieniaæ poziom
sygna³u nadchodz±cego z CD, mikrofonu i syntetyzerów, a tak¿e poziom
sygna³u wyj¶ciowego.

%description -l pt_BR
Este programa oferece um método interativo baseado em tty de controle
de mixagem de placas de som. Ele deixa você ajustar os níveis de
entrada do CD, microfone, e sintetizadores assim como o volume de
saída.

%description -l tr
Bu program metin ekranda, etkileþimli olarak ses kartý mixer denetimi
yapmanýzý saglar. Çýktý sesinin yanýsýra, CD, mikrofon ve panel
üzerindeki birleþtiriciden girdi seviyelerini ayarlamanýza olanak
verir.

%description -l ru
üÔÁ ÐÒÏÇÒÁÍÍÁ - ËÏÎÓÏÌØÎÙÊ, ÉÎÔÅÒÁËÔÉ×ÎÙÊ ÒÅÇÕÌÑÔÏÒ ÕÒÏ×ÎÅÊ ÍÉËÛÅÒÁ
Ú×ÕËÏ×ÏÊ ËÁÒÔÙ. ïÎÁ ÐÏÚ×ÏÌÑÅÔ ÉÚÍÅÎÑÔØ ËÁË ×ÈÏÄÎÙÅ ÕÒÏ×ÎÉ ÓÉÇÎÁÌÏ× Ó
CD, ÍÉËÒÏÆÏÎÁ, ÓÉÎÔÅÚÁÔÏÒÏ× ÎÁ Ú×ÕËÏ×ÏÊ ÐÌÁÔÅ, ÔÁË É ×ÙÈÏÄÎÏÊ ÕÒÏ×ÅÎØ.

%description -l uk
ãÑ ÐÒÏÇÒÁÍÁ - ËÏÎÓÏÌØÎÉÊ, ¦ÎÔÅÒÁËÔÉ×ÎÉÊ ÒÅÇÕÌÑÔÏÒ Ò¦×ÎÅÊ Í¦ËÛÅÒÕ
Ú×ÕËÏ×Ï§ ËÁÒÔËÉ. ÷ÏÎÁ ÄÏÚ×ÏÌÑ¤ ÚÍ¦ÎÀ×ÁÔÉ ÑË ×È¦ÄÎ¦ Ò¦×Î¦ ÓÉÇÎÁÌ¦× Ú
CD, Í¦ËÒÏÆÏÎÕ, ÓÉÎÔÅÚÁÔÏÒ¦× ÎÁ Ú×ÕËÏ×¦Ê ÐÌÁÔ¦, ÔÁË ¦ ×ÉÈ¦ÄÎÉÊ Ò¦×ÅÎØ.

%package OSS-preserve-settings
Summary:	Saves/restores mixer settings on system shutdown/startup
Summary(pl):	Zapisuje/odtwarza ustawienia przy zamkniêciu/starcie systemu
Group:		Applications/Sound
Requires:	%{name} = %{version}
PreReq:		rc-scripts >= 0.2.0
Requires(post,preun):	/sbin/chkconfig
Obsoletes:	rhsound
Conflicts:	alsa-utils

%description OSS-preserve-settings
This package contains script, which will save settings of sound card's
mixer on system shutdown and restore them on system startup.

%description OSS-preserve-settings -l pl
Ten pakiet zawiera skrypt, który zapisuje ustawienia miksera karty
d¼wiêkowej przy zamkniêciu systemu i odtwarza je po uruchomieniu
systemu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
#rm -f missing acinclude.m4
rm -f missing
#%%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}

CPPFLAGS="-I/usr/include/ncurses"
%configure \
	--without-gtk

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

%post OSS-preserve-settings
/sbin/chkconfig --add aumix
if [ ! -f /var/lock/subsys/aumix ]; then
	echo "Run \"/etc/rc.d/init.d/aumix start\" to initialize saving/restoring"
	echo "sound card mixer's settings on system shutdown/startup, and then"
	echo "setup sound volume."
fi

%preun OSS-preserve-settings
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/aumix ]; then
		/etc/rc.d/init.d/aumix stop
	fi
	/sbin/chkconfig --del aumix
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%config(noreplace,missingok) %verify(not size mtime md5) %{_sysconfdir}/aumixrc

%attr(755,root,root) %{_bindir}/aumix
%{_mandir}/man1/*
%{_datadir}/aumix
%{_pixmapsdir}/*.png
%{_desktopdir}/aumix.desktop

%files OSS-preserve-settings
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/aumix
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/aumix
