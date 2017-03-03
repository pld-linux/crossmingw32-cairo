Summary:	Cairo - multi-platform 2D graphics library - cross MinGW32 version
Summary(pl.UTF-8):	Cairo - wieloplatformowa biblioteka graficzna 2D - skrośna wersja MinGW32
%define		realname   cairo
Name:		crossmingw32-%{realname}
Version:	1.14.8
Release:	2
License:	LGPL v2.1 or MPL v1.1
Group:		Development/Libraries
Source0:	https://www.cairographics.org/releases/%{realname}-%{version}.tar.xz
# Source0-md5:	4ef0db2eacb271c74f8a3fd87822aa98
Patch0:		cairo-link.patch
Patch1:		cairo-mingw32.patch
Patch2:		cairo-add-cairo-API-to-setup-Win32-surface-for-HDC.patch
URL:		https://www.cairographics.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	crossmingw32-fontconfig >= 2.2.95
BuildRequires:	crossmingw32-freetype >= 2.3.0
BuildRequires:	crossmingw32-glib2 >= 2.14
BuildRequires:	crossmingw32-libpng
BuildRequires:	crossmingw32-pixman >= 0.30.0
BuildRequires:	crossmingw32-zlib
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig >= 1:0.18
Requires:	crossmingw32-fontconfig >= 2.2.95
Requires:	crossmingw32-freetype >= 2.3.0
Requires:	crossmingw32-libpng
Requires:	crossmingw32-pixman >= 0.30.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_libdir			%{_prefix}/lib
%define		_pkgconfigdir		%{_prefix}/lib/pkgconfig
%define		_dlldir			/usr/share/wine/windows/system
%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++
%define		__pkgconfig_provides	%{nil}
%define		__pkgconfig_requires	%{nil}

%ifnarch %{ix86}
# arch-specific flags (like alpha's -mieee) are not valid for i386 gcc
%define		optflags	-O2
%endif
# -z options are invalid for mingw linker, most of -f options are Linux-specific
# note: although C++ code is not used, failing configure check disables DLL building
%define		filterout_ld	-Wl,-z,.*
%define		filterout_c	-f[-a-z0-9=]*
%define		filterout_cxx	-f[-a-z0-9=]*

%description
Cairo provides anti-aliased vector-based rendering for X. Paths
consist of line segments and cubic splines and can be rendered at any
width with various join and cap styles. All colors may be specified
with optional translucence (opacity/alpha) and combined using the
extended Porter/Duff compositing algebra as found in the X Render
Extension.

Cairo exports a stateful rendering API similar in spirit to the path
construction, text, and painting operators of PostScript, (with the
significant addition of translucence in the imaging model). When
complete, the API is intended to support the complete imaging model of
PDF 1.4.

This package contains the cross version for Win32.

%description -l pl.UTF-8
Cairo obsługuje oparty na wektorach rendering z antyaliasingiem dla X.
Ścieżki składają się z odcinków i splajnów kubicznych, a renderowane
mogą być z dowolną grubością i różnymi stylami połączeń i zakończeń.
Wszystkie kolory mogą być podane z opcjonalną półprzezroczystością
(podaną przez współczynnik nieprzezroczystości lub alpha) i łączone
przy użyciu rozszerzonego algorytmu składania Portera-Duffa, który
można znaleźć w rozszerzeniu X Render.

Cairo eksportuje stanowe API renderujące w duchu podobne do operatorów
konstruowania ścieżek, tekstu i rysowania z PostScriptu (ze znacznym
dodatkiem półprzezroczystości w modelu obrazu). Kiedy API zostanie
ukończone, ma obsługiwać pełny model obrazu z PDF w wersji 1.4.

Ten pakiet zawiera wersję skrośną dla Win32.

%package static
Summary:	Static Cairo library (cross MinGW32 version)
Summary(pl.UTF-8):	Statyczna biblioteka Cairo (wersja skrośna MinGW32)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static Cairo library (cross MinGW32 version).

%description static -l pl.UTF-8
Statyczna biblioteka Cairo (wersja skrośna MinGW32).

%package dll
Summary:	DLL Cairo library for Windows
Summary(pl.UTF-8):	Biblioteka DLL Cairo dla Windows
Group:		Applications/Emulators
Requires:	crossmingw32-fontconfig-dll >= 2.2.95
Requires:	crossmingw32-freetype-dll >= 2.3.0
Requires:	crossmingw32-libpng-dll
Requires:	crossmingw32-pixman-dll >= 0.30.0

