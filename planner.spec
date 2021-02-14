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


# based on https://src.fedoraproject.org/rpms/elementary-planne
