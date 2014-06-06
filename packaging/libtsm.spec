Name:           libtsm
Version:        3.0
Release:        0
Summary:        State machine for terminal emulators
License:        MIT
Group:          Graphics & UI Framework/Wayland Window System
Url:            http://www.freedesktop.org/wiki/Software/libtsm

#Git-Clone:	git://people.freedesktop.org/~dvdhrm/libtsm
#Git-Web:	http://cgit.freedesktop.org/~dvdhrm/libtsm
Source0:         %name-%version.tar.xz
Source1001:     libtsm.manifest
BuildRequires:	autoconf >= 2.64, automake >= 1.11
BuildRequires:  expat-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool >= 2.2
BuildRequires:  libvpx-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(xkbcommon) >= 0.3.0

%description
TSM-Terminal Emulator State Machine
TSM is a state machine for DEC VT100-VT520 compatible terminal
emulators. It tries to support all common standards while keeping
compatibility to existing emulators like xterm, gnome-terminal,
konsole,..
TSM itself does not provide any rendering nor window management.
It is a simple plain state machine without any external dependencies.
It can be used to implement terminal emulators, but also to implement
other applications that need to interpret terminal escape sequences.

%package devel
Summary: Development files for package %{name}
Group:   Graphics & UI Framework/Development
Requires: libtsm

%description devel
This package provides header files and other developer releated files
for package %{name}.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen 
make 

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%_libdir/%{name}.so*

%files devel
%manifest %{name}.manifest
%_includedir/%{name}.h
%_libdir/pkgconfig/%{name}.pc

%changelog
