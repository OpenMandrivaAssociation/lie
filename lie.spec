%define liedir	%{_datadir}/lie

Name:		lie
Version:	2.2.2
Release:	%mkrel 1
Group:		Sciences/Mathematics
Summary:	Interactive computations of a Lie group theoretic nature
# No license file, and apparently only available from sagemath.org
# as the documented homepage neither ftp server directory exist anymre
License:	Freeware
Source0:	http://www.sagemath.org/packages/optional/lie-2.2.2.p3.spkg
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	bison
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel

%description
LiE purpose is to enable mathematicians and physicists to obtain on-line
information as well as to interactively perform computations of a Lie group
theoretic nature. It focuses on the representation theory of complex semisimple
(reductive) Lie groups and algebras, and on the structure of their Weyl
groups and root systems. The basic objects of computation are vectors and
matrices with integer entries, and polynomials with integral coefficients.
These objects are used to represent weights, (sets of) roots, characters and
similar objects relating to Lie groups and algebras. LiE does not compute
directly with elements of the Lie groups and algebras themselves, but the
computations may be parametrised by the type of the Lie group or algebra for
which they should be performed.

%prep
%setup -q -n %{name}-%{version}.p3

%build
pushd src
    %make
popd

%install
pushd src
    for dir in progs gapfiles; do
	mkdir -p %{buildroot}/%{liedir}/$dir
	cp -fa $dir/* %{buildroot}/%{liedir}/$dir
    done

    cp -fa INFO* LEARN* %{buildroot}/%{liedir}
    cp -fa Lie.exe %{buildroot}/%{liedir}

    mkdir -p %{buildroot}%{_bindir}
    cat > %{buildroot}%{_bindir}/lie << EOF
#!/bin/sh

LD=%{liedir}
exec \$LD/Lie.exe initfile \$LD
EOF
    chmod +x %{buildroot}%{_bindir}/lie
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc src/manual/manual.dvi
%{_bindir}/lie
%dir %{liedir}
%{liedir}/*
