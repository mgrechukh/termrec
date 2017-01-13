# vim: set sw=4 ts=4 et nu:

Name:               termrec
Version:            0.17.1
%define soname      0
Release:            mgr1
Summary:            Records Videos of Terminal Output
Source:             https://github.com/mgrechukh/termrec/tarball/%{version}-%{release}
URL:                http://angband.pl/termrec.html
Group:              Productivity/Text/Utilities
License:            LGPL-3.0
BuildRoot:          %{_tmppath}/build-%{name}-%{version}
BuildRequires:      gcc make glibc-devel pkgconfig
BuildRequires:      autoconf automake libtool
Requires:           libtty%{soname} = %{version}-%{release}

%description
"Termrec" is a program for recording "videos" of terminal output.

%package -n libtty%{soname}
Summary:            Library for Terminal Handling
Group:              System/Libraries

%description -n libtty%{soname}
Library for handling terminals.

%package -n libtty-devel
Summary:            Library for Terminal Handling
Group:              Development/Libraries/C and C++
Requires:           libtty%{soname} = %{version}-%{release}

%description -n libtty-devel
Library for handling terminals.

%prep
%setup -q

%build
%configure
%__make %{?_smp_flags}

%install
%makeinstall

%__rm -f "%{buildroot}%{_libdir}"/*.la

%post   -n libtty%{soname} -p /sbin/ldconfig
%postun -n libtty%{soname} -p /sbin/ldconfig

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING.LIB ChangeLog README
%{_bindir}/proxyrec
%{_bindir}/termcat
%{_bindir}/termplay
%{_bindir}/termrec
%{_bindir}/termtime
%doc %{_mandir}/man1/proxyrec.1*
%doc %{_mandir}/man1/termcat.1*
%doc %{_mandir}/man1/termplay.1*
%doc %{_mandir}/man1/termrec.1*
%doc %{_mandir}/man1/termtime.1*

%files -n libtty-devel
%defattr(-,root,root)
%{_includedir}/ttyrec.h
%{_includedir}/vt100.h
%{_libdir}/libtty.so
%{_libdir}/libtty.a
%doc %{_mandir}/man3/*.3.*

%files -n libtty%{soname}
%defattr(-,root,root)
%{_libdir}/libtty.so.%{soname}
%{_libdir}/libtty.so.%{soname}.*

%changelog
* Fri Sep  2 2011 pascal.bleser@opensuse.org
- initial version (0.16)
