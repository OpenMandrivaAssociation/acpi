Summary:	Displays information on ACPI devices
Name:		acpi
Version:	1.7
Release:	8
License:	GPLv2+
Group:		System/Servers
Url:		http://sourceforge.net/projects/acpiclient/
Source0:	http://downloads.sourceforge.net/project/acpiclient/acpiclient/%{version}/%{name}-%{version}.tar.gz
Requires:	dmidecode

%description
Attempts to replicate the functionality of the 'old' apm command on
ACPI systems, including battery and thermal information.

%prep
%autosetup -p1

%build
%configure
%make_build CFLAGS="%{optflags}"

%install
%make_install

%files
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_mandir}/man1/%{name}*
