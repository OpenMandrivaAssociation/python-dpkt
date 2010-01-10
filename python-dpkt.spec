Summary:	Fast, simple packet creation and parsing
Name:		python-dpkt
Version:	1.6
Release:	%mkrel 1
License:	BSD
Group:		Development/Python
URL:		http://code.google.com/p/dpkt/
Source0:	http://dpkt.googlecode.com/files/dpkt-%{version}.tar.gz
Patch0:     dpkt-1.6-fix-python2.6.patch
BuildRequires:	python-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Fast, simple packet creation and parsing

%prep
%setup -q -n dpkt-%{version}
%patch0 -p 0

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%doc AUTHORS CHANGES HACKING LICENSE README
%defattr(-,root,root)


