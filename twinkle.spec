Summary:	Voice Over IP phone using SIP for QT
Name:		twinkle
Version:	1.11.0
Release:	1
License:	GPLv2+
Group:		Communications
Url:		https://twinkle.dolezel.info/
Source0:	https://github.com/LubosD/twinkle/archive/v%{version}.tar.gz
Patch0:		twinkle-1.11.0-qt6.patch
Patch1:		twinkle-1.11.0-ilbc-2.0.patch
BuildRequires:	desktop-file-utils
BuildRequires:	libilbc-devel
BuildRequires:	magic-devel
BuildRequires:	cmake
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	ninja
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(commoncpp)
BuildRequires:	pkgconfig(libccrtp)
BuildRequires:	pkgconfig(libzrtpcpp)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(speexdsp)
BuildRequires:	pkgconfig(ucommon)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	bison
BuildRequires:	flex
Requires:	qt6-qtdeclarative

BuildSystem:	cmake
BuildOption:	-DWITH_QT6:BOOL=ON
BuildOption:	-DWITH_SPEEX:BOOL=ON
BuildOption:	-DWITH_ZRTP:BOOL=ON
BuildOption:	-DWITH_ILBC:BOOL=ON
BuildOption:	-DWITH_DBUS:BOOL=ON

%description
Twinkle is a soft phone for your voice over IP communcations using the SIP
protocol. You can use it for direct IP phone to IP phone communication or in
a network using a SIP proxy to route your calls.

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-console
%{_bindir}/%{name}-uri-handler
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/twinkle.png
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1
