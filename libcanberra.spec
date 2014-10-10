Summary:	Portable sound event library
Name:		libcanberra
Version:	0.30
Release:	4
License:	LGPL v2+
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/libcanberra/%{name}-%{version}.tar.xz
# Source0-md5:	34cb7e4430afaf6f447c4ebdb9b42072
URL:		http://0pointer.de/lennart/projects/libcanberra/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gstreamer-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	pkg-config
BuildRequires:	pulseaudio-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small and lightweight implementation of the XDG Sound Theme
Specification (http://0pointer.de/public/sound-theme-spec.html).

%package devel
Summary:	Header files for libcanberra library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcanberra library.

%package gtk
Summary:	GTK+ bindings for libcanberra library
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk
GTK+ bindings for libcanberra library.

%package gtk-devel
Summary:	Header files for libcanberra-gtk library
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk = %{version}-%{release}

%description gtk-devel
Header files for libcanberra-gtk library.

%package gtk3
Summary:	GTK+3 bindings for libcanberra library
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk3
GTK+3 bindings for libcanberra library.

%package gtk3-devel
Summary:	Header files for libcanberra-gtk3 library
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
# .h is needed by both libraries
Requires:	%{name}-gtk-devel = %{version}-%{release}
Requires:	%{name}-gtk3 = %{version}-%{release}

%description gtk3-devel
Header files for libcanberra-gtk library.

%package runtime
Summary:	libcanberra runtime
Group:		X11/Applications
Requires:	%{name}-gtk = %{version}-%{release}
Requires:	xdg-sound-theme

%description runtime
libcanberra runtime.

%package apidocs
Summary:	libcanberra API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libcanberra API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-oss		\
	--disable-silent-rules	\
	--disable-static	\
	--enable-alsa		\
	--enable-gstreamer	\
	--enable-null		\
	--enable-pulse		\
	--with-builtin=dso	\
	--with-html-dir=%{_gtkdocdir}
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -j1 \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/{*,gtk-?.0/modules/*}.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcanberra-%{version}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%post	gtk -p /usr/sbin/ldconfig
%postun	gtk -p /usr/sbin/ldconfig

%post	gtk3 -p /usr/sbin/ldconfig
%postun	gtk3 -p /usr/sbin/ldconfig

%post runtime

%preun runtime

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %ghost %{_libdir}/libcanberra.so.?
%attr(755,root,root) %{_libdir}/libcanberra.so.*.*.*
%dir %{_libdir}/libcanberra-%{version}
%attr(755,root,root) %{_libdir}/libcanberra-%{version}/libcanberra-alsa.so
%attr(755,root,root) %{_libdir}/libcanberra-%{version}/libcanberra-gstreamer.so
%attr(755,root,root) %{_libdir}/libcanberra-%{version}/libcanberra-multi.so
%attr(755,root,root) %{_libdir}/libcanberra-%{version}/libcanberra-null.so
%attr(755,root,root) %{_libdir}/libcanberra-%{version}/libcanberra-pulse.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcanberra.so
%{_includedir}/canberra.h
%{_pkgconfigdir}/libcanberra.pc
%{_datadir}/vala/vapi/libcanberra.vapi

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libcanberra-gtk.so.?
%attr(755,root,root) %{_libdir}/libcanberra-gtk.so.*.*.*

%files gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcanberra-gtk.so
%{_includedir}/canberra-gtk.h
%{_pkgconfigdir}/libcanberra-gtk.pc
%{_datadir}/vala/vapi/libcanberra-gtk.vapi

%files gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libcanberra-gtk3.so.?
%attr(755,root,root) %{_libdir}/libcanberra-gtk3.so.*.*.*

%files gtk3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcanberra-gtk3.so
%{_pkgconfigdir}/libcanberra-gtk3.pc

%files runtime
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/canberra-boot
%attr(755,root,root) %{_bindir}/canberra-gtk-play
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libcanberra-gtk-module.so
%attr(755,root,root) %{_libdir}/gtk-3.0/modules/libcanberra-gtk-module.so
%attr(755,root,root) %{_libdir}/gtk-3.0/modules/libcanberra-gtk3-module.so
%attr(755,root,root) %{_datadir}/gnome/shutdown/libcanberra-logout-sound.sh
%{_datadir}/gnome/autostart/libcanberra-login-sound.desktop
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/canberra-gtk-module.desktop
%{systemdunitdir}/canberra-system-bootup.service
%{systemdunitdir}/canberra-system-shutdown-reboot.service
%{systemdunitdir}/canberra-system-shutdown.service

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

