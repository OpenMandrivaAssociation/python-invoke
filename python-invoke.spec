Name:		python-invoke
Version:	1.7.3
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/i/invoke/invoke-%{version}.tar.gz
Summary:	Pythonic task execution
URL:		https://pypi.org/project/invoke/
License:	BSD
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Pythonic task execution

%prep
%autosetup -p1 -n invoke-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/inv
%{_bindir}/invoke
%{py_sitedir}/invoke
%{py_sitedir}/invoke-*.*-info
