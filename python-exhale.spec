#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-exhale.spec)

Summary:	Automatic C++ library API documentation generator using Doxygen, Sphinx, and Breathe
Summary(pl.UTF-8):	Automatyczny generator dokumentacji API bibliotek C++ wykorzystujący narzędzia Doxygen, Sphinx i Breathe
Name:		python-exhale
# keep 0.2.x here for python2 support
Version:	0.2.4
Release:	0.1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/exhale/
Source0:	https://files.pythonhosted.org/packages/source/e/exhale/exhale-%{version}.tar.gz
# Source0-md5:	fc9e7916c65a2162d8e3850c725cfc7f
URL:		https://pypi.org/project/exhale/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Automatic C++ library API documentation generator using Doxygen,
Sphinx, and Breathe. Exhale revives Doxygen's class/file hierarchies
using reStructuredText for superior markup syntax/websites.

%description -l pl.UTF-8
Automatyczny generator dokumentacji API bibliotek C++, wykorzystujący
narzędzia Doxygen, Sphinx i Breathe. Exhale ożywia hierarchie
klas/plików Doxygena przy użyciu reStructuredText pod kątem składni
znaczników/stron WWW.

%package -n python3-exhale
Summary:	Automatic C++ library API documentation generator using Doxygen, Sphinx, and Breathe
Summary(pl.UTF-8):	Automatyczny generator dokumentacji API bibliotek C++ wykorzystujący narzędzia Doxygen, Sphinx i Breathe
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-exhale
Automatic C++ library API documentation generator using Doxygen,
Sphinx, and Breathe. Exhale revives Doxygen's class/file hierarchies
using reStructuredText for superior markup syntax/websites.

%description -n python3-exhale -l pl.UTF-8
Automatyczny generator dokumentacji API bibliotek C++, wykorzystujący
narzędzia Doxygen, Sphinx i Breathe. Exhale ożywia hierarchie
klas/plików Doxygena przy użyciu reStructuredText pod kątem składni
znaczników/stron WWW.

%prep
%setup -q -n exhale-%{version}

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
%doc LICENSE README.rst
%{py_sitescriptdir}/exhale
%{py_sitescriptdir}/exhale-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-exhale
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/exhale
%{py3_sitescriptdir}/exhale-%{version}-py*.egg-info
%endif
