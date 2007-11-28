#
# Conditional build:
%bcond_with	glitz		# build with glitz backend
#
Summary:	Cairo - multi-platform 2D graphics library - cross Mingw32 version
Summary(pl.UTF-8):	Cairo - wieloplatformowa biblioteka graficzna 2D - skrośna wersja Mingw32
%define		realname   cairo
Name:		crossmingw32-%{realname}
Version:	1.4.12
Release:	1
License:	LGPL v2.1 or MPL 1.1
Group:		Development/Libraries
Source0:	http://cairographics.org/releases/%{realname}-%{version}.tar.gz
# Source0-md5:	8e50c2c0d56388e4ee94196c0c7a7904
URL:		http://cairographics.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	crossmingw32-fontconfig
BuildRequires:	crossmingw32-freetype >= 2.1.10
%{?with_glitz:BuildRequires:	crossmingw32-glitz >= 0.5.1}
BuildRequires:	crossmingw32-libpng
BuildRequires:	crossmingw32-zlib
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.15
Requires:	crossmingw32-fontconfig
Requires:	crossmingw32-freetype >= 2.1.10
%{?with_glitz:Requires:	crossmingw32-glitz >= 0.5.1}
Requires:	crossmingw32-libpng
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_pkgconfigdir		%{_prefix}/lib/pkgconfig
%define		_dlldir			/usr/share/wine/windows/system
%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

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
przy użyciu rozszerzonego algorytmu mieszania Portera-Duffa, który
można znaleźć w rozszerzeniu X Render.

Cairo eksportuje stanowe API renderujące w duchu podobne do operatorów
konstruowania ścieżek, tekstu i rysowania z PostScriptu (ze znacznym
dodatkiem półprzezroczystości w modelu obrazu). Kiedy API zostanie
ukończone, ma obsługiwać pełny model obrazu z PDF w wersji 1.4.

Ten pakiet zawiera wersję skrośną dla Win32.

%package static
Summary:	Static cairo library (cross mingw32 version)
Summary(pl.UTF-8):	Statyczna biblioteka cairo (wersja skrośna mingw32)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static cairo library (cross mingw32 version).

%description static -l pl.UTF-8
Statyczna biblioteka cairo (wersja skrośna mingw32).

%package dll
Summary:	DLL cairo library for Windows
Summary(pl.UTF-8):	Biblioteka DLL cairo dla Windows
Group:		Applications/Emulators
Requires:	crossmingw32-fontconfig-dll
Requires:	crossmingw32-freetype-dll >= 2.1.10
%{?with_glitz:Requires:	crossmingw32-glitz-dll >= 0.5.1}
Requires:	crossmingw32-libpng-dll

%description dll
DLL cairo library for Windows.

%description dll -l pl.UTF-8
Biblioteka DLL cairo dla Windows.

%prep
%setup -q -n %{realname}-%{version}

%build
export PKG_CONFIG_LIBDIR=%{_prefix}/lib/pkgconfig
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	lt_cv_deplibs_check_method=pass_all \
	--target=%{target} \
	--host=%{target} \
	--disable-gtk-doc \
	--disable-xlib \
	--disable-xlib-render \
	--enable-freetype \
	%{?with_glitz:--enable-glitz} \
	--enable-pdf \
	--enable-png \
	--enable-ps \
	--enable-svg \
	--enable-windows

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
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_libdir}/libcairo.dll.a
%{_libdir}/libcairo.la
%{_includedir}/cairo
%{_pkgconfigdir}/cairo.pc
%{_pkgconfigdir}/cairo-ft.pc
%{_pkgconfigdir}/cairo-pdf.pc
%{_pkgconfigdir}/cairo-png.pc
%{_pkgconfigdir}/cairo-ps.pc
%{_pkgconfigdir}/cairo-svg.pc
%{_pkgconfigdir}/cairo-win32.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcairo.a

%files dll
%defattr(644,root,root,755)
%{_dlldir}/libcairo-*.dll
