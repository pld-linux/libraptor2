Summary:	Raptor RDF Parser Toolkit
Summary(pl.UTF-8):	Raptor - zestaw narzędzi do analizy RDF
Name:		libraptor2
# the real name is raptor2, but it follows libraptor (named as such because raptor was already occupied)
%define	rname	raptor2
Version:	2.0.4
Release:	1
License:	LGPL v2.1+ or GPL v2+ or Apache v2.0+
Group:		Libraries
Source0:	http://download.librdf.org/source/%{rname}-%{version}.tar.gz
# Source0-md5:	0373efb8d85dc872bc7bb5b1c69299fb
URL:		http://librdf.org/raptor/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11
# WWW library can be one of: curl(default),xml,libfetch,libwww,none
BuildRequires:	curl-devel
BuildRequires:	gtk-doc-automake >= 1.3
BuildRequires:	libtool
BuildRequires:	yajl-devel
# XML library can be libxml or expat; grddl parser requires libxml2+libxslt anyway
BuildRequires:	libxml2-devel >= 2.6.8
BuildRequires:	libxslt-devel >= 1.0.18
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Raptor is the RDF Parser Toolkit for Redland written in C consisting
of two parsers for the RDF/XML and N-Triples syntaxes for RDF. Raptor
is designed to work efficiently when used with Redland but is entirely
separate.

%description -l pl.UTF-8
Raptor to zestaw narzędzi do analizy RDF dla Redland napisany w C,
składający się z dwóch analizatorów dla składni RDF/XML i N-Triplets
dla RDF. Raptor został zaprojektowany, by pracować wydajnie, jeśli
jest używany z Redland, ale jest całkowicie oddzielny.

%package devel
Summary:	libraptor2 library header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libraptor2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel
Requires:	libxml2-devel >= 2.6.8
Requires:	libxslt-devel >= 1.0.18
Requires:	yajl-devel

%description devel
libraptor2 library header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libraptor2.

%package static
Summary:	Static libraptor2 library
Summary(pl.UTF-8):	Statyczna biblioteka libraptor2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraptor2 library.

%description static -l pl.UTF-8
Statyczna biblioteka libraptor2.

%package apidocs
Summary:	libraptor2 API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libraptor2
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	libraptor-apidocs < 2.0.0

%description apidocs
libraptor2 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libraptor2.

%package rapper
Summary:	Raptor RDF parser test program
Summary(pl.UTF-8):	Testowy program parsera Raptor RDF
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libraptor-rapper < 2.0.0
Obsoletes:	redland-rapper

%description rapper
Raptor RDF parser test program.

%description rapper -l pl.UTF-8
Testowy program parsera Raptor RDF.

%prep
%setup -q -n %{rname}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# avoid using parsedate from libinn, use curl_getdate instead
%configure \
	ac_cv_header_libinn_h=no \
	--enable-release \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE.txt NEWS NOTICE README RELEASE.html UPGRADING.html
%attr(755,root,root) %{_libdir}/libraptor2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libraptor2.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libraptor2.so
%{_libdir}/libraptor2.la
%{_includedir}/raptor2
%{_pkgconfigdir}/raptor2.pc
%{_mandir}/man3/libraptor2.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libraptor2.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/raptor

%files rapper
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rapper
%{_mandir}/man1/rapper.1*
