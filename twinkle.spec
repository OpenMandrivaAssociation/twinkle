# build with KDE address book support? - disabled while it only
# supports KDE 3
%define kde	0

%define _requires_exceptions libresolv.so.2

Name: 	 	twinkle
Summary: 	Voice Over IP phone using SIP for QT
Version: 	1.4.2
Release: 	%{mkrel 4}
Source0:	http://www.xs4all.nl/~mfnboer/twinkle/download/%{name}-%{version}.tar.gz
URL:		http://www.xs4all.nl/~mfnboer/twinkle/
License:	GPLv2+
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libCommonC++-devel >= 1.3.0
BuildRequires:	ccrtp-devel >= 1.3.4
BuildRequires:	qt3-devel
BuildRequires:	libsndfile-devel
BuildRequires:	speex-devel
BuildRequires:	boost-devel
BuildRequires:	libzrtpcpp-devel
BuildRequires:	desktop-file-utils
BuildRequires:	alsa-lib-devel
BuildRequires:	file-devel
BuildRequires:	libilbc-devel
BuildRequires:	readline-devel
%if %kde
BuildRequires:	kdelibs-common
BuildRequires:	kdepim-devel
%endif

%description
Twinkle is a soft phone for your voice over IP communcations using the SIP
protocol. You can use it for direct IP phone to IP phone communication or in
a network using a SIP proxy to route your calls.

%prep
%setup -q

%build
export QTDIR=%{qt3dir}
export PATH=%{qt3dir}/bin:${PATH}
%if %kde
%configure_kde3 --with-zrtp --with-kde
%else
%configure2_5x --with-zrtp --without-kde
%endif
%make
										
%install
rm -rf %{buildroot}
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

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%update_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/*.desktop
