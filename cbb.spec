Summary:	An X11 based personal finance manager
Name:		cbb
Version:	0.8.1
Serial:		1
Release:	3mdk
Source0:	cbb-0.8.1.tar.gz
License:	GPL
Group:		Applications/Productivity
URL:		http://cbb.sourceforge.net/
BuildArch:	noarch
#BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	tcl >= 7.4, tk >= 4.0, gnuplot


%description
CBB is a personal financial management application written in Tcl/Tk
and Perl (it contains no compiled code) and utilizing a simple (tab
delimited) data file format. CBB provides a simple interface for users
to balance their checkbooks and to add their own reports, graphs, and
external modules without having to modify any of the CBB source.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Announce Bugs COPYING FAQ README THANKS Todo Version
%attr(755,root,root) %{_bindir}/cbb
%attr(755,root,root) %{_bindir}/dialog4duplicate
%{_libdir}/cbb
