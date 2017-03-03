Summary: Create DOS/MS-compatible boot records
Name: ms-sys
Version: 2.5.3
Release: 2%{?dist}
License: GPL
Group: Applications/System
URL: http://ms-sys.sourceforge.net/

Source: https://downloads.sourceforge.net/project/ms-sys/ms-sys%20development/%{version}/ms-sys-%{version}.tar.gz
BuildRequires: bash
BuildRequires: gettext

%description
This program is used to create DOS/MS-compatible boot records. It is
able to do the same as Microsoft "fdisk /mbr" to a hard disk. It is
also able to do the same as DOS "sys" to a floppy or FAT32 partition
except that it does not copy any system files, only the boot record is
written.

%prep
%setup

%build
%{__make} debug \
    CC="${CC:-%{__cc}}" \
    EXTRA_CFLAGS="%{optflags} -fasm" \
    EXTRA_LDFLAGS="%{optflags}" \
    PREFIX="%{_prefix}" \
    SHELL="/bin/bash"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" PREFIX="%{_prefix}" MANDIR="%{_mandir}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%license COPYING
%doc CHANGELOG CONTRIBUTORS FAQ README TODO
%doc %{_mandir}/man1/ms-sys.1.gz
%doc %{_mandir}/*/man1/ms-sys.1.gz
%{_bindir}/ms-sys

%changelog
* Sun Apr 17 2016 Elia Devito <eliadevito@yahoo.it> - 2.5.3-2
- added new %files
- addedd %license

* Sun Apr 17 2016 Elia Devito <eliadevito@yahoo.it> - 2.5.3-1
- Updated to release 2.5.3

* Thu Oct 01 2015 Elia Devito <eliadevito@yahoo.it> - 2.4.1-1
- Updated to release 2.4.1

* Sun Jun 01 2014 Dag Wieers <dag@wieers.com> - 2.4.0-1
- Updated to release 2.4.0.

* Sun Apr 08 2012 Dag Wieers <dag@wieers.com> - 2.3.0-1
- Updated to release 2.3.0.

* Wed Jan 26 2011 Dag Wieers <dag@wieers.com> - 2.2.1-1
- Updated to release 2.2.1.

* Fri May 14 2010 Dag Wieers <dag@wieers.com> - 2.2.0-1
- Updated to release 2.2.0.

* Sun Mar 21 2010 Dag Wieers <dag@wieers.com> - 2.1.5-1
- Updated to release 2.1.5.

* Thu Oct 22 2009 Dag Wieers <dag@wieers.com> - 2.1.4-1
- Updated to release 2.1.4.

* Mon Dec 31 2007 Dag Wieers <dag@wieers.com> - 2.1.3-1
- Updated to release 2.1.3.

* Sat Nov 26 2005 Dag Wieers <dag@wieers.com> - 2.1.2-1
- Updated to release 2.1.2.

* Thu Aug 04 2005 Dag Wieers <dag@wieers.com> - 2.1.1-1
- Updated to release 2.1.1.

* Sun Jun 06 2004 Dag Wieers <dag@wieers.com> - 2.0.0-1
- Updated to release 2.0.0.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Initial package. (using DAR)
