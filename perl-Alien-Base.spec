# NOTE: for versions > 0.043_01 see perl-Alien-Build.spec
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Alien
%define		pnam	Base
Summary:	Alien::Base - Base classes for Alien:: modules
Summary(pl.UTF-8):	Alien::Base - klasy bazowe dla modułów Alien::
Name:		perl-Alien-Base
Version:	0.005
Release:	2.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Alien/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a9718c202966e7fafd23fbcf069e7c6b
URL:		http://search.cpan.org/dist/Alien-Base/
BuildRequires:	perl-Module-Build >= 0.36
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Archive-Extract
BuildRequires:	perl-Capture-Tiny >= 0.17
BuildRequires:	perl-File-ShareDir
BuildRequires:	perl-File-chdir >= 0.1005
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Sort-Versions
BuildRequires:	perl-Test-Simple >= 0.94
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alien::Base comprises base classes to help in the construction of
Alien:: modules. Modules in the Alien namespace are used to locate and
install (if necessary) external libraries needed by other Perl
modules.

%description -l pl.UTF-8
Alien::Base obejmuje klasy bazowe pomagające w konstrukcji modułów
Alien::. Moduły w przestrzeni nazw Alien służą do lokalizacji i
instalowania (w razie potrzeby) zewnętrznych bibliotek wymaganych
przez inne moduły Perla.

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Alien/Base/Authoring.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Alien/Base/ModuleBuild/API.pod

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Alien/Base.pm
%dir %{perl_vendorlib}/Alien/Base
%{perl_vendorlib}/Alien/Base/ConfigData.pm
%{perl_vendorlib}/Alien/Base/ModuleBuild.pm
%{perl_vendorlib}/Alien/Base/PkgConfig.pm
%{perl_vendorlib}/Alien/Base/ModuleBuild
%{_mandir}/man3/Alien::Base.3pm*
%{_mandir}/man3/Alien::Base::Authoring.3pm*
%{_mandir}/man3/Alien::Base::ConfigData.3pm*
%{_mandir}/man3/Alien::Base::ModuleBuild.3pm*
%{_mandir}/man3/Alien::Base::ModuleBuild::API.3pm*
%{_examplesdir}/%{name}-%{version}
