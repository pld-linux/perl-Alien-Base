#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Alien
%define		pnam	Base
Summary:	Alien::Base - Base classes for Alien:: modules
Name:		perl-Alien-Base
Version:	0.005
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Alien/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a9718c202966e7fafd23fbcf069e7c6b
URL:		http://search.cpan.org/dist/Alien-Base/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(File::chdir) >= 0.1005
BuildRequires:	perl-Capture-Tiny >= 0.17
BuildRequires:	perl-File-ShareDir
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Sort-Versions
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alien::Base comprises base classes to help in the construction of
Alien:: modules. Modules in the Alien namespace are used to locate and
install (if necessary) external libraries needed by other Perl
modules.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Alien/*.pm
%{perl_vendorlib}/Alien/Base
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
