%define	name	soya
%define	oname	Soya
%define	version	0.13.2
%define	tutver	0.13
%define	rel	1
%define	release	%mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
Url:		http://home.gna.org/oomadness/en/index.html
Source0:	http://download.gna.org/soya/%{oname}-%{version}.tar.bz2
Source1:	http://download.gna.org/soya/%{oname}Tutorial-%{tutver}.tar.bz2
#(peroyvind): do NOT blindly remove this path without ensuring that same behaviour is kept!
#Patch0:		soya-0.12-use-system-ode.patch
Group:		Development/Python
Summary:	A practical high-level object-oriented 3D engine
BuildRequires:	python-devel png-devel SDL-devel cal3d-devel mesaglu-devel
BuildRequires:	ode-devel glew-devel freetype2-devel openal-devel
Requires:	editobj

%description
A practical high-level object-oriented 3D engine.

# (jiba) A separate package for the tutorial
%package	tutorial
Summary:	Tutorial for the Soya 3D engine
License:	GPL
Group:		Development/Python
Requires:	%{name} >= %{version}

%description	tutorial
This is a set of tutorial for Soya.
Soya is a practical high-level object-oriented 3D engine for Python.

%prep
%setup -q -n %{oname}-%{version} -a 1
#%patch0 -p1 -b .ode
rm -rf `find -name CVS` `find -name .cvswrappers`

%build
# needed to generate proper c code for gcc4
#pyrexc _ode.pyx
python setup.py build #--dont-build-ode

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README CHANGES AUTHORS
%{_bindir}/%{name}_editor
%py_platsitedir/%{name}
%py_platsitedir/*.egg-info

%files tutorial
%defattr(644,root,root,0755)
%doc %{oname}Tutorial-%{tutver}/AUTHORS %{oname}Tutorial-%{tutver}/tutorial
