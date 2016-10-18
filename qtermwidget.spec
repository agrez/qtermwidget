Name:		qtermwidget
Version:	0.7.0
Release:	1%{?dist}
License:	GPLv2+
Summary:	A terminal emulator widget for Qt 5
URL:		https://github.com/lxde/%{name}
Source0:	https://github.com/lxde/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:	pkgconfig(Qt5Gui)
Conflicts:      qtermwidget-qt5
Obsoletes:      qtermwidget-qt5


%description
QTermWidget is an open-source project originally based on KDE4 Konsole
application, but it took its own direction later.
The main goal of this project is to provide Unicode-enabled, embeddable
QT widget for using as a built-in console (or terminal emulation widget).


%package	devel
Summary:    qtermwidget - devel package
Requires:   %{name}%{?_isa} = %{version}-%{release}
Conflicts:  qtermwidget-qt5-devel
Obsoletes:  qtermwidget-qt5-devel


%description	devel
Development files for qtermwidget library.

%prep
%autosetup


%build
%{?cmake} -DUSE_QT5=ON -DBUILD_DESIGNER_PLUGIN=0
make %{?_smp_mflags}


%install
%make_install


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_libdir}/lib%{name}5.so.*
%{_datadir}/%{name}5/

%files	devel
%{_includedir}/%{name}5/
%{_libdir}/lib%{name}5.so
%{_libdir}/pkgconfig/%{name}5.pc
%{_datadir}/cmake/%{name}5/


%changelog
* Mon Oct 17 2016 Vaughan <devel at agrez.net> - 0.7.0-1
- New release
- Depreciate Qt4 build (build support for Qt <= 5.4 dropped upstream)
- Update Summary / Url
- Drop Patch0 (qt-virt-manager patch)
- Add needed Conflicts/Obsoletes
- Use %autosetup
- Update %license file

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

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
