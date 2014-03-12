Summary:	Voice Over IP phone using SIP for QT
Name:		twinkle
Version:	1.4.2
Release:	8
License:	GPLv2+
Group:		Communications
Url:		http://www.xs4all.nl/~mfnboer/twinkle/
Source0:	http://www.xs4all.nl/~mfnboer/twinkle/download/%{name}-%{version}.tar.gz
Patch0:		twinkle-1.4.2_libccrtp1.patch
BuildRequires:	desktop-file-utils
BuildRequires:	boost-devel
BuildRequires:	libilbc-devel
BuildRequires:	magic-devel
BuildRequires:	qt3-devel
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libccext2)
BuildRequires:	pkgconfig(libccrtp)
BuildRequires:	pkgconfig(libzrtpcpp)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(speex)

%description
Twinkle is a soft phone for your voice over IP communcations using the SIP
protocol. You can use it for direct IP phone to IP phone communication or in
a network using a SIP proxy to route your calls.

%files
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/*.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
export QTDIR=%{qt3dir}
export PATH=%{qt3dir}/bin:${PATH}
%configure2_5x \
	--with-zrtp \
	--without-kde
%make

%install
%makeinstall_std

#icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
install -m 0644 src/gui/images/twinkle48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -m 0644 src/gui/images/twinkle32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m 0644 src/gui/images/twinkle16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications

# correct icon syntax
sed -i -e 's,%{_datadir}/%{name}/twinkle48.png,%{name},g' %{name}.desktop
# run via soundwrapper
sed -i -e 's,Exec=%{name},Exec=soundwrapper %{_bindir}/%{name},g' %{name}.desktop
desktop-file-install --vendor="" \
	--dir %{buildroot}%{_datadir}/applications/ \
	--remove-category="KDE" \
	%{name}.desktop

