%define name	twinkle
%define version	1.0
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Voice Over IP phone using SIP for QT
Version: 	%{version}
Release: 	%{release}

Source:		http://www.xs4all.nl/~mfnboer/twinkle/download/%{name}-%{version}.tar.bz2
URL:		http://www.xs4all.nl/~mfnboer/twinkle/
License:	GPL
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libCommonC++-devel >= 1.3.0
BuildRequires:	ccrtp-devel >= 1.3.4
BuildRequires:	qt3-devel
BuildRequires:	libsndfile-devel
BuildRequires:	speex-devel
BuildRequires:	boost-devel

%description
Twinkle is a soft phone for your voice over IP communcations using the SIP
protocol. You can use it for direct IP phone to IP phone communication or in
a network using a SIP proxy to route your calls.

%prep
%setup -q

%build
%configure2_5x --with-qt-libraries=%{_prefix}/lib/qt3/%{_lib} --without-kde
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="Twinkle" longtitle="SIP phone for KDE" section="More Applications/Communications" xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{title}
Comment=%{summary}
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=KDE;QT;AudioVideo;Network;Telephony;X-MandrivaLinux-MoreApplications-Communications;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cp src/gui/images/twinkle48.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cp src/gui/images/twinkle32.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cp src/gui/images/twinkle16.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%name.desktop
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

