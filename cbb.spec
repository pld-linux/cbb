Summary:	An X11 based personal finance manager
Summary(pl):	Program do zarz±dzania finansami osobistymi
Name:		cbb
Version:	0.8.1
Epoch:		1
Release:	4
Source0:	http://cbb.sourceforge.net/down/%{name}-%{version}.tar.gz
License:	GPL
Group:		Applications
Group(de):	Applikationen
Group(pl):	Aplikacje
URL:		http://cbb.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	tcl >= 7.4, tk >= 4.0, gnuplot


%description
CBB is a personal financial management application written in Tcl/Tk
and Perl (it contains no compiled code) and utilizing a simple (tab
delimited) data file format. CBB provides a simple interface for users
to balance their checkbooks and to add their own reports, graphs, and
external modules without having to modify any of the CBB source.

%description -l pl
CBB jest mened¿erem finansów osobistych napisanym w Tcl/Tk i Perlu
(nie zawiera kompilownego kodu) i u¿ywa prostego formatu plików z
danymi. CBB ma prosty interfejs i daje siê ³atwo rozbudowywaæ bez
modyfikacji kodu.

%prep
%setup -q

%build
%configure
%{__make}

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
