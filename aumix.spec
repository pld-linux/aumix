Summary:	curses based audio mixer
Summary(fr):	Mixer audio bas� sur curses.
Summary(tr):	Metin ekranl� ses kar��t�r�c�
Summary(pl):	mikser audio bazuj�cy na curses
Summary(ru):	����� ������ �� ���� ���������� curses
Summary(ua):	��Ħ� ͦ����, ��������� �� ¦������æ curses
Name:		aumix
Version:	1.18.3
Release:	1
Copyright:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D�wi�k
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
Steuerung eines Soundkarten-Mixers. Sie k�nnen damit die 
Eingangspegel der CD, des Mikrophons und von Synthesizer-Karten 
sowie auch die Ausgabelautst�rke regeln. 

%description -l fr
Ce programme offre une m�thode intaractive en mode texte pour contr�ler
le mixer des cartes son. Il permet d'ajuster les niveaux d'entr�e du CD,
du micro et des synth�tiseurs de la carte, tout comme le volume de sortie.

%description -l tr
Bu program metin ekranda, etkile�imli olarak ses kart� mixer denetimi
yapman�z� saglar. ��kt� sesinin yan�s�ra, CD, mikrofon ve panel �zerindeki
birle�tiriciden girdi seviyelerini ayarlaman�za olanak verir.

%description -l pl
Ten program przynosi bazuj�c� na tty, interaktywn� metod� kontrolowania
miksera karty d�wi�kowej. aumix pozwala zmienia� poziom sygna�u
nadchodz�cego z CD, mikrofonu i syntetyzer�w tak samo jak poziom
sygna�u wyj�ciowego.

%description -l ru
��� ��������� - ����������, ������������� ��������� ������� �������
�������� �����. ��� ��������� �������� ��� ������� ������ �������� �
CD, ���������, ������������ �� �������� �����, ��� � �������� �������.

%description -l ua
�� �������� - ����������, ������������� ��������� Ҧ���� ͦ�����
������ϧ ������. ���� ������Ѥ �ͦ������ �� �Ȧ�Φ Ҧ�Φ �����̦� �
CD, ͦ�������, ���������Ҧ� �� �����צ� ���Ԧ, ��� � ��Ȧ���� Ҧ����.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr

make

%install
rm -rf $RPM_BUILD_ROOT

make prefix="$RPM_BUILD_ROOT/usr" install

strip $RPM_BUILD_ROOT/usr/bin/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS BUGS ChangeLog NEWS README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,BUGS,ChangeLog,NEWS,README}.gz

%lang(de)    /usr/share/locale/de/LC_MESSAGES/aumix.mo
%lang(es)    /usr/share/locale/es/LC_MESSAGES/aumix.mo
%lang(pl)    /usr/share/locale/pl/LC_MESSAGES/aumix.mo
%lang(pt_BR) /usr/share/locale/pt_BR/LC_MESSAGES/aumix.mo
%lang(ru)    /usr/share/locale/ru/LC_MESSAGES/aumix.mo
%lang(ua)    /usr/share/locale/ua/LC_MESSAGES/aumix.mo

%attr(755,root,root) /usr/bin/aumix
%{_mandir}/man1/*

%changelog
* Wed May  5 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.18.3-1]
- included de, fr, ru, ua translations from dis tar ball,
- recompiled on new rpm.

* Mon Apr  5 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [1.17-2]
- gzipping documentation and man pages,
- changed BuildRoot to /tmp/%%{name}-%%{version}-root,
- removed man group from man pages,
- cosmetic changes for common l&f.

* Tue Feb 09 1999 Arkadiusz Mi�kiewicz <misiek@misiek.eu.org>
  [1.17-1d]
- new upstream release
- removed patches

* Mon Feb 01 1999 Arkadiusz Mi�kiewicz <misiek@misiek.eu.org>
  [1.15-1d]
- new upstream release
- now 755 mode instead 711 on binary
- added URL

* Wed Oct 07 1998 Arkadiusz Mi�kiewicz <misiek@zsz2.starachowice.pl>
- corrected vendor
- few changes for PLD
- patch for slang (ncurses is bad thing ;)
- added %%lang macro
- added configure.in patch

* Thu Aug 06 1998 Arkadiusz Mi�kiewicz <misiek@debian.eu.org>
- updated to 1.10
- added polish summary and description
- added small autoconf patch

* Tue Jul 28 1998 Arkadiusz Mi�kiewicz <misiek@misiek.eu.org>
- updated to 1.9.4

* Wed Jul 22 1998 Arkadiusz Mi�kiewicz <misiek@misiek.eu.org>
- updated to 1.9.3

* Tue Jul 21 1998 Arkadiusz Mi�kiewicz <misiek@misiek.eu.org>
- new aumix version
