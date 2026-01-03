#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTTP
%define		pnam	Entity-Parser
Summary:	HTTP::Entity::Parser - PSGI compliant HTTP Entity Parser
Name:		perl-HTTP-Entity-Parser
Version:	0.25
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/HTTP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	09663f9577975587e832e28ba5f5f8af
URL:		https://search.cpan.org/dist/HTTP-Entity-Parser/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-Module-Build-Tiny
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(HTTP::MultiPartParser)
BuildRequires:	perl(JSON::MaybeXS) >= 1.003007
BuildRequires:	perl(WWW::Form::UrlEncoded) >= 0.23
BuildRequires:	perl-HTTP-Message >= 6
BuildRequires:	perl-Hash-MultiValue
BuildRequires:	perl-Stream-Buffered
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTTP::Entity::Parser is a PSGI-compliant HTTP Entity parser. This
module also is compatible with HTTP::Body. Unlike HTTP::Body,
HTTP::Entity::Parser reads HTTP entities from PSGI's environment
$env->{'psgi.input'} and parses it. This module supports
application/x-www-form-urlencoded, multipart/form-data and
application/json.


%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--destdir=$RPM_BUILD_ROOT \
	--installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/HTTP/Entity
%{perl_vendorlib}/HTTP/Entity/*.pm
%{perl_vendorlib}/HTTP/Entity/Parser
%{_mandir}/man3/HTTP::Entity::Parser*.3*
%{_examplesdir}/%{name}-%{version}
