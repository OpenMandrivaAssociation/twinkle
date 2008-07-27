# build with KDE address book support?
%define kde	1

%define name	twinkle
%define version	1.2
%define release %mkrel 1

#define _requires_exceptions libresolv.so.2

Name: 	 	%{name}
Summary: 	Voice Over IP phone using SIP for QT
Version: 	%{version}
Release: 	%{release}

Source:		http://www.xs4all.nl/~mfnboer/twinkle/download/%{name}-%{version}.tar.gz
URL:		http://www.xs4all.nl/~mfnboer/twinkle/
License:	GPL
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libCommonC++-devel >= 1.3.0
BuildRequires:	ccrtp-devel >= 1.3.4
BuildRequires:	qt3-devel
BuildRequires:	qt4-linguist
BuildRequires:	libsndfile-devel
BuildRequires:	speex-devel
BuildRequires:	boost-devel
BuildRequires:	libzrtpcpp-devel
BuildRequires:	desktop-file-utils
BuildRequires:	alsa-lib-devel
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
%if %kde
%configure_kde3 --with-zrtp --with-kde
%else
%configure_kde3 --with-zrtp --without-kde
%endif
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cp src/gui/images/twinkle48.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cp src/gui/images/twinkle32.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cp src/gui/images/twinkle16.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

mkdir -p %{buildroot}%{_kde3_datadir}/applications
desktop-file-install --vendor="" \
	--dir %{buildroot}%{_kde3_datadir}/applications/ \
	twinkle.desktop

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README THANKS
%{_kde3_bindir}/%name
%{_kde3_datadir}/%name
%{_kde3_datadir}/applications/*.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
