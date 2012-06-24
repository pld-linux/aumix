Summary:	curses based audio mixer
Summary(fr):	Mixer audio bas� sur curses.
Summary(tr):	Metin ekranl� ses kar��t�r�c�
Summary(pl):	mikser audio bazuj�cy na curses
Summary(ru):	����� ������ �� ���� ���������� curses
Summary(ua):	��Ħ� ͦ����, ��������� �� ¦������æ curses
Name:		aumix
Version:	1.19
Release:	1
Copyright:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D�wi�k
URL:            http://www.jpj.net/~trevor/aumix.html
Source:		http://www.jpj.net/~trevor/aumix/%{name}-%{version}.tar.gz
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

%build
<<<<<<< aumix.spec
autoconf
CFLAGS="$RPM_OPT_FLAGS -I%{_includedir}/ncurses" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix}
=======
gettextize --copy --force
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--mandir=%{_mandir}
>>>>>>> 1.14

make CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

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
* Tue Jun 1 1999 Piotr Czerwi�ski <pius@pld.org.pl> 
  [1.19-1]
- updated to 1.19,
- added using DESTDIR,
- fixed passing make flags.

* Wed May  5 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.18.3-1]
- translations from distributed in tar ball spec,
- spec rewritted by Arkadiusz Mi�kiewicz <misiek@misiek.eu.org> and 
  Piotr Czerwi�ski <pius@pld.org.pl>.
