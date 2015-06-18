%if 0%{?rhel} == 6
%define cmake_pkg cmake28
%else
%define cmake_pkg cmake
%endif

Name:		qtermwidget
Version:	0.6.0
Release:	3%{?dist}
License:	GPLv2+
Summary:	Qt4 terminal widget
URL:		https://github.com/qterminal/%{name}/
Source0:	https://github.com/qterminal/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
# https://github.com/qterminal/qtermwidget/commit/da6838df1ab5a919c32cde68017518ac7b8ba0e5
Patch0:		qtermwidget-0.6.0-qt-virt-manager.patch
BuildRequires:  %{cmake_pkg} >= 2.8
BuildRequires:	pkgconfig(QtGui)

%description
QTermWidget is an open-source project originally based on KDE4 Konsole
application, but it took its own direction later.
The main goal of this project is to provide Unicode-enabled, embeddable
QT widget for using as a built-in console (or terminal emulation widget)


%package	devel
Summary:	Qt4 terminal widget - devel package
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Development files for qtermwidget library.


%package	qt5
Summary:	Qt4 terminal widget
BuildRequires:	pkgconfig(Qt5Gui)

%description	qt5
QTermWidget is an open-source project originally based on KDE4 Konsole
application, but it took its own direction later.
The main goal of this project is to provide Unicode-enabled, embeddable
QT widget for using as a built-in console (or terminal emulation widget)


%package	qt5-devel
Summary:	Qt5 terminal widget - devel package
Requires:	%{name}-qt5%{?_isa} = %{version}-%{release}

%description	qt5-devel
Development files for qtermwidget-qt5 library.


%prep
%setup0 -q
%patch0 -p 0


%build
# qt4
mkdir build4
pushd build4
%{?cmake28}%{!?cmake28:%{?cmake}} ..
make %{?_smp_mflags}
popd
# qt5
mkdir build5
pushd build5
%{?cmake28}%{!?cmake28:%{?cmake}} -DUSE_QT5=ON -DBUILD_DESIGNER_PLUGIN=0 ..
make %{?_smp_mflags}
popd


%install
# qt4
pushd build4
%make_install
popd
# qt5
pushd build5
%make_install
popd


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%post	qt5
/sbin/ldconfig


%postun	qt5
/sbin/ldconfig


%files
%doc AUTHORS COPYING Changelog README
%{_libdir}/lib%{name}4.so.*
%{_libdir}/qt4/plugins/designer/lib%{name}4plugin.so
%{_datadir}/%{name}4/

%files	devel
%{_includedir}/%{name}4/
%{_libdir}/lib%{name}4.so
%{_libdir}/pkgconfig/%{name}4.pc
%{_datadir}/cmake/%{name}4/

%files	qt5
%doc AUTHORS COPYING Changelog README
%{_libdir}/lib%{name}5.so.*
%{_datadir}/%{name}5/

%files	qt5-devel
%{_includedir}/%{name}5/
%{_libdir}/lib%{name}5.so
%{_libdir}/pkgconfig/%{name}5.pc
%{_datadir}/cmake/%{name}5/


%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 TI_Eugene <ti.eugene@gmail.com> - 0.6.0-2
- qt-virt-manager compatible patch added

* Tue Nov 04 2014 TI_Eugene <ti.eugene@gmail.com> - 0.6.0-1
- Version bump
- qt5 packages added

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

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