%description dll
DLL Cairo library for Windows.

%description dll -l pl.UTF-8
Biblioteka DLL Cairo dla Windows.

%package gobject
Summary:	Cairo GObject functions library - cross MinGW32 version
Summary(pl.UTF-8):	Biblioteka funkcji Cairo GObject - wersja skrośna MinGW32 
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	crossmingw32-glib2 >= 2.14

%description gobject
Cairo GObject functions library - cross MinGW32 version.

%description gobject -l pl.UTF-8
Biblioteka funkcji Cairo GObject - wersja skrośna MinGW32.

%package gobject-static
Summary:	Static Cairo GObject library (cross MinGW32 version)
Summary(pl.UTF-8):	Statyczna biblioteka Cairo GObject (wersja skrośna MinGW32)
Group:		Development/Libraries
Requires:	%{name}-gobject = %{version}-%{release}

%description gobject-static
Static Cairo GObject library (cross MinGW32 version).

%description gobject-static -l pl.UTF-8
Statyczna biblioteka Cairo GObject (wersja skrośna MinGW32).

%package gobject-dll
Summary:	DLL Cairo GObject library for Windows
Summary(pl.UTF-8):	Biblioteka DLL Cairo GObject dla Windows
Group:		Applications/Emulators
Requires:	%{name}-dll = %{version}-%{release}
Requires:	crossmingw32-glib2-dll >= 2.14

%description gobject-dll
DLL Cairo GObject library for Windows.

%description gobject-dll -l pl.UTF-8
Biblioteka DLL Cairo GObject dla Windows.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
export PKG_CONFIG_LIBDIR=%{_prefix}/lib/pkgconfig
%{__libtoolize}
%{__aclocal} -I build
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	CPPFLAGS="%{rpmcppflags} -Dffs=__builtin_ffs" \
	lt_cv_deplibs_check_method=pass_all \
	--target=%{target} \
	--host=%{target} \
	--disable-gtk-doc \
	--disable-silent-rules \
	--disable-xlib \
	--disable-xlib-render \
	--enable-freetype \
	--enable-pdf \
	--enable-png \
	--enable-ps \
	--enable-tee \
	--enable-windows \
	--enable-xml

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_dlldir}
mv -f $RPM_BUILD_ROOT%{_prefix}/bin/*.dll $RPM_BUILD_ROOT%{_dlldir}

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{_dlldir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{_libdir}/*.a
%endif

rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains only notes, not LGPL/MPL texts
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/libcairo.dll.a
%{_libdir}/libcairo.la
%{_libdir}/libcairo-script-interpreter.dll.a
%{_libdir}/libcairo-script-interpreter.la
%{_includedir}/cairo
%exclude %{_includedir}/cairo/cairo-gobject.h
%{_pkgconfigdir}/cairo.pc
%{_pkgconfigdir}/cairo-fc.pc
%{_pkgconfigdir}/cairo-ft.pc
%{_pkgconfigdir}/cairo-pdf.pc
%{_pkgconfigdir}/cairo-png.pc
%{_pkgconfigdir}/cairo-ps.pc
%{_pkgconfigdir}/cairo-script.pc
%{_pkgconfigdir}/cairo-svg.pc
%{_pkgconfigdir}/cairo-tee.pc
%{_pkgconfigdir}/cairo-win32.pc
%{_pkgconfigdir}/cairo-win32-font.pc
%{_pkgconfigdir}/cairo-xml.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcairo.a
%{_libdir}/libcairo-script-interpreter.a

%files dll
%defattr(644,root,root,755)
%{_dlldir}/libcairo-2.dll
%{_dlldir}/libcairo-script-interpreter-2.dll

%files gobject
%defattr(644,root,root,755)
%{_libdir}/libcairo-gobject.dll.a
%{_libdir}/libcairo-gobject.la
%{_includedir}/cairo/cairo-gobject.h
%{_pkgconfigdir}/cairo-gobject.pc

%files gobject-static
%defattr(644,root,root,755)
%{_libdir}/libcairo-gobject.a

%files gobject-dll
%defattr(644,root,root,755)
%{_dlldir}/libcairo-gobject-2.dll
