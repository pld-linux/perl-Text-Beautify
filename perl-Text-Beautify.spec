#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Beautify
Summary:	Beautifies text
Summary(pl):	Upi�kszanie tekstu
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
Upi�ksza tekst. Wykonuje operacje takie jak usuwanie podw�jnych
spacji, usuwanie zb�dnych spacji z pocz�tku i ko�ca linii, zamiana
pierwszej litery na wielk�, itp.

Mo�na w��czy� / wy��czy� konkretn� operacj� za pomoc� enable_feature /
disable_feature. Komendy te zwr�c� prawd� je�li ich wykonanie zako�czy
si� powodzeniem.

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
