Summary:	curses based audio mixer
Summary(pl):	mikser audio bazuj±cy na curses
Name:		aumix
Version:	1.18.2
Release:	1
Copyright:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Source:		http://www.jpj.net/~trevor/aumix/%{name}-%{version}.tar.gz
Patch:		aumix.patch
URL:		http://www.jpj.net/~trevor/aumix.html
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This program provides a tty based, interactive method of controlling a
sound cards mixer. It lets you adjust the input levels from the CD,
microphone, and on board synthesizers as well as the output volume.

%description -l pl
Ten program przynosi bazuj±c± na tty, interaktywn± metodê kontrolowania
miksera karty d¼wiêkowej. aumix pozwala zmieniaæ poziom sygna³u
nadchodz±cego z CD, mikrofonu i syntetyzerów tak samo jak poziom
sygna³u wyj¶ciowego.

%prep
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses" LDFLAGS="-s" \
./configure \
	--prefix=/usr

make

%install
rm -rf $RPM_BUILD_ROOT

make prefix="$RPM_BUILD_ROOT/usr" install

strip $RPM_BUILD_ROOT/usr/bin/*

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/* \
	AUTHORS BUGS ChangeLog NEWS README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,BUGS,ChangeLog,NEWS,README}.gz

%attr(755,root,root) /usr/bin/aumix
/usr/man/man1/*

%lang(de)    /usr/share/locale/de/LC_MESSAGES/aumix.mo
%lang(es)    /usr/share/locale/es/LC_MESSAGES/aumix.mo
%lang(pl)    /usr/share/locale/pl/LC_MESSAGES/aumix.mo
%lang(pt_BR) /usr/share/locale/pt_BR/LC_MESSAGES/aumix.mo
%lang(ru)    /usr/share/locale/ru/LC_MESSAGES/aumix.mo
%lang(ua)    /usr/share/locale/ua/LC_MESSAGES/aumix.mo

%changelog
* Mon Apr  5 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.17-2]
- gzipping documentation and man pages,
- changed BuildRoot to /tmp/%%{name}-%%{version}-root,
- removed man group from man pages,
- cosmetic changes for common l&f.

* Tue Feb 09 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [1.17-1d]
- new upstream release
- removed patches

* Mon Feb 01 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [1.15-1d]
- new upstream release
- now 755 mode instead 711 on binary
- added URL

* Wed Oct 07 1998 Arkadiusz Mi¶kiewicz <misiek@zsz2.starachowice.pl>
- corrected vendor
- few changes for PLD
- patch for slang (ncurses is bad thing ;)
- added %%lang macro
- added configure.in patch

* Thu Aug 06 1998 Arkadiusz Mi¶kiewicz <misiek@debian.eu.org>
- updated to 1.10
- added polish summary and description
- added small autoconf patch

* Tue Jul 28 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- updated to 1.9.4

* Wed Jul 22 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- updated to 1.9.3

* Tue Jul 21 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- new aumix version
