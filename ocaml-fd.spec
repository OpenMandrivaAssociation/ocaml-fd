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
BuildRequires:	ocaml-findlib
BuildRequires:	tetex-latex
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



%changelog
* Sat Aug 01 2009 Florent Monnier <blue_prawn@mandriva.org> 1.1.0-1mdv2010.0
+ Revision: 405305
- latex BuildRequires
- updated version

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-7mdv2010.0
+ Revision: 390083
- rebuild

* Mon Dec 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-6mdv2009.1
+ Revision: 320763
- move non-devel files into main package
- site-lib hierarchy doesn't exist anymore

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-5mdv2009.0
+ Revision: 254262
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0.0-3mdv2008.1
+ Revision: 136633
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-3mdv2008.0
+ Revision: 90013
- rebuild

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-2mdv2008.0
+ Revision: 77682
- drop macro definition, now in rpm-mandriva-setup
  ship .cmi file in non-devel subpackage

* Fri Aug 31 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1mdv2008.0
+ Revision: 77097
- import ocaml-fd


* Fri Aug 31 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1mdv2008.0
- contributed by Andre Nathan <andre@digirati.com.br>
