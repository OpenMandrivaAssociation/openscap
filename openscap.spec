Name:           openscap
Version:        0.5.7
Release:        %mkrel 1
Summary:        Set of open source libraries enabling integration of the SCAP line of standards
Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.open-scap.org/
Source0:        http://open-scap.org/download/%{name}-%{version}.tar.gz
Patch0:		openscap-0.5.7-literal.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  swig pcre-devel libxml2-devel
BuildRequires:	rpm-devel
BuildRequires:	libnl-devel
BuildRequires:	curl-devel
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig

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
%patch0 -p0 -b .literal

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/oscap-scan
%{_libdir}/*.so.*
%{_libdir}/%{name}

%files python
%defattr(-,root,root,-)
%{python_sitearch}/*

%files perl
%defattr(-,root,root,-)
%{perl_vendorarch}/*
%{perl_vendorlib}/*

%files devel
%defattr(-,root,root,-)
%doc docs/{html,latex,examples}/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
