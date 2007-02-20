#
# Conditional build:
%bcond_with	glitz		# build with glitz backend
#
Summary:	Cairo - multi-platform 2D graphics library - cross Mingw32 version
Summary(pl):	Cairo - wieloplatformowa biblioteka graficzna 2D - skro¶na wersja Mingw32
%define		_realname   cairo
Name:		crossmingw32-%{_realname}
Version:	1.2.6
Release:	1
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	http://cairographics.org/releases/%{_realname}-%{version}.tar.gz
# Source0-md5:	487b3d7515752fe57f780d0fd707b01a
Patch0:		%{_realname}-link.patch
URL:		http://cairographics.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	crossmingw32-fontconfig
BuildRequires:	crossmingw32-freetype >= 2.1.10
%{?with_glitz:BuildRequires:	crossmingw32-glitz >= 0.5.1}
BuildRequires:	crossmingw32-libpng
BuildRequires:	crossmingw32-pkgconfig
BuildRequires:	crossmingw32-zlib
BuildRequires:	libtool
Requires:	crossmingw32-freetype >= 2.1.10
%{?with_glitz:Requires:	glitz >= 0.5.1}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32
%define		arch			%{_prefix}/%{target}
%define		gccarch			%{_prefix}/lib/gcc-lib/%{target}
%define		gcclib			%{_prefix}/lib/gcc-lib/%{target}/%{version}

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_pkgconfigdir		%{_prefix}/lib/pkgconfig
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

Cairo relies on the Xc library for backend rendering. Xc provides an
abstract interface for rendering to multiple target types. As of this
writing, Xc allows Cairo to target X drawables as well as generic
image buffers. Future backends such as PostScript, PDF, and perhaps
OpenGL are currently being planned.

%description -l pl
Cairo obs³uguje oparty na wektorach rendering z antyaliasingiem dla X.
¦cie¿ki sk³adaj± siê z odcinków i splajnów kubicznych, a renderowane
mog± byæ z dowoln± grubo¶ci± i ró¿nymi stylami po³±czeñ i zakoñczeñ.
Wszystkie kolory mog± byæ podane z opcjonaln± pó³przezroczysto¶ci±
(podan± przez wspó³czynnik nieprzezroczysto¶ci lub alpha) i ³±czone
przy u¿yciu rozszerzonego algorytmu mieszania Portera-Duffa, który
mo¿na znale¼æ w rozszerzeniu X Render.

Cairo eksportuje stanowe API renderuj±ce w duchu podobne do operatorów
konstruowania ¶cie¿ek, tekstu i rysowania z PostScriptu (ze znacznym
dodatkiem pó³przezroczysto¶ci w modelu obrazu). Kiedy API zostanie
ukoñczone, ma obs³ugiwaæ pe³ny model obrazu z PDF w wersji 1.4.

Cairo do backendowego renderowania wykorzystuje bibliotekê Xc. Xc
dostarcza abstrakcyjny interfejs do renderowania na wiele rodzajów
wyj¶æ. Aktualnie Xc pozwala Cairo tworzyæ obiekty X, a tak¿e ogólne
bufory obrazu. W przysz³o¶ci planowane s± takie backendy jak
PostScript, PDF i byæ mo¿e OpenGL.

%prep
%setup -q -n %{_realname}-%{version}
%patch0 -p1

%build
export PKG_CONFIG_PATH=%{_prefix}/lib/pkgconfig
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	AR="%{target}-ar" \
	RANLIB="%{target}-ranlib" \
	--target=%{target} \
	--host=%{target_platform} \
	%{?with_glitz:--enable-glitz} \
	--enable-ps \
	--enable-pdf \
	--disable-xlib \
	--disable-xlib-render \
	--enable-windows \
	--enable-svg \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains only notes, not LGPL/MPL texts
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.a
%{_includedir}/*
%{_pkgconfigdir}/*.pc
