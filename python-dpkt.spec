Summary:	Fast, simple packet creation and parsing
Name:		python-dpkt
Version:	1.7
Release:	3
License:	BSD
Group:		Development/Python
URL:		http://code.google.com/p/dpkt/
Source0:	http://dpkt.googlecode.com/files/dpkt-%{version}.tar.gz
BuildRequires:	python-devel

%description
Fast, simple packet creation and parsing

%prep
%setup -q -n dpkt-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc AUTHORS CHANGES HACKING LICENSE README
%{py_sitedir}/dpkt
%{py_sitedir}/dpkt-%{version}-py%{py_ver}.egg-info


%changelog
* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 1.7-2mdv2011.0
+ Revision: 598985
- rebuild for py2.7

* Sun Sep 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.7-1mdv2011.0
+ Revision: 577742
- new version

* Mon Jan 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.6-1mdv2010.1
+ Revision: 489427
- new version

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.4-8mdv2010.0
+ Revision: 442100
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 1.4-7mdv2009.1
+ Revision: 323627
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.4-6mdv2009.0
+ Revision: 259583
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.4-5mdv2009.0
+ Revision: 247407
- rebuild

* Sat Dec 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-3mdv2008.1
+ Revision: 139211
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Dec 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.4-2mdv2007.0
+ Revision: 96097
- Rebuild for new python
- Import python-dpkt

* Sun Mar 19 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4-1mdk
- initial Mandriva package

