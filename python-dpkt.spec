Summary:	Fast, simple packet creation and parsing
Name:		python-dpkt
Version:	1.7
Release:	%mkrel 2
License:	BSD
Group:		Development/Python
URL:		http://code.google.com/p/dpkt/
Source0:	http://dpkt.googlecode.com/files/dpkt-%{version}.tar.gz
BuildRequires:	python-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Fast, simple packet creation and parsing

%prep
%setup -q -n dpkt-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS CHANGES HACKING LICENSE README
%defattr(-,root,root)
%{py_sitedir}/dpkt
%{py_sitedir}/dpkt-%{version}-py%{pyver}.egg-info
