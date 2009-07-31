%define name	ocaml-fd
%define version	1.1.0
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Descriptor-passing functions for OCaml
Source: 	http://oss.digirati.com.br/ocaml-fd/ocaml-fd-%{version}.tar.gz
URL:		http://oss.digirati.com.br/ocaml-fd
License:	LGPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:  ocaml-findlib
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
make all opt
make doc

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/fd
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL LICENSE doc/fd
%dir %{_libdir}/ocaml/fd
%{_libdir}/ocaml/fd/*.cmi
%{_libdir}/ocaml/fd/*.cma
%{_libdir}/ocaml/fd/META
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.owner

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/fd/*.a
%{_libdir}/ocaml/fd/*.mli
%{_libdir}/ocaml/fd/*.cmxa

