Summary:	GNUe Common Library is the basis for the GNUe tools
#Summary(pl):	
Name:		gnue-common
Version:	0.5.14
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.gnuenterprise.org/downloads/current/%{name}-%{version}.tar.gz
# Source0-md5:	cb92026b01dc32bdc3b8ea80d3bcbd8f
URL:		http://www.gnuenterprise.org/
BuildRequires:	python
BuildRequires:	python-devel
Requires:	python
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

#%description -l pl

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gnue/grpc

python setup.py install \
	--install-lib=%{py_sitedir} \
	--prefix=/usr \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

# watch out for paths.py
#find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

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
%config(noreplace) %verify(not size mtime md5) /etc/gnue/*.conf
%{_mandir}/man?/*
