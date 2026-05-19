Summary:	Automatic C++ library API documentation generator using Doxygen, Sphinx, and Breathe
Summary(pl.UTF-8):	Automatyczny generator dokumentacji API bibliotek C++ wykorzystujący narzędzia Doxygen, Sphinx i Breathe
Name:		python3-exhale
Version:	0.3.7
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/exhale/
Source0:	https://files.pythonhosted.org/packages/source/e/exhale/exhale-%{version}.tar.gz
# Source0-md5:	84e7ec2fcec2afa2c8b9c214526bd70e
URL:		https://pypi.org/project/exhale/
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools >= 1:42
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.8
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

%prep
%setup -q -n exhale-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/exhale
%{py3_sitescriptdir}/exhale-%{version}-py*.egg-info
