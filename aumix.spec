Summary:	curses based audio mixer
Summary(fr):	Mixer audio bas� sur curses
Summary(tr):	Metin ekranl� ses kar��t�r�c�
Summary(pl):	mikser audio bazuj�cy na curses
Summary(ru):	����� ������ �� ���� ���������� curses
Summary(ua):	��Ħ� ͦ����, ��������� �� ¦������æ curses
Name:		aumix
Version:	1.25
Release:	1
Copyright:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D�wi�k
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
Steuerung eines Soundkarten-Mixers. Sie k�nnen damit die 
Eingangspegel der CD, des Mikrophons und von Synthesizer-Karten 
sowie auch die Ausgabelautst�rke regeln. 

%description -l fr
Ce programme offre une m�thode intaractive en mode texte pour contr�ler
le mixer des cartes son. Il permet d'ajuster les niveaux d'entr�e du CD,
du micro et des synth�tiseurs de la carte, tout comme le volume de sortie.

%description -l pl
Ten program przynosi bazuj�c� na tty, interaktywn� metod� kontrolowania
miksera karty d�wi�kowej. aumix pozwala zmienia� poziom sygna�u
nadchodz�cego z CD, mikrofonu i syntetyzer�w tak samo jak poziom
sygna�u wyj�ciowego.

%description -l tr
Bu program metin ekranda, etkile�imli olarak ses kart� mixer denetimi
yapman�z� saglar. ��kt� sesinin yan�s�ra, CD, mikrofon ve panel �zerindeki
birle�tiriciden girdi seviyelerini ayarlaman�za olanak verir.

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
