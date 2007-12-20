%define name acpi
%define version 0.09
%define release %mkrel 1

Summary: Displays information on ACPI devices
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://grahame.angrygoats.net/source/acpi/%{name}-%{version}.tar.bz2
Source1: acpi.init
Patch1: acpi-0.09-on_ac_power.patch.bz2
Patch2: acpi-0.07-fix-README.patch.bz2
License: GPL
Group: System/Servers
BuildRoot: %{_tmppath}/%{name}-buildroot
Url: http://grahame.angrygoats.net/acpi.shtml
Requires(post):  rpm-helper
Requires(preun): rpm-helper
Requires: dmidecode

%description
Attempts to replicate the functionality of the 'old' apm command on
ACPI systems, including battery and thermal information.

%prep
%setup -q
%patch1 -p1 -b .on_ac_power
%patch2 -p1 -b .readme

%build
%configure2_5x
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
install -d -m755 $RPM_BUILD_ROOT/%{_mandir}/man1/
install -D -m755 %{SOURCE1} $RPM_BUILD_ROOT/%_initrddir/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_post_service %{name}

%preun
%_preun_service  %{name}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %_initrddir/%{name}
%{_bindir}/*
