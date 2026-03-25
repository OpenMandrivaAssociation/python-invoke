%define module invoke

Name:		python-invoke
Version:	2.2.1
Release:	1
Summary:	Pythonic task execution
License:	BSD-2-Clause
Group:		Development/Python
URL:		https://github.com/pyinvoke/invoke
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Invoke is a Python library for managing shell-oriented subprocesses and
organizing executable Python code into CLI-invokable tasks.

It draws inspiration from various sources (make/rake, Fabric 1.x, etc)
to arrive at a powerful & clean feature set.

%files
%doc README.rst
%{_bindir}/inv
%{_bindir}/invoke
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
