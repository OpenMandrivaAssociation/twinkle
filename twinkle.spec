Summary:	Voice Over IP phone using SIP for QT
Name:		twinkle
Version:	1.10.0
Release:	1
License:	GPLv2+
Group:		Communications
Url:		https://twinkle.dolezel.info/
Source0:	https://github.com/LubosD/twinkle/archive/v%{version}.tar.gz
Patch2:		twinkle-1.9.0-ilbc-2.0.patch
BuildRequires:	desktop-file-utils
BuildRequires:	boost-devel
BuildRequires:	libilbc-devel
BuildRequires:	magic-devel
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	ninja
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libccext2)
BuildRequires:	pkgconfig(libccrtp)
BuildRequires:	pkgconfig(libzrtpcpp)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(speexdsp)
BuildRequires:	pkgconfig(ucommon)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	%{_lib}qt5quick-devel

%description
Twinkle is a soft phone for your voice over IP communcations using the SIP
protocol. You can use it for direct IP phone to IP phone communication or in
a network using a SIP proxy to route your calls.

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-console
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/twinkle.png
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1
%cmake_kde5 \
	-DWITH_QT5:BOOL=ON \
	-DWITH_SPEEX:BOOL=ON \
	-DWITH_ZRTP:BOOL=ON \
	-DWITH_ILBC:BOOL=ON

%build
%ninja -C build

%install
%ninja_install -C build

#icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
install -m 0644 src/gui/images/twinkle48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -m 0644 src/gui/images/twinkle32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m 0644 src/gui/images/twinkle16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

# correct icon syntax
sed -i -e 's,%{_datadir}/%{name}/twinkle48.png,%{name},g' %{buildroot}%{_datadir}/applications/%{name}.desktop
