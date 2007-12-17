Summary:	Fast, simple packet creation and parsing
Name:		python-dpkt
Version:	1.4
Release:	%mkrel 2
License:	BSD
Group:		Development/Python
URL:		http://monkey.org/~dugsong/dpkt/
Source0:	http://monkey.org/~dugsong/dpkt/dpkt-%{version}.tar.bz2
BuildRequires:	python-devel

%description
Fast, simple packet creation and parsing

%prep

%setup -q -n dpkt-%{version}

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


