Name: 	 	twinkle
Summary: 	Voice Over IP phone using SIP for QT
Version: 	1.4.2
Release: 	7
License:	GPLv2+
Group:		Communications
URL:		http://www.xs4all.nl/~mfnboer/twinkle/
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

%prep
%setup -q
%apply_patches

%build
#autoreconf -fi
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

%files 
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/*.desktop



%changelog
* Mon Jun 11 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.4.2-7
+ Revision: 804955
- rebuild for boost libs
- added p0 to fix build with newer libccrtp
- cleaned up spec

* Thu Mar 17 2011 Funda Wang <fwang@mandriva.org> 1.4.2-6
+ Revision: 645810
- rebuild for new boost

* Tue Aug 24 2010 Funda Wang <fwang@mandriva.org> 1.4.2-5mdv2011.0
+ Revision: 572688
- drop kde3 conditions

* Thu Feb 25 2010 Angelo Naselli <anaselli@mandriva.org> 1.4.2-4mdv2011.0
+ Revision: 510926
- Rebuilt against new commoncpp2 1.8.0

* Mon Feb 08 2010 Anssi Hannula <anssi@mandriva.org> 1.4.2-3mdv2010.1
+ Revision: 501882
- rebuild for new boost

* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 1.4.2-2mdv2010.1
+ Revision: 500336
- rebuild for new boost

* Sun Nov 22 2009 Jérôme Brenier <incubusss@mandriva.org> 1.4.2-1mdv2010.1
+ Revision: 469062
- new version 1.4.2

* Thu Mar 26 2009 Funda Wang <fwang@mandriva.org> 1.4.1-2mdv2009.1
+ Revision: 361301
- rebuild for new boost

* Sat Jan 31 2009 Funda Wang <fwang@mandriva.org> 1.4.1-1mdv2009.1
+ Revision: 335856
- new version 1.4.1

* Mon Jan 26 2009 Funda Wang <fwang@mandriva.org> 1.4-1mdv2009.1
+ Revision: 333583
- new version 1.4

* Mon Dec 22 2008 Funda Wang <fwang@mandriva.org> 1.3.2-2mdv2009.1
+ Revision: 317406
- rebuild for new boost

* Wed Dec 10 2008 Adam Williamson <awilliamson@mandriva.org> 1.3.2-1mdv2009.1
+ Revision: 312607
- menu entry: run via soundwrapper
- menu entry: drop KDE category, fix icon name
- fd.o icons
- %%buildroot not $RPM_BUILD_ROOT
- move out of KDE 3 area now as it's not a KDE app built this way
- buildrequires libilbc-devel
- new release 1.3.2
- drop unnecessary defines
- drop KDE support (we're dropping KDE 3, it doesn't support KDE 4)

* Sat Nov 08 2008 Funda Wang <fwang@mandriva.org> 1.3.1-3mdv2009.1
+ Revision: 301067
- disable requirement on private libs

* Sat Aug 23 2008 Funda Wang <fwang@mandriva.org> 1.3.1-2mdv2009.0
+ Revision: 275368
- add br
- New version 1.3.1

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 1.2-3mdv2009.0
+ Revision: 261725
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.2-2mdv2009.0
+ Revision: 255011
- rebuild

* Sun Jul 27 2008 Funda Wang <fwang@mandriva.org> 1.2-1mdv2009.0
+ Revision: 250558
- BR lrelease
- New version 1.2

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun Mar 02 2008 Austin Acton <austin@mandriva.org> 1.1-4mdv2008.1
+ Revision: 177716
- enable KDE support (bug 36973)

* Sun Jan 13 2008 Austin Acton <austin@mandriva.org> 1.1-3mdv2008.1
+ Revision: 150571
- qt3 bin path
- rebuild for boost

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 25 2007 Austin Acton <austin@mandriva.org> 1.1-2mdv2008.0
+ Revision: 55303
- buildrequires alsa (closes 32090)

* Mon Jul 23 2007 Funda Wang <fwang@mandriva.org> 1.1-1mdv2008.0
+ Revision: 54798
- Install desktop file
- New version

* Sun May 20 2007 Austin Acton <austin@mandriva.org> 1.0.1-1mdv2008.0
+ Revision: 28874
- new version

* Thu May 17 2007 Austin Acton <austin@mandriva.org> 1.0-3mdv2008.0
+ Revision: 27538
- fix menu

* Wed May 16 2007 Austin Acton <austin@mandriva.org> 1.0-2mdv2008.0
+ Revision: 27464
- fix wrong auto requires
- build with zrtp support


* Wed Mar 14 2007 Austin Acton <austin@mandriva.org> 1.0-1mdv2007.1
+ Revision: 143851
- fix lib64 build
- build QT-only
- new version; maybe add zrtp support later
- Import twinkle

* Mon Aug 14 2006 Austin Acton <austin@mandriva.org> 0.8.1-1mdv2007.0
- 0.8.1

* Sat Aug 12 2006 Austin Acton <austin@mandriva.org> 0.8-2mdv2007.0
- buildrequires boost-devel
- XDG menu

* Thu Jul 06 2006 Austin Acton <austin@mandriva.org> 0.8-1mdv2007.0
- New release 0.8

* Tue May 16 2006 Austin Acton <austin@mandriva.org> 0.7.1-1mdk
- initial package

