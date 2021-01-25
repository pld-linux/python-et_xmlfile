# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		et_xmlfile
Summary:	An implementation of lxml.xmlfile for the standard library
Name:		python-%{module}
Version:	1.0.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/et_xmlfile/
Source0:	https://files.pythonhosted.org/packages/source/e/et_xmlfile/%{module}-%{version}.tar.gz
# Source0-md5:	f47940fd9d556375420b2e276476cfaf
URL:		https://bitbucket.org/openpyxl/et_xmlfile
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
et_xmlfile is a low memory library for creating large XML files.

It is based upon the xmlfile module from lxml with the aim of allowing
code to be developed that will work with both libraries. It was
developed initially for the openpyxl project but is now a standalone
module.

%package -n python3-%{module}
Summary:	An implementation of lxml.xmlfile for the standard library
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-%{module}
et_xmlfile is a low memory library for creating large XML files.

It is based upon the xmlfile module from lxml with the aim of allowing
code to be developed that will work with both libraries. It was
developed initially for the openpyxl project but is now a standalone
module.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
