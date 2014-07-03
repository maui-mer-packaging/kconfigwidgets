# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kf5-kconfigwidgets

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 3 addon for creating configuration dialogs
Version:    5.0.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kf5-kconfigwidgets.yaml
Source101:  kf5-kconfigwidgets-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  kf5-kauth-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kcodecs-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfig-gui
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kguiaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  gettext-devel

%description
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kf5-kauth-devel
Requires:   kf5-kcoreaddons-devel
Requires:   kf5-kcodecs-devel
Requires:   kf5-kconfig-devel
Requires:   kf5-kconfig-gui
Requires:   kf5-kdoctools-devel
Requires:   kf5-kguiaddons-devel
Requires:   kf5-ki18n-devel
Requires:   kf5-kwidgetsaddons-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications |
that use %{name}.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc COPYING COPYING.LIB README.md
%{_kf5_libdir}/libKF5ConfigWidgets.so.*
%{_kf5_bindir}/preparetips5
%{_kf5_datadir}/kf5/kconfigwidgets
%{_kf5_mandir}/man1/*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/kconfigwidgets_version.h
%{_kf5_includedir}/KConfigWidgets
%{_kf5_libdir}/libKF5ConfigWidgets.so
%{_kf5_libdir}/cmake/KF5ConfigWidgets
%{_datadir}/qt5/mkspecs/modules/qt_KConfigWidgets.pri
# >> files devel
# << files devel
