%global commit 8b3062f0248673b23b88afbd6f1d6ca581820c94
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		qtermwidget
Version:	0.4.0
Release:	7%{?dist}
License:	GPLv2+
Summary:	Qt4 terminal widget
URL:		https://github.com/qterminal/qtermwidget/
#Source0:	https://github.com/qterminal/qtermwidget/archive/%{version}.tar.gz
Source0:	https://github.com/qterminal/qtermwidget/tarball/%{commit}/qterminal-%{name}-%{version}-%{shortcommit}.tar.gz
BuildRequires:	cmake, pkgconfig(QtGui)

%description
QTermWidget is an open-source project originally based on KDE4 Konsole
application, but it took its own direction later.
The main goal of this project is to provide Unicode-enabled, embeddable
QT widget for using as a built-in console (or terminal emulation widget)

%package devel
Summary:	Qt4 terminal widget - devel package
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for qtermwidget library.

%prep
%setup0 -qn qterminal-%{name}-%{shortcommit}

%build
mkdir build
pushd build
%cmake ..
make %{?_smp_mflags}
popd

%install
pushd build
%make_install
popd

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING Changelog README
%{_libdir}/lib%{name}.so.*
%{_libdir}/qt4/plugins/designer/lib%{name}plugin.so
%{_datadir}/%{name}/

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-6
- Next git snapshot
- Source0 URL changed
- patch removed

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-4
- _isa added to -devel Requires.

* Thu Apr 18 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-3
- all cmake flags removed. "%cmake .." is the best.

* Thu Apr 18 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-2
- release added to -devel Requires
- dist tag added
- patch link to upstream issue added
- -devel description changed (environment > files)
- designer plugin moved to main package

* Tue Apr 16 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-1
- Initial Fedora packaging
