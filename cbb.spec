Summary: An X11 based personal finance manager. 
Name: cbb
Version: 0.8.1
Serial: 1
Release: 3mdk
Source0: cbb-0.8.1.tar.gz
Copyright: GPL
Group: Applications/Productivity
URL: http://cbb.sourceforge.net/
BuildArch: noarch
#BuildRoot: /var/tmp/cbb-build
Requires: tcl >= 7.4, tk >= 4.0, gnuplot


%description
CBB is a personal financial management application written in Tcl/Tk
and Perl (it contains no compiled code) and utilizing a simple (tab
delimited) data file format.  CBB provides a simple interface for
users to balance their checkbooks and to add their own reports,
graphs, and external modules without having to modify any of the CBB
source.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=/usr install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Announce Bugs COPYING FAQ README THANKS Todo Version
/usr/bin/cbb
/usr/bin/dialog4duplicate
/usr/lib/cbb

%changelog
* Thu Jan 06 2000 Florent Villard <warly@mandrakesoft.com> 0.81-2mdk
- add a Serial to solve version numbering change

* Thu Jan 06 2000 Florent Villard <warly@mandrakesoft.com> 0.81-1mdk
- mandrake adaptation

* Wed Jan 05 2000 Scott Lampert <fortunato@heavymetal.org>
- updated to 0.8.1

* Tue Jan 04 2000 Tim Powers <timp@redhat.com>
- reinstated using a buildroot, much safer than throwing files all over the
	system
- changed group to match valid Red Hat groups
- expanded requires
- quiet setup
- changed summary/description to match what Red Hat has shipped in the past
- using %configure instead of running autoconf and ./configure (%configure
	also defaults to --prefix=/usr)
- added %defattr(-,root,root) to the %files section

* Tue Jan 04 2000 Scott Lampert <fortunato@heavymetal.org>

- updated to 0.8.0
- resolves some Y2K issues

* Fri Dec 17 1999 Scott Lampert <fortunato@heavymetal.org>

- updated to 0.79

* Tue Oct 19 1999 Scott Lampert <fortunato@heavymetal.org>

- updated to 0.78

* Wed Jan 20 1999 Scott Lampert <fortunato@heavymetal.org>

- updated to 0.77

* Fri Jan 15 1999 Scott Lampert <fortunato@heavymetal.org>

- updated to 0.76

* Wed Jan 13 1999 Scott Lampert <fortunato@heavymetal.org>

- updated to 0.75

* Sat Aug 22 1998 Scott Lampert <fortunato@heavymetal.org>

- updated to 0.74
- Moved to /usr root instead of /usr/local as per typical RedHat packages
