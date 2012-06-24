# NOTE:		Please keep in sync with aumix-gtk.
Summary:	curses based audio mixer
Summary(de):	Audio-Mixer auf curses-Basis
Summary(fr):	Mixer audio bas� sur curses
Summary(tr):	Metin ekranl� ses kar��t�r�c�
Summary(pl):	Mikser audio bazuj�cy na curses
Summary(ru):	����� ������ �� ���� ���������� curses
Summary(uk):	��Ħ� ͦ����, ��������� �� ¦������æ curses
Name:		aumix
Version:	2.7
Release:	2
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Source0:	http://www.jpj.net/~trevor/aumix/%{name}-%{version}.tar.gz
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	x%{name}.desktop
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-xaumix.patch
URL:		http://www.jpj.net/~trevor/aumix.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	gpm-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	aumix-gtk

%define		_xbindir	/usr/X11R6/bin
%define		_xdatadir	/usr/X11R6/share
%define		_xmandir	/usr/X11R6/man

%description
This program provides a tty-based, interactive method of controlling a
sound card's mixer. It lets you adjust the input levels from the CD,
microphone, and onboard synthesizers as well as the output volume.

%description -l de
Dieses Programm bietet eine interaktive Methode auf tty-Basis zur
Steuerung eines Soundkarten-Mixers. Sie k�nnen damit die Eingangspegel
der CD, des Mikrophons und von Synthesizer-Karten sowie auch die
Ausgabelautst�rke regeln.

%description -l fr
Ce programme offre une m�thode intaractive en mode texte pour
contr�ler le mixer des cartes son. Il permet d'ajuster les niveaux
d'entr�e du CD, du micro et des synth�tiseurs de la carte, tout comme
le volume de sortie.

%description -l pl
Ten program przynosi bazuj�c� na tty, interaktywn� metod�
kontrolowania miksera karty d�wi�kowej. aumix pozwala zmienia� poziom
sygna�u nadchodz�cego z CD, mikrofonu i syntetyzer�w tak samo jak
poziom sygna�u wyj�ciowego.

%description -l tr
Bu program metin ekranda, etkile�imli olarak ses kart� mixer denetimi
yapman�z� saglar. ��kt� sesinin yan�s�ra, CD, mikrofon ve panel
�zerindeki birle�tiriciden girdi seviyelerini ayarlaman�za olanak
verir.

%description -l ru
��� ��������� - ����������, ������������� ��������� ������� �������
�������� �����. ��� ��������� �������� ��� ������� ������ �������� �
CD, ���������, ������������ �� �������� �����, ��� � �������� �������.

%description -l uk
�� �������� - ����������, ������������� ��������� Ҧ���� ͦ�����
������ϧ ������. ���� ������Ѥ �ͦ������ �� �Ȧ�Φ Ҧ�Φ �����̦� �
CD, ͦ�������, ���������Ҧ� �� �����צ� ���Ԧ, ��� � ��Ȧ���� Ҧ����.

%package OSS-preserve-settings
Summary:	Saves/restores mixer settings on system shutdown/startup
Summary(pl):	Zapisuje/odtwarza ustawienia przy zamkni�ciu/starcie systemu
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Requires:	%{name} = %{version}
Prereq:		rc-scripts >= 0.2.0
Obsoletes:	rhsound
Conflicts:	alsa-utils

%description OSS-preserve-settings
This package contains script, which will save settings of sound card's
mixer on system shutdown and restore them on system startup.

%description -l pl OSS-preserve-settings
Ten pakiet zawiera skrypt, kt�ry zapisuje ustawienia miksera karty
d�wi�kowej przy zamkni�ciu systemu i odtwarza je po uruchomieniu
systemu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
aclocal
autoconf
automake -a -c
gettextize --copy --force

CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure --without-gtk

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Multimedia,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT{%{_xbindir},%{_xmandir}/man1} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/xaumix $RPM_BUILD_ROOT%{_xbindir}
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/xaumix* $RPM_BUILD_ROOT%{_xmandir}/man1
mv -f $RPM_BUILD_ROOT%{_datadir}/aumix/*xpm $RPM_BUILD_ROOT%{_pixmapsdir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/aumix
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/aumix
install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

touch $RPM_BUILD_ROOT%{_sysconfdir}/aumixrc

gzip -9nf AUTHORS BUGS ChangeLog NEWS README TODO

%find_lang %{name}

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

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,BUGS,ChangeLog,NEWS,README,TODO}.gz
%config(noreplace,missingok) %verify(not size mtime md5) %{_sysconfdir}/aumixrc

%attr(755,root,root) %{_bindir}/aumix
%{_mandir}/man1/*
%{_datadir}/aumix

%attr(755,root,root) %{_xbindir}/xaumix
%{_xmandir}/man1/*
%{_pixmapsdir}/*.xpm
%{_applnkdir}/Multimedia/xaumix.desktop

%files OSS-preserve-settings
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/aumix
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/aumix
