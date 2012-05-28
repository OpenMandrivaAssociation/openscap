Name:           openscap
Version:        0.8.2
Release:        1
Summary:        Set of open source libraries enabling integration of the SCAP line of standards
Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.open-scap.org/
Source0:        http://open-scap.org/download/%{name}-%{version}.tar.gz
Patch0:		openscap-0.8.2-literal.patch
Patch1:		openscap-0.7.1-rpm5.patch
Patch2:		openscap-0.7.1-link.patch
BuildRequires:  swig
BuildRequires:	pcre-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	libgcrypt-devel
#BuildRequires:	rpm-devel
BuildRequires:	curl-devel

%description
OpenSCAP is a set of open source libraries providing an easier path 
for integration of the SCAP line of standards. SCAP is a line of standards 
managed by NIST with the goal of providing a standard language 
for the expression of Computer Network Defense related information.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        python
Summary:        Python bindings for %{name}
Group:          Development/Python
Requires:       %{name} = %{version}-%{release}
BuildRequires:  python-devel 

%description    python
The %{name}-python package contains the bindings so that %{name}
libraries can be used by python.

%package        perl
Summary:        Perl bindings for %{name}
Group:          Development/Perl
Requires:       %{name} = %{version}-%{release}
BuildRequires:  perl-devel

%description    perl
The %{name}-perl package contains the bindings so that %{name}
libraries can be used by perl.

%prep
%setup -q
%patch0 -p1 -b .literal
%patch2 -p0 -b .link

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{_sysconfdir}/bash_completion.d/oscap
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/%{name}
%{_mandir}/man8/*
%{_datadir}/%{name}

%files python
%{python_sitearch}/*

%files perl
%{perl_vendorarch}/*
%{perl_vendorlib}/*.pm

%files devel
%doc docs/{html,examples}/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
