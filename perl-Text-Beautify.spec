#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Beautify
Summary:	Beautifies text
Summary(pl.UTF-8):   Upiększanie tekstu
Name:		perl-Text-Beautify
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d415f26a113ff4846698892029103a88
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

%description -l pl.UTF-8
Upiększa tekst. Wykonuje operacje takie jak usuwanie podwójnych
spacji, usuwanie zbędnych spacji z początku i końca linii, zamiana
pierwszej litery na wielką, itp.

Można włączyć / wyłączyć konkretną operację za pomocą enable_feature /
disable_feature. Komendy te zwrócą prawdę jeśli ich wykonanie zakończy
się powodzeniem.

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
