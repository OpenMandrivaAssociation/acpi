Summary:	Displays information on ACPI devices
Name:		acpi
Version:	1.7
Release:	3
License:	GPLv2+
Group:		System/Servers
Url:		http://sourceforge.net/projects/acpiclient/
Source0:	http://downloads.sourceforge.net/project/acpiclient/acpiclient/%{version}/%{name}-%{version}.tar.gz
Requires:	dmidecode

%description
Attempts to replicate the functionality of the 'old' apm command on
ACPI systems, including battery and thermal information.

%prep
%setup -q

%build
%configure2_5x
%make CFLAGS="%{optflags}"

%install
%makeinstall

%triggerpostun -- acpi < 0.09-4
rm -f /etc/rc.d/*/{K,S}*acpi

%files
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_mandir}/man1/%{name}*

