#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Beautify
Summary:	Beautifies text
Summary(pl):	Upiêkszanie tekstu
Name:		perl-Text-Beautify
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic	
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9858d264133411d5f7f31c7179ebf525
URL:		http://search.cpan.org/dist/Text-Beatuify/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Beautifies text. This involves operations like squeezing double
spaces, removing spaces from the beginning and end of lines, upper
casing the first character in a string, etc.

You can enable / disable features with enable_feature /
disable_feature. These commands return a true value if they are
successful.

%description -l pl
Upiêksza tekst. Wykonuje operacje takie jak usuwanie podwójnych
spacji, usuwanie zbêdnych spacji z pocz±tku i koñca linii, zamiana
pierwszej litery na wielk±, itp.

Mo¿na w³±czyæ / wy³±czyæ konkretn± operacjê za pomoc± enable_feature /
disable_feature. Komendy te zwróc± prawdê je¶li ich wykonanie zakoñczy
siê powodzeniem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Text/Beautify.pm
%{_mandir}/man3/*
