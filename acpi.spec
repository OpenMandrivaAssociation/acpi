Summary:	Displays information on ACPI devices
Name:		acpi
Version:	1.8
Release:	1
License:	GPLv2+
Group:		System/Servers
Url:		https://sourceforge.net/projects/acpiclient/
Source0:	http://downloads.sourceforge.net/project/acpiclient/acpiclient/%{version}/%{name}-%{version}.tar.gz
Requires:	dmidecode
BuildSystem:	autotools

%description
Attempts to replicate the functionality of the 'old' apm command on
ACPI systems, including battery and thermal information.

%files
%doc AUTHORS README
%{_bindir}/*
%{_mandir}/man1/%{name}*
