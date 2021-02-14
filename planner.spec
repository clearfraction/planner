%global appid com.github.alainm23.planner

Name:           planner
Version:        2.6.7
Release:        1
Summary:        Task manager with iTodoist support designed for GNU/Linux
License:        GPLv3+
URL:            https://github.com/alainm23/planner
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  appstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.40.3
BuildRequires:  libgee-lib libgee-dev
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  libpeas-dev
BuildRequires:  cmake json-glib-dev webkitgtk-dev
Requires:       hicolor-icon-theme

%description
Advanced planner app

%package dev
Summary: Devel files for %{name}
Requires: %{name} = %{version}-%{release}

%description dev
Devel files for %{name}.


%prep
%setup -n planner-%{version}

%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang %{appid}

# Remove trashy SVG icon dupes
rm -r   %{buildroot}%{_datadir}/icons/hicolor/*@2/      \
        %{buildroot}%{_datadir}/icons/hicolor/48x48/    \
        %{buildroot}%{_datadir}/icons/hicolor/64x64/    

%files -f %{appid}.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{appid}
%{_bindir}/%{appid}.quick-add
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_libdir}/%{appid}/
%{_libdir}/libplannercore.so.0*
%{_datadir}/metainfo/*.xml
 

%files dev
%{_datadir}/vala/vapi/*
%{_includedir}/*.h
%{_libdir}/libplannercore.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Fri Feb 12 2021 Kalev Lember <klember@redhat.com> - 1:2.6.7-3
- Rebuilt for evolution-data-server soname bump

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan  2 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1:2.6.7-1
- build(update): 2.6.7

* Sat Jan  2 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.6.6-1
- build(update): 2.6.6

* Tue Dec 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 6.2.3-1
- build(update): 6.2.3 | See: https://github.com/alainm23/planner/releases/tag/6.2.3

* Sat Dec 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.6.2-1
- build(update): 2.6.2

* Fri Dec 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.6.1-1
- build(update): 2.6.1

* Tue Oct 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5.7-1
- build(update): 2.5.7

* Thu Oct 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5.5-1
- build(update): 2.5.5

* Mon Oct 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5.4-1
- build(update): 2.5.4

* Wed Oct  7 21:03:44 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5.3-1
- build(update): 2.5.3

* Wed Oct  7 19:58:57 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5.2-1
- build(update): 2.5.2

* Sat Oct  3 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5.1-1
- Update to 2.5.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Kevin Fenzi <kevin@scrye.com> - 2.4.6-2
- Rebuild for new evolution-data-server

* Wed Jul 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4.6-1
- Update 2.4.6

* Mon Jun 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4.5-1
- Update 2.4.5

* Sun Jun 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4.4-1
- Update 2.4.4

* Sun Jun 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4.3-1
- Update 2.4.3

* Mon Jun 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4.2-1
- Update 2.4.2

* Thu Apr 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3.5-1
- Update 2.3.5

* Thu Apr 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3.4-1
- Update 2.3.4

* Tue Apr 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3.3-1
- Update 2.3.3

* Sun Apr 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3.2-1
- Update 2.3.2

* Wed Apr 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3.1-1
- Update 2.3.1

* Tue Apr 14 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.14-2
- Remove LTO

* Mon Mar 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.14-1
- Update to 2.2.14

* Fri Feb 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.1-2
- Initial package
