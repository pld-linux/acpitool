Summary:	AcpiTool - Linux ACPI client
Summary(pl.UTF-8):	AcpiTool - linuksowy klient ACPI
Name:		acpitool
Version:	0.5
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://freeunix.dyndns.org:8088/ftp_site/pub/unix/acpitool/%{name}-%{version}.tar.bz2
# Source0-md5:	c4acc19eb002d6871d12abb490593202
Patch0:		%{name}-gcc43.patch
URL:		http://freeunix.dyndns.org:8088/site2/acpitool.shtml
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AcpiTool is (yet another) Linux ACPI client. It's a small command-line
application. Besides "basic" ACPI information like battery status, AC
presence, etc... Acpitool also supports various extensions for
Toshiba, Asus and IBM Thinkpad laptops, allowing you to change the LCD
brightness level, toggle fan on/off, and more.

%description -l pl.UTF-8
AcpiTool to (jeszcze jeden) linuksowy klient ACPI. Jest to mała
aplikacja działająca z linii poleceń. Oprócz "podstawowych" informacji
ACPI, takich jak stan baterii, obecność zasilania AC itp. obsługuje
także różne rozszerzenia dla laptopów Toshiby, Asusa i IBM Thinkpad,
pozwalające zmieniać poziom jasności LCD, włączać i wyłączać
wiatraczki itp.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
