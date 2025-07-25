Summary:	An X11 based personal finance manager
Summary(pl.UTF-8):	Program do zarządzania finansami osobistymi
Name:		cbb
Version:	0.8.1
Epoch:		1
Release:	5
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/cbb/%{name}-%{version}.tar.gz
# Source0-md5:	7a435ef954c5c2ba209d34ca5fa5c3a7
Source1:	%{name}.1
Source2:	dialog4duplicate.1
Patch0:		%{name}-DESTDIR.patch
URL:		http://home.gna.org/cbb/
BuildRequires:	automake
BuildRequires:	autoconf
Requires:	gnuplot
Requires:	tcl >= 7.4
Requires:	tk >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CBB is a personal financial management application written in Tcl/Tk
and Perl (it contains no compiled code) and utilizing a simple (tab
delimited) data file format. CBB provides a simple interface for users
to balance their checkbooks and to add their own reports, graphs, and
external modules without having to modify any of the CBB source.

%description -l pl.UTF-8
CBB jest programem zarządzającym finansami osobistymi napisanym w
Tcl/Tk i Perlu (nie zawiera kompilowanego kodu) i używa prostego
formatu plików z danymi. CBB ma prosty interfejs i daje się łatwo
rozbudowywać bez modyfikacji kodu.

%prep
%setup -q
%patch -P0 -p0

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=%{_prefix} \
	WISH=/usr/bin/wish \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Announce Bugs FAQ README THANKS Todo Version
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/cbb
%attr(755,root,root) %{_bindir}/dialog4duplicate
%dir %{_libdir}/cbb
%attr(755,root,root) %{_libdir}/cbb/*.pl
%attr(755,root,root) %{_libdir}/cbb/*.tcl
%{_libdir}/cbb/*.conf
%{_libdir}/cbb/*.cat
%{_libdir}/cbb/contrib
%{_libdir}/cbb/docs
%{_libdir}/cbb/graphs
%{_libdir}/cbb/images
%{_libdir}/cbb/languages
%{_libdir}/cbb/reports
