Summary:	Displays information on ACPI devices
Name:		acpi
Version:	1.6
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


%changelog
* Wed Feb 08 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.6-1
+ Revision: 771788
- version update 1.6

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5-3
+ Revision: 662751
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5-2mdv2011.0
+ Revision: 603169
- rebuild

* Mon Apr 05 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.5-1mdv2010.1
+ Revision: 531538
- Update to 1.5

* Sun Feb 21 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4-1mdv2010.1
+ Revision: 508871
- update to new version 1.4
- drop both patches
- spec file clean

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.09-7mdv2010.0
+ Revision: 413021
- rebuild

* Mon Dec 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.09-6mdv2009.1
+ Revision: 321079
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.09-5mdv2009.0
+ Revision: 220327
- rebuild

* Fri Feb 22 2008 Olivier Blin <blino@mandriva.org> 0.09-4mdv2008.1
+ Revision: 173968
- remove old initscript symlinks on update

* Tue Feb 12 2008 Olivier Blin <blino@mandriva.org> 0.09-3mdv2008.1
+ Revision: 166310
- remove init script, modules are loaded by udev coldplug on the acpi bus
- bunzip patches

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.09-2mdv2008.1
+ Revision: 148413
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed May 23 2007 Christiaan Welvaart <spturtle@mandriva.org> 0.09-1mdv2008.0
+ Revision: 30352
- Import acpi

