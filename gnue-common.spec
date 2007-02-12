Summary:	GNUe Common Library - the basis for the GNUe tools
Summary(pl.UTF-8):   GNUe Common Library - wspólna biblioetka będąca podstawą dla narzędzi GNUe
Name:		gnue-common
Version:	0.5.14
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.gnuenterprise.org/downloads/current/%{name}-%{version}.tar.gz
# Source0-md5:	cb92026b01dc32bdc3b8ea80d3bcbd8f
Patch0:		%{name}-pyc_pyo.patch
URL:		http://www.gnuenterprise.org/
BuildRequires:	python
BuildRequires:	python-devel
Requires:	python
Obsoletes:	GNUe-Common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNUe Common Library is the basis for the GNUe tools, such as
Forms, Reports, Application Server, and Designer.  It implements a
database-abstraction layer that provides support for most major
databases. A builtin XML-to-Object parser and Object-to-XML
marshaller are used by Forms, Reports, and Designer to save and
read Forms/Report definitions to and from an XML file.  It also
defines and implements an RPC abstraction layer that will allow
server processes to define their public methods once and have them
available to CORBA, XML-RPC, SOAP, and DCOM clients.

%description -l pl.UTF-8
GNUe Common Library to podstawa dla narzędzi GNUe tools, takich jak
Forms, Reports, Application Server czy Designer. Implementuje warstwę
abstrakcji dla baz danych dostarczającą obsługę większości popularnych
baz. Wbudowany parser XML do obiektów oraz przekształcanie obiektów
do XML są używane przez Forms, Reports i Designera w celu zapisu i
odczytu definicji Forms/Report do/z pliku XML. Biblioteka definiuje i
implementuje także warstwę abstrakcji RPC pozwalającą procesom serwera
na definiowanie własnych metod publicznych udostępnianych klientom
interfejsów CORBA, XML-RPC, SOAP i DCOM.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gnue/grpc

python setup.py install \
	--install-lib=%{py_sitedir} \
	--prefix=/usr \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -a \! -name paths.py -exec rm {} \;

mv $RPM_BUILD_ROOT/etc/gnue/{sample.,}connections.conf
mv $RPM_BUILD_ROOT/etc/gnue/{sample.,}gnue.conf

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README* TODO doc/*.* doc/technotes
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/gnue
%{_datadir}/gnue
%dir /etc/gnue
%config(noreplace) %verify(not md5 mtime size) /etc/gnue/*.conf
%{_mandir}/man?/*
