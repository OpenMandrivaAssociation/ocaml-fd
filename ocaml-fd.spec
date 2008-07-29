%define name	ocaml-fd
%define version	1.0.0
%define release	%mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Descriptor-passing functions for OCaml
Source: 	http://oss.digirati.com.br/ocaml-fd/ocaml-fd-%{version}.tar.bz2
URL:		http://oss.digirati.com.br/ocaml-fd
License:	LGPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:  findlib
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This OCaml library implements miscellaneous functions related to UNIX file
descriptors. Currently, send_fd, recv_fd and fexecve are implemented.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n ocaml-fd-%{version}

%build
make all
make allopt
make doc

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}/stublibs
install -d -m 755 %{buildroot}/%_defaultdocdir/%{name}/html
ocamlfind install fd META -destdir %{buildroot}/%{ocaml_sitelib} \
  fd.cmi fd.mli fd.cma fd.cmxa dllfd.so libfd.a fd.a
rm -f %{buildroot}/%{ocaml_sitelib}/stublibs/*.owner

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL LICENSE doc/html
%dir %{ocaml_sitelib}/fd
%{ocaml_sitelib}/fd/*.cmi

%files devel
%defattr(-,root,root)
%{ocaml_sitelib}/fd/*
%exclude %{ocaml_sitelib}/fd/*.cmi
%{ocaml_sitelib}/stublibs/dllfd.so

